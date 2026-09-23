"""Standalone Pandoc/Word edition builder. Run using the configured document Python."""
from pathlib import Path
import argparse
import json
import os
import re
import shutil
import subprocess
import tempfile
from xml.sax.saxutils import escape
from urllib.parse import urlsplit, unquote
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.text.run import Run

TEMPLATE_VERSION='sokointel-premium-3'
LICENSES={
    'CC BY-NC-SA 4.0':('Attribution NonCommercial ShareAlike 4.0 International','https://creativecommons.org/licenses/by-nc-sa/4.0/','You may share and adapt the original material for noncommercial purposes, with attribution, a link to the license and an indication of changes. Distribute adaptations under the same license.'),
    'CC BY-NC-ND 4.0':('Attribution NonCommercial NoDerivatives 4.0 International','https://creativecommons.org/licenses/by-nc-nd/4.0/','You may share the original material for noncommercial purposes with attribution and a link to the license. Modified versions may not be distributed under this license.'),
    'CC BY 4.0':('Attribution 4.0 International','https://creativecommons.org/licenses/by/4.0/','You may share and adapt the original material, including for commercial purposes, with attribution, a link to the license and an indication of changes.')}


def plain_heading(text):
    return re.sub(r'\s+',' ',re.sub(r'[^\w\s]',' ',text.replace('&','and'))).strip()


def image_path(url, root, manifest):
    """Only publication-managed images can be embedded; never fetch a remote URL."""
    parsed=urlsplit(url)
    if parsed.scheme or parsed.netloc or parsed.query:
        raise ValueError('Upload article images to the website before generating editions: '+url[:120])
    name=unquote(parsed.path)
    if name.startswith('/files/'):
        key=name.strip('/').split('/')[-1]
        if not manifest.get(key,{}).get('public'):
            raise ValueError('This image is not a public publication asset: '+url[:120])
        base=root/'content/assets';target=base/key
    elif name.startswith('/media/'):
        base=root/'media';target=base/name[len('/media/'):]
    else:
        raise ValueError('Use an uploaded /media/ or /files/ image URL: '+url[:120])
    target=target.resolve()
    if not target.is_relative_to(base.resolve()) or not target.is_file():
        raise ValueError('The article image could not be found: '+url[:120])
    if target.suffix.lower() not in {'.png','.jpg','.jpeg','.gif','.webp'}:
        raise ValueError('Use a PNG or JPEG edition image: '+url[:120])
    return str(target)


def run(args, **kwargs):
    return subprocess.run(args,check=True,capture_output=True,text=True,encoding='utf-8',timeout=240,**kwargs)


def markdown_to_docx(markdown, output, config):
    pandoc=config['pandoc']
    # Parse first so image targets are validated even in reference-style Markdown.
    parsed=json.loads(run([pandoc,'--from=markdown-raw_html-raw_tex-yaml_metadata_block','--to=json'],input=markdown).stdout)
    catalog_path=Path(config['root'])/'content/catalog.json'
    manifest=json.loads(catalog_path.read_text(encoding='utf-8'))['files'] if catalog_path.is_file() else {}
    def walk(value):
        if isinstance(value,dict):
            if value.get('t')=='Image':value['c'][-1][0]=image_path(value['c'][-1][0],Path(config['root']),manifest)
            if value.get('t')=='Link':
                url=value['c'][-1][0]
                if url.startswith('/') and not url.startswith('//'):value['c'][-1][0]=config['publication_url']+url
            for child in value.values():walk(child)
        elif isinstance(value,list):
            for child in value:walk(child)
    walk(parsed)
    run([pandoc,'--from=json','--to=docx','--output',str(output)],input=json.dumps(parsed,ensure_ascii=False))


def font(style,name,size,bold=False):
    style.font.name=name;style.font.size=Pt(size);style.font.bold=bold
    style.font.italic=False
    style.font.color.rgb=RGBColor(0,0,0)
    rpr=style.element.get_or_add_rPr()
    for fonts in rpr.findall(qn('w:rFonts')):
        for key in list(fonts.attrib):
            if 'theme' in key.lower():del fonts.attrib[key]
        fonts.set(qn('w:eastAsia'),name);fonts.set(qn('w:cs'),name)
    for item in list(rpr):
        if item.tag==qn('w:color'):item.attrib.pop(qn('w:themeColor'),None)


def field(paragraph,instruction):
    element=OxmlElement('w:fldSimple');element.set(qn('w:instr'),instruction)
    paragraph._p.append(element)


def add_front_matter(doc,snapshot):
    for name,size in [('Front Heading',21),('Front Subheading',13)]:
        if name not in doc.styles:doc.styles.add_style(name,WD_STYLE_TYPE.PARAGRAPH)
        style=doc.styles[name];font(style,'Calibri',size,True)
        style.paragraph_format.space_before=Pt(18);style.paragraph_format.space_after=Pt(9)
        style.paragraph_format.keep_with_next=True
    elements=[]
    def p(text='',style=None):
        paragraph=doc.add_paragraph(text,style)
        elements.append(paragraph._p)
        return paragraph
    brand=p('SOKOINTEL','Subtitle')
    for r in brand.runs:r.bold=True;r.font.color.rgb=RGBColor.from_string('173D33')
    p('A Philtechent Ltd publication','Caption')
    title=p(plain_heading(snapshot['title']),'Title')
    title.paragraph_format.space_before=Pt(65)
    p(snapshot['description'],'Subtitle')
    p('Research through '+snapshot['research_date'],'Caption')
    p('sokointel.com','Caption')
    p('RESEARCH EDITION','Caption').paragraph_format.space_before=Pt(28)
    end=p();end.paragraph_format.page_break_before=True
    p('Research questions','Front Heading')
    for i,q in enumerate(snapshot['questions'],1):p(f'{i}. {q}')
    p('Reading path','Front Heading')
    p('The main articles develop the argument and worked examples. Technical appendices follow the relevant article, with calculations, formula dictionaries and source references where supplied.')
    field(p(),'TOC \\o "1-1" \\h \\z \\u')
    metadata=p('Publication details and license','Front Heading')
    metadata.paragraph_format.page_break_before=True
    for label,value in [('Title',snapshot['title']),('Publication','Sokointel'),('Publisher and rights holder','Philtechent Ltd'),('Edition date',snapshot['edition_date']),('Research cutoff',snapshot['research_date']),('Edition identifier',snapshot.get('identifier',TEMPLATE_VERSION)),('Language','English'),('Canonical publication',snapshot['canonical_url'])]:
        row=p();row.paragraph_format.space_after=Pt(7)
        row.add_run(label+'  ').bold=True;row.add_run(value)
        for r in row.runs:r.font.name='Calibri';r.font.size=Pt(11)
    p('Creative Commons license','Front Subheading')
    license_name,license_url,license_summary=LICENSES[snapshot['license']]
    for text in [f"© {snapshot['edition_date'][:4]} Philtechent Ltd. Except where separately credited, original content in this publication is licensed under {snapshot['license']}.",license_name,license_summary,license_url,'Suggested attribution: Sokointel, '+snapshot['title']+', Philtechent Ltd, '+snapshot['edition_date']+'. '+snapshot['canonical_url'],'Third-party material retains the rights and license terms stated by its respective source. Source citations identify the supporting evidence and do not change those terms.']:
        paragraph=p(text)
        paragraph.paragraph_format.line_spacing=1.1
        for r in paragraph.runs:r.font.name='Calibri';r.font.size=Pt(11)
    for element in reversed(elements):doc._element.body.insert(0,element)
    # Start the manuscript after the auto-sized front matter.
    next_element=elements[-1].getnext()
    if next_element is not None and next_element.tag==qn('w:p'):
        from docx.text.paragraph import Paragraph
        Paragraph(next_element,doc).paragraph_format.page_break_before=True


def format_document(path,snapshot,config):
    doc=Document(path)
    body_font=config.get('body_font','Georgia');sans=config.get('heading_font','Calibri')
    for section in doc.sections:
        section.page_width=Inches(8.5);section.page_height=Inches(11)
        section.left_margin=section.right_margin=Inches(.85)
        section.top_margin=Inches(.85);section.bottom_margin=Inches(.8)
        section.header_distance=section.footer_distance=Inches(.35)
        section.different_first_page_header_footer=True
        header=section.header.paragraphs[0]
        header.text='SOKOINTEL  /  '+plain_heading(snapshot['series_title'])
        for r in header.runs:r.font.name=sans;r.font.size=Pt(9);r.font.color.rgb=RGBColor(0,0,0)
        footer=section.footer.paragraphs[0]
        footer.text='sokointel.com   ·   Philtechent Ltd'
        footer.add_run(' '*6+'|   ');field(footer,'PAGE')
        footer.alignment=WD_ALIGN_PARAGRAPH.RIGHT
        for r in footer.runs:r.font.name=sans;r.font.size=Pt(9)
    for style in doc.styles:
        if style.type==1:
            font(style,body_font,12)
            pf=style.paragraph_format
            pf.space_after=Pt(9);pf.line_spacing=1.18;pf.widow_control=True
            pf.keep_together=False;pf.keep_with_next=False
    styles={s.name:s for s in doc.styles}
    for name,size in [('Title',32),('Subtitle',14),('Heading 1',21),('Heading 2',16),('Heading 3',13),('Heading 4',12),('Heading 5',11)]:
        if name not in styles:continue
        style=styles[name];font(style,body_font if name=='Title' else sans,size,name not in ['Subtitle','Title'])
        style.paragraph_format.space_before=Pt(20 if name!='Title' else 0)
        style.paragraph_format.space_after=Pt(9)
        style.paragraph_format.line_spacing=1.1;style.paragraph_format.keep_with_next=True
        style.paragraph_format.alignment=WD_ALIGN_PARAGRAPH.LEFT
    for name in ['Caption','TOC 1','TOC 2']:
        if name in styles:
            font(styles[name],sans,11)
            styles[name].paragraph_format.line_spacing=1.1
    for name in ['Source Code','Block Text']:
        if name in styles:
            font(styles[name],sans if name=='Block Text' else 'Consolas',11)
            styles[name].paragraph_format.line_spacing=1.12
    for p in doc.paragraphs:
        if p.style.name.startswith('Heading'):
            p.paragraph_format.keep_with_next=True
            if p.style.name=='Heading 1':p.paragraph_format.page_break_before=True
        if p.text.startswith('[') and re.match(r'^\[\d+\]',p.text):
            for element in p._p.xpath('.//w:r'):
                r=Run(element,p);r.font.name=sans;r.font.size=Pt(11)
            p.paragraph_format.line_spacing=1.12
        if p.text.startswith(('Mathematical equivalence:','Units and scope:')):
            p.paragraph_format.keep_with_next=True
        if p._p.xpath('.//w:drawing'):
            p.alignment=WD_ALIGN_PARAGRAPH.CENTER;p.paragraph_format.keep_together=True
        # Excel expressions remain editable; line wrapping is typographic only.
        if p.style.name=='Source Code':
            p.paragraph_format.keep_together=len(p.text)<1000
            p.paragraph_format.space_after=Pt(12)
            for r in p.runs:
                r.font.name='Consolas';r.font.size=Pt(11)
                r.text=re.sub(r'([,;*/+=^()\[\]])',lambda m:m[1]+'\u200b',r.text)
        for r in p.runs:
            if r.style and 'verbatim' in r.style.name.lower():
                r.font.name='Consolas';r.font.size=Pt(11)
                r.text=re.sub(r'([,;*/+=^()\[\]])',lambda m:m[1]+'\u200b',r.text)
    for shape in doc.inline_shapes:
        factor=min(1,Inches(6.75)/shape.width,Inches(6.1)/shape.height)
        shape.width=int(shape.width*factor);shape.height=int(shape.height*factor)
    for table in doc.tables:
        table.alignment=WD_TABLE_ALIGNMENT.CENTER;table.autofit=False
        n=len(table.columns)
        weights=[]
        for j in range(n):
            lengths=[len(row.cells[j].text) for row in table.rows]
            weights.append(max(7,min(55,(sum(lengths)/max(1,len(lengths)))**.65*3)))
        widths=[6.75*w/sum(weights) for w in weights]
        for col,width in zip(table.columns,widths):col.width=Inches(width)
        for i,row in enumerate(table.rows):
            trpr=row._tr.get_or_add_trPr()
            no_split=OxmlElement('w:cantSplit');trpr.append(no_split)
            if i==0:trpr.append(OxmlElement('w:tblHeader'))
            for j,cell in enumerate(row.cells):
                cell.width=Inches(widths[j]);cell.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
                props=cell._tc.get_or_add_tcPr()
                borders=OxmlElement('w:tcBorders')
                for side in ['top','left','bottom','right']:
                    edge=OxmlElement('w:'+side);edge.set(qn('w:val'),'single');edge.set(qn('w:sz'),'4');edge.set(qn('w:color'),'D9D9D9');borders.append(edge)
                props.append(borders)
                shade=OxmlElement('w:shd');shade.set(qn('w:fill'),'24374B' if i==0 else 'F2F5F7' if i%2 else 'FFFFFF');props.append(shade)
                margins=OxmlElement('w:tcMar')
                for side in ['top','left','bottom','right']:
                    mar=OxmlElement('w:'+side);mar.set(qn('w:w'),'100');mar.set(qn('w:type'),'dxa');margins.append(mar)
                props.append(margins)
                for p in cell.paragraphs:
                    p.paragraph_format.space_before=Pt(3);p.paragraph_format.space_after=Pt(3)
                    p.paragraph_format.line_spacing=1.12;p.paragraph_format.keep_with_next=False
                    for r in p.runs:
                        r.font.name=sans;r.font.size=Pt(11)
                        r.font.color.rgb=RGBColor.from_string('FFFFFF' if i==0 else '000000')
                        if i==0:r.bold=True
                        if len(r.text)>65 and not ' ' in r.text:r.text=re.sub(r'([,;*/+=])',lambda m:m[1]+'\u200b',r.text)
    add_front_matter(doc,snapshot)
    for style in doc.styles:
        if style.type==1:
            for border in style.element.xpath('.//w:pBdr'):border.getparent().remove(border)
    for color in doc._element.xpath('.//w:pStyle/../w:color'):color.attrib.pop(qn('w:themeColor'),None)
    doc.core_properties.author='Sokointel | Philtechent Ltd'
    doc.core_properties.title=snapshot['title'];doc.core_properties.subject=snapshot['series_title']
    doc.core_properties.keywords='Sokointel, research, '+TEMPLATE_VERSION
    doc.core_properties.identifier=snapshot.get('identifier',TEMPLATE_VERSION)
    doc.core_properties.language='en'
    doc.core_properties.comments=snapshot['license']+' | '+LICENSES[snapshot['license']][1]+' | '+snapshot['canonical_url']
    doc.save(path)


def convert_pdf(docx,pdf,config):
    if config['pdf_engine']=='word':
        script=Path(__file__).with_name('export_edition_word.ps1')
        run(['powershell.exe','-NoProfile','-NonInteractive','-ExecutionPolicy','Bypass','-File',str(script),'-DocumentPath',str(docx),'-PdfPath',str(pdf)])
    elif config['pdf_engine']=='libreoffice':
        soffice=config.get('soffice') or shutil.which('soffice')
        if not soffice:raise RuntimeError('Configure SOFFICE_BIN for the PDF worker.')
        with tempfile.TemporaryDirectory(prefix='sokointel-lo-') as profile:
            run([soffice,'-env:UserInstallation='+Path(profile).as_uri(),'--headless','--convert-to','pdf:writer_pdf_Export','--outdir',str(pdf.parent),str(docx)])
    else:raise ValueError('EDITION_PDF_ENGINE must be word or libreoffice.')
    if not pdf.is_file() or pdf.stat().st_size<1000:raise RuntimeError('The PDF converter did not produce a complete edition.')


def build(payload,output):
    output.mkdir(parents=True,exist_ok=True)
    snapshot=payload['snapshot'];parts=[]
    for article in snapshot['articles']:
        parts.append('# '+article['title']+'\n\n'+article['body'])
        if article['appendix'].strip():parts.append(article['appendix'])
    docx=output/(snapshot['slug']+'.docx');pdf=docx.with_suffix('.pdf')
    markdown_to_docx('\n\n'.join(parts),docx,payload['config'])
    format_document(docx,snapshot,payload['config'])
    convert_pdf(docx,pdf,payload['config'])
    from pypdf import PdfReader,PdfWriter
    from pypdf.generic import DecodedStreamObject,NameObject
    original=PdfReader(pdf);writer=PdfWriter();writer.clone_document_from_reader(original)
    license_url=LICENSES[snapshot['license']][1]
    writer.add_metadata({'/Title':snapshot['title'],'/Author':'Sokointel | Philtechent Ltd','/Subject':snapshot['series_title'],
                         '/Keywords':TEMPLATE_VERSION+', '+snapshot['license'],'/License':license_url,
                         '/Publisher':'Philtechent Ltd','/ResearchCutoff':snapshot['research_date'],'/EditionDate':snapshot['edition_date'],
                         '/Identifier':snapshot.get('identifier',TEMPLATE_VERSION),'/Source':snapshot['canonical_url']})
    xmp=f'''<?xpacket begin="\ufeff"?><x:xmpmeta xmlns:x="adobe:ns:meta/"><rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"><rdf:Description rdf:about="" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:xmpRights="http://ns.adobe.com/xap/1.0/rights/"><dc:title><rdf:Alt><rdf:li xml:lang="x-default">{escape(snapshot['title'])}</rdf:li></rdf:Alt></dc:title><dc:creator><rdf:Seq><rdf:li>Sokointel</rdf:li></rdf:Seq></dc:creator><dc:publisher><rdf:Bag><rdf:li>Philtechent Ltd</rdf:li></rdf:Bag></dc:publisher><dc:rights><rdf:Alt><rdf:li xml:lang="x-default">{escape(snapshot['license'])}</rdf:li></rdf:Alt></dc:rights><dc:identifier>{escape(snapshot.get('identifier',TEMPLATE_VERSION))}</dc:identifier><dc:source>{escape(snapshot['canonical_url'])}</dc:source><dc:date><rdf:Seq><rdf:li>{snapshot['edition_date']}</rdf:li></rdf:Seq></dc:date><xmpRights:WebStatement>{license_url}</xmpRights:WebStatement><xmpRights:Marked>True</xmpRights:Marked></rdf:Description></rdf:RDF></x:xmpmeta><?xpacket end="w"?>'''
    metadata=DecodedStreamObject();metadata.set_data(xmp.encode('utf-8'));metadata[NameObject('/Type')]=NameObject('/Metadata');metadata[NameObject('/Subtype')]=NameObject('/XML')
    writer._root_object[NameObject('/Metadata')]=writer._add_object(metadata)
    temp=pdf.with_suffix('.metadata.pdf');writer.write(temp);os.replace(temp,pdf)
    reader=PdfReader(pdf)
    if len(reader.pages)<1 or not any((p.extract_text() or '').strip() for p in reader.pages):raise RuntimeError('The generated PDF has no readable content.')
    report={'docx':docx.name,'pdf':pdf.name,'pages':len(reader.pages),'template':TEMPLATE_VERSION}
    (output/'result.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps(report))


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('payload');parser.add_argument('output')
    args=parser.parse_args()
    build(json.loads(Path(args.payload).read_text(encoding='utf-8')),Path(args.output))

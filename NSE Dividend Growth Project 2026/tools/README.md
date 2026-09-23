# NSE Dividend Growth publishing workflow

1. Run \`prepare_manuscript.py\` to make the punctuation-only em-dash substitutions and create the two Markdown parts.
2. Run \`build_publications.py\` to create the branded Word and PDF editions in \`Publication/Output\`.
3. Run \`build_formula_workbook.mjs\` to create the editable formula dictionary workbook.
4. Run \`validate_publications.py\` after a build to verify source reconstruction and output integrity.

The publication builder uses Pandoc for Markdown-to-Word conversion and Word for the final PDF export. The retained \`edition_document.py\` and \`export_edition_word.ps1\` tools provide the same Sokointel branding, metadata, reading path and CC BY-NC-SA 4.0 license page used by the website editions.

# Next endeavours plan

## Purpose

Build Sokointel as a working research library. A reader should be able to move from a useful question to a dated source, an inspectable calculation, a reusable workbook, and a deeper member edition. The financial-material folder remains the research and publication workspace. The business website blog becomes the reader-facing home for articles, tools, member resources, and updates.

## Product structure

### Open learning layer

Every research path begins with a short article, an interactive visual or calculator, and a practical explanation of the model. Public tools should make a financial decision easier to explore without requiring a download or membership.

The priority public tools are:

1. Compounding and real-value explorer.
2. Dividend-income, withholding-tax, and reinvestment explorer.
3. DCA allocation planner with whole-share rounding and transaction-cost reserve.
4. Portfolio-weight and contribution-rebalancing explorer.
5. Kenyan household cash-flow, PAYE, pension, medical-reserve, and mortgage tools.
6. International-investing allocation, currency-conversion, and remittance-cost explorer.
7. DCF and dividend-discount learning tools with explicit assumptions and formula displays.

Each tool should link to its related article section, formula dictionary, workbook, and collection page. The display should show inputs, arithmetic, results, and the source date for any prefilled market data.

### Member research layer

One research membership should provide complete PDF editions, editable Word editions, detailed workbooks, formula dictionaries, source ledgers, combined collection PDFs, ZIP packages, and monthly research notes.

The research collections remain the centre of the membership. Newsletters, calculators, and public articles should lead naturally into the relevant collections.

### Power-user workbook layer

Use three levels of workbook delivery:

1. Open calculator: a web tool for immediate exploration.
2. Workbook template: an editable Excel file with documented inputs, formulas, controls, source table, and scenario tabs.
3. Optional add-in: an eventual reusable Excel add-in for repeated functions, portfolio checks, model imports, and report preparation.

The add-in work begins after workbook formulas have stabilized. The first technical decision is whether to build a cross-platform Office JavaScript add-in for broad reach, an Excel-DNA .NET add-in for powerful Windows desktop workflows, or both with clearly separated scope. Workbook files should remain useful without an add-in.

## Research programme

### Existing four collections

For African markets and business credit, international investing and diaspora finance, Kenyan tax and household finance, and Kenyan equities and company analysis:

- Maintain a source ledger with publication date, access date, source type, claim supported, and update cadence.
- Link practical calculations to the workbook and relevant calculator.
- Turn each research question into a navigation anchor on the website, in the PDF reading path, and in future presentation slides.
- Refresh market prices, tax thresholds, platform availability, and regulatory references on a stated cycle.
- Make each workbook a detailed but readable companion: inputs, calculations, outputs, sensitivity or scenario sections, formula dictionary, and source table.

### NSE dividend-growth research

Publish the two-part NSE Dividend Growth DCA and Watchlist collection as the fifth Sokointel series:

- Part one: core portfolio construction, transaction-cost reserve, three-month DCA schedule, dividend income, tax, and stress testing.
- Part two: watchlist selection, diversification, bank-replacement comparisons, monitoring, and portfolio expansion.
- Companion workbook: inputs, core portfolio, DCA plan, income scenarios, and formula dictionary.
- Public calculator: DCA allocation and dividend-income explorer.
- Member assets: two Word editions, two PDFs, formula workbook, combined reading edition, and ZIP collection.
- Website content: dated research snapshot, source links, price-reference disclosure, edition metadata, and direct links between article, workbook, calculator, and collection.

### New research paths from the organised source material

1. US markets and portfolio construction: core, core-plus, and core-satellite architectures; ETF roles; factor concentration; fee comparison; rebalancing; QQQ and QQQM comparison; semiconductor-sleeve comparison; and the role of SMH and SOXX.
2. NSE value investing and dividend growth: circle of competence, business quality, liquidity, valuation, margin of safety, and portfolio sizing in the Kenyan market.
3. Excel financial tools and add-ins: a practical product-design guide for calculator templates, documented workbooks, and the eventual add-in roadmap.

The reader route should begin with a broad-market core, then use a deliberate satellite allocation rather than accidental concentration.

## Research and data standards

1. Put the research cutoff date on every article, workbook, PDF, and calculator page that includes market, tax, or platform data.
2. Record the source URL and captured input beside every market-sensitive calculation.
3. Use historical statements, official company disclosures, fund documents, exchange notices, regulators, and peer-reviewed sources where they answer the question.
4. Keep sourced numbers separate from editable inputs so readers can see what was observed, assumed, and calculated.
5. Use scenario testing and sensitivity analysis for genuinely variable inputs. Do not create artificial precision where a source is missing.
6. Build a claim-to-source review before publication: claim, source, date, relevant page or table, and editorial status.
7. Preserve an archived edition when a refreshed price, tax rate, or policy changes a released calculation.

## Publishing workflow

1. Draft and maintain the source manuscript in Markdown.
2. Run Markdown checks for title, links, research-date metadata, source references, punctuation, and table structure.
3. Generate web-ready article content, Word editions, PDFs, workbook companions, and a collection package from the same approved manuscript.
4. Render the editions for layout review.
5. Build or update the website series, articles, downloadable resources, workbook links, calculator links, and membership package.
6. Run site tests and content-link checks.
7. Publish the public article and calculator, then release the member edition and newsletter sequence.
8. Add the release to the research calendar, source-refresh register, and video or presentation backlog.

## Website work

### Immediate work

- Replace the Altman Z-score page with calculators that match the financial-material research library.
- Keep the existing compounding explorer and add a calculator index page.
- Add the NSE Dividend Growth DCA and Watchlist series in the same visual and resource pattern as the first four collections.
- Update home-page counts, research cards, library filters, workbook library, bundle pages, sitemap, and member resource list through the data-driven series model.
- Add the DCA and dividend-income calculator as a public lead tool for the NSE collection.
- Build the NSE combined PDF and member ZIP package after the two editions and workbook are imported.

### Information architecture

Every series page should contain research questions, a simple reading path, article cards, a public tool or visual, the detailed workbook card, the complete member edition, related collections, and a dated source-update note.

Every article page should contain a concise introduction tied to a reader question, a linked table of contents, inline visuals only where they clarify a decision, a companion-calculator link at the relevant calculation, a workbook link with a clear description of editable inputs, and a link to the next article and complete collection.

## Visual and presentation programme

The YouTube and presentation programme should reuse the research-question structure:

1. Start with the reader question.
2. Show the relevant dated data or company evidence.
3. Explain the calculation with a simple diagram.
4. Show the scenario or sensitivity result.
5. Demonstrate the workbook or calculator.
6. Close with the research path and next question.

Use the Sokointel palette: paper background, deep green text, muted sage surfaces, and restrained orange for action or change. Slides should have generous whitespace, one argument per slide, a readable chart, and a visible source line. Use real numbers with an as-of date for charts involving prices, yields, taxes, or returns.

## Folder structure

### Financial material

- African Markets and Business Credit
- International Investing and Diaspora Finance
- Kenyan Tax and Household Finance
- Kenyan Equities and Company Analysis
- NSE Dividend Growth Project 2026
- US Markets and Portfolio Construction
- NSE Value Investing and Dividend Growth
- Excel Financial Tools and Add-ins
- Publishing and Video Production
- Source Ledgers
- Release Archive

Every new collection should contain Research Notes, Source Word when imported documents exist, Manuscripts, Workbooks, Publication, Presentation, and Sources.

### Business website blog

- content for imported and versioned publication assets.
- apps/core for research series, articles, collections, and edition generation.
- apps/calculators for public tools and their calculation logic.
- docs for product, publishing, data, and technical plans.
- scripts for imports, package generation, audits, and release checks.
- output for generated collection PDFs and ZIP packages.

## Delivery sequence

### Phase 1: Establish the fifth collection

- Import the NSE series, articles, PDFs, Word editions, and workbook.
- Add the DCA and dividend-income calculator.
- Build the member package and update website navigation.
- Publish the first NSE collection release.

### Phase 2: Connect reading and calculation

- Add calculator index, calculator cards, and article-level links.
- Add workbook landing cards with formula dictionaries and a clear description of editable inputs.
- Link public calculators to the relevant collection and workbook.

### Phase 3: Build the next research collections

- Turn the organised US-markets, NSE-value, and Excel-tools notes into sourced research briefs.
- Set research questions before drafting.
- Build article, workbook, calculator, PDF, presentation, and newsletter paths together.

### Phase 4: Add reusable modelling infrastructure

- Standardise source ledgers, formula dictionaries, validation checks, scenario blocks, and edition metadata.
- Create a workbook-template standard for common financial models.
- Prototype the add-in after repeated calculations and user workflow have been proven in templates.

### Phase 5: Operate a sustainable research cadence

- Monthly: newsletter, price and source refresh list, and one useful calculator or workbook improvement.
- Quarterly: full collection update where data has changed materially.
- Annually: archive a dated edition and review the research roadmap, membership resources, and video catalogue.

## Success measures

- Each public article leads naturally to a useful calculator, workbook, or member edition.
- Each calculator displays its inputs and formula path clearly.
- Every market-sensitive number has a source date and traceable source.
- Every member workbook has an editable input area, formula dictionary, source table, and scenario section.
- Every collection has a coherent article, edition, workbook, calculator, and presentation path.
- Readers can move from a free tool to deeper research without losing the question they started with.

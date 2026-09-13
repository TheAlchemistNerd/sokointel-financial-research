# Financial Material Research Library

## Purpose and scope

This repository is the working research library for a set of connected financial-education projects. It brings together long-form articles, technical appendices, workbooks, data notes, graphics, video-production guides and publication material covering Kenyan equities, dividend growth, international investing, portfolio construction, household finance and related market subjects. The library is designed to be useful in two settings at once. It is a durable source workspace for writers and editors, and it is the editorial foundation for articles, companion workbooks and video episodes published through the SokoIntel website.

The materials are organized as research projects rather than as one large undifferentiated collection of drafts. Each project has its own question, reader path, sources and practical tools. The projects nevertheless share a common discipline: define the investment question clearly, state the economic mechanism, identify the evidence and date used, separate facts from illustrative assumptions, explain the relevant calculation, and provide a path for a reader to reproduce the work in a workbook where that is useful.

The library is not a trade-alert archive or a collection of static price claims. A quoted market price is useful only with a date, source and purpose. A fund expense ratio must be identified as gross, net, total or prospectus expense as appropriate. A tax or legal observation must state the taxpayer facts and jurisdiction to which it applies. These conventions help a reader distinguish a reusable analytical method from a time-limited observation.

## Research projects

The principal folders each serve a defined purpose.

- **NSE Dividend Growth Project 2026** develops dividend-growth analysis for listed Kenyan businesses. It focuses on business quality, distributable cash flow, payout capacity, balance-sheet resilience, valuation discipline and the difference between a high current yield and a sustainable growing distribution.

- **Kenyan Equities and Company Analysis** applies company analysis to actual Kenyan listed businesses. It is the place for reading annual reports, assessing revenue and margin drivers, analysing capital allocation, examining balance-sheet risks and forming evidence-based valuation ranges. The project uses real-company facts rather than invented market prices.

- **NSE Value Investing and Dividend Growth** remains a research source while its distinct material is incorporated into the dividend-growth and company-analysis work. It should not be treated as a parallel publication track without checking the material map and source ledger.

- **US Markets and Portfolio Construction** is a progressive capital-markets and portfolio-construction series. It begins with markets, benchmarks and fund wrappers, then examines ownership and cross-border implementation, portfolio architecture, broad cores, deliberate tilts, thematic satellites, options income, rebalancing, withdrawals and review. Its companion workbook uses live formulas so assumptions can be changed without retyping calculations.

- **International Investing and Diaspora Finance** addresses the practical questions that arise when an investor earns, saves, moves or supports family across borders. It considers fund domicile, tax residence, currency, transfers, custody, remittances and the household purpose of money. This series uses its existing Unicode mathematical notation where that has already been established; the other projects use TeX notation for formulas in Markdown.

- **Kenyan Tax and Household Finance**, **African Markets and Business Credit**, and **Excel Financial Tools and Add-ins** supply related analytical material and tools. They should be read in their stated project context rather than treated as interchangeable investment guidance.

- **Publishing and Video Production** contains production assets, reusable episode guides, workflow material and publishing resources that connect research to the website and video channel.

## Editorial model

A research project starts with a concrete question, not a product, ticker or conclusion. The author records the intended reader, the question to be answered, the sources likely to be needed, the assumptions that need testing and the practical outcome a reader should be able to reach. The project is then divided into parts that follow a reader’s decision sequence. A series should define concepts before it asks a reader to apply them. For example, a portfolio series should explain exposure, benchmark, fund structure and total implementation cost before it asks a reader to select a core holding or a tactical sleeve.

Each article should make clear which statements are current observations and which are examples. Current observations require a source and retrieval date. Examples should use stated inputs and should be labelled as illustrative. When a calculation appears in an article, the Markdown should present the mathematical relationship in TeX. The article can say how the calculation is made in Excel, but cell-specific formula documentation belongs in the workbook. This keeps the article readable while allowing the workbook to remain a transparent, editable model.

Tables are part of the argument, not decoration. A table needs a meaningful title or nearby introduction, clear column headings, consistent units and enough surrounding text to explain what a reader may and may not infer from it. The website renderer wraps tables for accessible horizontal scrolling and preserves MathJax expressions. External research sources should be linked directly and open in a separate browser tab so readers can retain their place in the article.

The public site has a structured editorial workflow. Research editors frame the question and prepare the manuscript. Publishing editors review sources, tables, headings, image descriptions and release readiness. Edition operators generate or inspect downloadable editions. Membership operators manage plans and prices. Public comments are moderated before display, while designated editorial staff can attach internal notes to specific source lines or quoted passages. This creates an audit trail and reduces the risk that publishing knowledge is held by one person.

## Workbooks and calculators

Companion workbooks are the place for transparent, editable calculations. They are intended to complement an article, not replace the reasoning in it. Workbook sheets must distinguish input cells from formulas, identify units and currencies, state whether a value is historical or illustrative, and include sources and dates for external inputs. A reader should be able to change a return assumption, contribution amount, holding weight, correlation, expense ratio, withdrawal or tax input and see the dependent calculations update.

The US Markets workbook is maintained as one authoritative file. It combines fund inputs, fee drag, allocation and blended cost, diversification, concentration, risk, wheel mechanics, tax scenarios, rebalancing, dollar-cost averaging, sequence risk and the case-study model. Older workbooks and build scripts may remain in the project as source material or archives, but they are not a second reader-facing workbook. Formula extensions should be integrated into the authoritative workbook only after formula checks, recalculation and source review.

Browser calculators on the website are deliberately compact learning and planning tools. They use browser-side JavaScript and retain a visitor’s recent inputs locally where the calculator design calls for it. They do not reveal workbook structure, research inputs, source ledgers or premium workbook templates. The workbooks retain their value through their linked models, detailed assumptions, sensitivity analysis, documentation and editorial context.

## Sources and data retrieval

Source quality is part of the research result. Use primary sources first: exchange notices, company annual reports, audited financial statements, issuer prospectuses, fund fact sheets, regulatory publications, tax authority guidance and official data releases. Record the publication or retrieval date, the instrument or company identifier, the relevant jurisdiction, and the precise page or section where practical. Secondary commentary can provide context or identify questions, but it should not be the sole basis for a material factual claim when a primary source is available.

For equity research, retain the source record that supports revenue, earnings, dividends, shares outstanding, debt, cash flow, capital expenditure, payout decisions and corporate actions. For funds, retain benchmark definition, legal domicile, expense definition, holdings methodology, distribution policy and trading information. For cross-border analysis, separate the investor’s residence, citizenship where relevant, account location, fund domicile, listing venue, withholding position, currency route and eventual spending currency. These are different facts and should not be collapsed into a single label such as “international investment”.

Market data changes. Price tables should identify the observation date and describe an appropriate use, such as a historical order-size illustration. They should not imply that different dates form a same-day comparison. Tax figures and regulations require special care because they can change through legislation, administrative guidance or personal facts. When in doubt, preserve the calculation method, document the source and date, and state the condition that would require the reader to verify the current rule.

## Visual and video assets

Charts, diagrams and infographics should explain a decision or mechanism that would otherwise take more text to understand. A visual needs descriptive alternative text, a clear caption where useful and a connection to the surrounding argument. The US Markets series, for example, uses a fund-decision hierarchy, cross-border workflow, portfolio architecture map, strategy rings and an options-wheel cycle. These visuals complement each other. No useful diagram should be removed merely because a newer visual covers a different aspect of the series.

Video episodes are produced through reusable project-specific guides. Staff use the guide to prepare the episode objective, outline, visual cues, screen demonstration, citations, chapters and publication metadata. The completed episode is uploaded through the organisation’s YouTube Studio account. A publishing editor then adds the video URL to the relevant article through Django Admin. Until a valid URL exists, the article displays a planned-video placeholder. YouTube embedding itself does not require an application API key.

## Technology and operations

The publishing application is maintained in the separate `business and technical website blog` workspace. It uses Django, MathJax-aware Markdown rendering, role-based editorial access, a local PostgreSQL migration path, a consent-aware transactional-email design and configurable membership prices. Secrets such as database URLs, email tokens, payment keys and production secret keys belong in private environment configuration or the hosting platform’s secret store. They must never be stored in Markdown, workbooks, screenshots, commits or generated public editions.

Postmark is the configured transactional-email direction. It requires a verified sender or domain and a private server token before live delivery is enabled. Paystack, Stripe and IntaSend are planned payment options. Their keys, callback URLs and webhook signing configuration are needed only when live checkout and verified entitlement processing are implemented. Any payment event must be verified on the server before membership access changes. A pricing record belongs in the administration workflow, where markets, currencies, provider availability, review dates and purchasing-power assumptions can be updated without code changes.

## Repository conventions

This Git repository starts with the documentation and ignore policy so that source control can be introduced deliberately. The first commit contains the root README and `.gitignore` only. Existing research files remain untracked until they have been reviewed for provenance, secret exposure, generated status and intended retention. The `.gitignore` excludes environments, secrets, databases, local caches, temporary Office files, generated editions, build directories, packaged archives and downloaded data caches. It does not exclude Markdown, approved workbooks, charts or research-source documents by default.

Use descriptive, focused commits. A manuscript revision, workbook formula correction, source-ledger update, renderer fix and generated release should not be mixed in one commit. Generated artefacts should be reproducible from tracked source or placed in a release system, rather than committed casually. Before committing, inspect the staged diff, confirm that no secret or personal data is present, ensure Markdown has no accidental em dashes where the editorial style forbids them, and run the proportionate checks for the change.

## Working with the library

Begin with the project README, guide or material map nearest to the work you are doing. Preserve working research that has not yet been incorporated. When merging related material, map each unique concept to its destination before editing so that the final reader path remains coherent. Prefer improving a single authoritative article, workbook or graphic over maintaining parallel versions that answer the same question. If two pieces of material answer different questions, keep both and explain the boundary between them.

The measure of success for this library is not the number of files it contains. It is whether a reader, editor or future maintainer can trace a published claim to evidence, understand a calculation, update a dated observation, reproduce a workbook result, publish a revised edition and create a video episode without depending on undocumented knowledge. This repository provides the shared structure for that work.
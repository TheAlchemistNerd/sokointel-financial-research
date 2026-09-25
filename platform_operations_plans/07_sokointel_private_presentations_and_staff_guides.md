# Sokointel: private presentations and staff production guides

Date: 25 September 2026  
Status: planned; implementation has not started for this delivery workflow.

## Purpose and current boundary

Make each article/video episode's editable PowerPoint, exported PDF deck and recording guide available through a staff-only Sokointel page. Keep the research repository as the source of the presentation package, and use private object storage for published delivery files.

The presentation package currently lives in the research repository. Automatic bucket uploads, production PDF deck exports and staff guide pages are not yet wired together. Enabling a bucket alone will not upload presentations, create document records or publish internal pages. Existing review exports are evidence of review, not a complete published PDF deck library.

Presentation production and publishing must remain separate from the reading-PDF background worker. Reader visits, article imports and staff downloads must not trigger presentation conversion or a full-library rebuild.

## Required connections

| Area | Planned behavior |
| --- | --- |
| Private storage | Upload each approved PowerPoint and its exported PDF deck to a private bucket under version-specific object keys. |
| Document records | Retain article/episode association, stable document identifier, version, source fingerprint, generation date, storage references and publication status. |
| Internal guide pages | Show the recording guide, slide index, source references and links to the matching PowerPoint and PDF deck. |
| Staff permissions | Check the user's role before allowing either page access or file downloads. Public membership alone does not grant staff production access. |

## Task 1 — Define the publication manifest and version contract

Extend the existing episode manifest without discarding workbook references, screenshot provenance or QA results. Separate a stable episode/document identifier from the identifier for a particular published version.

Each version should record:

- Article and series codes, episode identifier and title.
- Version identifier, source revision and source fingerprint covering the relevant deck inputs, guide content, evidence and template version.
- Build fingerprint covering the conversion settings and converter version, so a rendering change can justify a new build even when the source text is unchanged.
- Generation time in UTC, publication time, publishing staff member and review status.
- PowerPoint and PDF storage keys, MIME types, byte sizes and individual SHA-256 checksums.
- Slide count, PDF page count, guide revision and QA report references.

Reuse a matching successful build when its objects are present and verified. Repeated downloads do not generate or upload another copy. Changed inputs or a deliberate rebuild create a new version; do not overwrite the previous approved version. Define retention separately, with no automatic deletion introduced by this work.

Acceptance: an episode can be traced from its staff page to the exact guide, deck, PDF, source revision and evidence used for that version.

## Task 2 — Export and validate the PDF decks

Use a separate presentation build command or controlled production job to convert the approved PowerPoints. Preserve the existing slide branding, embedded workbook/calculator evidence and readable equations. Export slides as the deck PDF; keep staff narration and recording notes in the internal guide unless a separate notes export is explicitly selected.

Pilot one episode before processing a bounded batch. Validate file opening, slide-to-page count, readable formulas, clipping, screenshots and source links. Record failures per episode and allow targeted retries without rebuilding the successful episodes.

Acceptance: the pilot has a reviewed PowerPoint/PDF pair with checksums and matching slide/page counts; the same command supports selected episode IDs.

## Task 3 — Connect private storage and document records

Configure a private bucket backend and a dedicated upload/synchronization command. Render into temporary local storage, validate the output, then upload through the storage interface. Account for the existing renderer's filesystem assumptions rather than assuming that changing a bucket setting makes every generation path compatible.

Store file bytes in the bucket and document metadata/references in the database. Keep credentials in deployment configuration. Upload and verify both files before marking a version ready; switch the current-version reference only after the pair and associated guide are complete. A failed upload must leave the previous approved version available.

Repeated synchronization of the same verified version must be safe and skip duplicate work. Missing objects should be reported and repaired from the validated artifacts where available. Record upload state separately from build state. Introduce database migrations only as required by the final document/version models.

Acceptance: web and publishing services can use the same private artifacts without sharing a local Railway filesystem; a partial upload cannot become the current published version.

## Task 4 — Publish internal guide pages and a master index

Create a staff production index grouped by project/series and episode. Each guide page should include the episode questions, recording sequence, slide index, workbook ranges, calculator demonstrations, source dates, known evidence limitations and recording status.

Display the document identifier, current version, generation date and download links for both the PowerPoint and PDF deck. Bind the guide and downloads to the same approved version. Keep video recording, review and external publication as separate statuses; uploading a deck must not imply that a video has been released.

Import guide content through the application's supported safe rendering path. Reconcile the staff index with the research master index and retain links to source records. Flag missing or unpublished article associations instead of silently creating unrelated public articles.

Acceptance: staff can locate an episode from the master index and follow its guide, slides and sources without searching the repository.

## Task 5 — Enforce roles at pages and downloads

Map explicit presentation permissions onto the existing staff/editorial role system: view guides, download assets, and manage/publish versions. Use the least access needed for each role. Hiding navigation links is not access control.

Check authorization on every guide and download endpoint, including requests for historical versions. Keep the bucket private. Use an authenticated download proxy or short-lived signed object URLs issued only after permission checks. Do not place permanent public bucket URLs in internal guides. Record publishing actions and version changes through the existing audit approach.

Acceptance: anonymous users, ordinary members and staff without the relevant permission cannot access protected pages or obtain download links; authorized staff can access only the permitted actions.

## Task 6 — Pilot, roll out and document operations

After Tasks 1–5, publish one approved episode end to end, verify authorized and unauthorized access, repeat the upload to confirm reuse, and introduce a test revision to confirm safe version switching and rollback. Exercise a conversion failure, a partial upload and a missing stored object before batch rollout.

Roll out the remaining approved episodes in bounded batches with resumable progress. Reconcile the production index against the source manifest rather than hard-coding article counts. Document configuration, migrations, selective export/upload commands, permission assignment, failure recovery and version rollback in the platform repository.

Acceptance: every intended published episode has an accessible authorized staff guide and a verified matching PPTX/PDF pair, with no presentation jobs added to the reading-PDF worker queue.

## Implementation boundaries

This plan does not upload files, enable a bucket, create migrations, expose production pages or change membership/payment behavior. It does not modify calculators or rebuild existing reading PDFs. Implement and validate the workflow as a separate milestone; review the relevant Git diffs, prepare detailed commit messages and commit/push the corresponding changes in both repositories at that milestone.

## Source links

- [Presentation package and current delivery boundaries](<../Publishing and Video Production/Presentation Assets/README.md>)
- [Presentation master index](<../Publishing and Video Production/Presentation Assets/Master Index.md>)
- [YouTube production plan](<../Publishing and Video Production/YouTube Production Plan.md>)
- [Railway deployment and background workers](01_sokointel_railway_background_workers.md)
- [Membership, workbooks and payments](02_sokointel_membership_workbooks_payments.md)

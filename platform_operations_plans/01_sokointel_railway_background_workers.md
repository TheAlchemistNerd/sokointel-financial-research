# Sokointel on Railway: Deployment and Background Workers

## Decision

Sokointel will run on Railway. The web application, edition worker, and PostgreSQL service will be separate Railway services in one Railway project environment. ChamaBanking and OSFreelance do not share this production environment.

## Current worker

Sokointel already has a durable Django edition queue. Article and collection work is queued outside the web request. The existing production command is:

    python manage.py edition_worker --watch --recover-stale

It watches continuously, produces Word, PDF, and ZIP editions, and can recover work that has remained running for more than thirty minutes. It is therefore a persistent worker service.

## Railway service layout

| Service | Source | Start responsibility | Public access |
| --- | --- | --- | --- |
| Sokointel Web | Sokointel repository | Django web process | Yes |
| Sokointel Editions | Same repository and worker image | python manage.py edition_worker --watch --recover-stale | No |
| Sokointel PostgreSQL | Railway PostgreSQL | Durable relational state | No |
| Sokointel Cron | Same repository, only after short commands exist | Daily summary, backup check, or cleanup | No |

Create the web and edition services from the same Git revision. They use the same database, object-storage settings, and application configuration, but different start commands. Railway services in the same environment communicate privately, while Railway PostgreSQL is private by default. See [Railway private networking](https://docs.railway.com/networking/private-networking) and [Railway PostgreSQL](https://docs.railway.com/databases/postgresql).

Railway Cron is not suitable for the edition worker. A cron job must finish and exit. Railway can skip the next schedule if an earlier run remains active. Cron schedules use UTC and cannot run more frequently than every five minutes. Use cron only for a terminating management command. See [Railway Cron Jobs](https://docs.railway.com/cron-jobs).

## Required storage change

The current generator reads and attaches private files. Railway web and worker services have different ephemeral filesystems. A file written by the worker cannot safely be expected to exist in the web process.

Before separating the worker, move private editions and uploads to S3-compatible object storage. Store a storage key, original filename, content type, byte size, SHA-256 checksum, source snapshot identifier, created time, and retention state. The worker uploads the final file, verifies the checksum, updates the database, then marks the job successful. The web application checks entitlement before returning a time-limited private download.

Do not use a public bucket or a predictable URL as access control.

## Worker image

PDF generation uses LibreOffice through soffice. Build a dedicated worker Docker image with LibreOffice Writer, required fonts, a configured soffice path, and a non-root process. Test the same image in CI. Start with one concurrent edition job. Increase concurrency only after measuring an individual article, a full collection PDF, and a ZIP build.

The web service may use a smaller image if it never generates editions.

## Release procedure

1. Create Railway staging and production environments.
2. Add a private Railway PostgreSQL service to each.
3. Provision private object storage and scope credentials to the required prefix.
4. Deploy the web service and run migrations as an explicit release step.
5. Deploy the edition worker from the exact same Git revision.
6. Queue one article edition and one collection edition.
7. Confirm database state, checksum, protected download, and member entitlement.
8. Restart the worker and prove stale-job recovery does not duplicate output.
9. Send a controlled Postmark message.
10. Enable public traffic after backup and restore checks pass.

## Health and operations

| Signal | Alert | First response |
| --- | --- | --- |
| Worker heartbeat | Missing for ten minutes | Inspect logs and redeploy worker |
| Queued editions | Oldest queued job exceeds publishing window | Inspect worker and review before retry |
| Failed edition | Any new failure after release | Preserve state and inspect redacted error |
| Running edition | More than thirty minutes | Allow recovery, then investigate cause |
| Object output | Missing object or checksum | Block download and mark failure |
| Database backup | Backup or restore test fails | Pause risky releases |

The worker has no public domain. Keep staging and production credentials separate. Do not log documents, payment secrets, or private article content. Verified provider webhooks, not browser redirects, grant paid access.

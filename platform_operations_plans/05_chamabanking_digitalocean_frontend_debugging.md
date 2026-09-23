# ChamaBanking: DigitalOcean Pilot and Frontend Debugging

## Starting position

The frontend-export directory is an architecture starter kit, not a runnable application. It has no package manifest, web source, mobile source, lockfile, test harness, or build pipeline. Create a dedicated chamabanking-frontend repository.

The backend is a Spring Boot modular monolith with PostgreSQL, Flyway, Firebase authentication, OpenAPI, group workflows, financial records, audit endpoints, notifications, and payment integrations. The generated OpenAPI document and running non-production backend are the source of truth over prose specifications.

## DigitalOcean environments

| Environment | Application | Database | Purpose |
| --- | --- | --- | ---|
| Local | Spring Boot test profile | Disposable Postgres | Development and contract checks |
| Staging | DigitalOcean staging Droplet | Separate staging database | Integration and sandbox tests |
| Pilot | DigitalOcean app environment | Dedicated Managed PostgreSQL preferred | Closed non-custodial pilot |
| Production later | Separate scalable services | Managed PostgreSQL with tested recovery | After security and operational gates pass |

Do not expose PostgreSQL publicly. Use a firewall, SSH keys, TLS proxy, private database networking, monitoring, encrypted backups, and two administrators. Build versioned images in CI and deploy the exact image. Do not compile Java on the production Droplet.

## Frontend delivery

| Phase | Deliverable | Evidence |
| --- | --- | --- |
| Contract baseline | Run backend in non-production and capture OpenAPI | Reproducible command and versioned contract |
| Foundation | Create Turborepo with web, mobile, API, types, UI, config, and utilities | Clean install, lint, typecheck, tests, and build |
| Typed client | Generate types from real OpenAPI and configure runtime client | Contract tests and compile-time checks |
| Auth and tenancy | Firebase development auth, refresh, logout, group selection, tenant context | Tests prove group isolation |
| Safe loop | Profile, groups, members, manual records, approvals, audit, export | One full cycle without payment automation |
| Quality | Loading, errors, offline, accessibility, responsive tests, monitoring | Browser and accessibility evidence |
| Integrations | Payment, KYC, uploads, notifications, then mobile | End-to-end sandbox evidence |

Sprint one is web only: shell, Firebase development setup, runtime configuration, generated types, API client, login state, group switcher, error page, read-only group dashboard, and browser tests.

Sprint two creates the first safe loop: create or select a group, add or view members, record a manual contribution, submit it for approval, inspect audit history, and export a record. Mobile follows after web validates terminology, roles, failures, and tenant behaviour.

## Financial gate

Before automated contributions, payouts, loans, dividends, billing, or payment callbacks, prove role and group authorisation, client and webhook idempotency, provider signature verification, ledger reconciliation, reversal and dispute workflow, audit events for every state change, currency and time-zone handling, backup restore, and support procedures.

A payment request accepted by a provider is not proof that money settled or that records reconciled. The pilot promise is group visibility and governance, not custody of member funds.

# Database Boundaries: Railway, DigitalOcean and Local Development

## Decision

Use product-specific production database services.

- Sokointel uses private Railway PostgreSQL within Railway.
- ChamaBanking uses a dedicated DigitalOcean PostgreSQL service before it handles sensitive group records.
- OSFreelance uses its own database cluster or service when it leaves local development.
- Local development may use one PostgreSQL server with separate databases and roles.

Do not create a shared cross-cloud production database between Railway and DigitalOcean. It adds public-network dependence, latency, recovery complexity, and a broader failure domain.

## Local development

| Boundary | Database |
| --- | --- |
| Sokointel | sokointel_dev |
| OSFreelance Identity | osfreelance_identity_dev |
| OSFreelance DealFlow | osfreelance_dealflow_dev |
| OSFreelance Growth | osfreelance_growth_dev |
| OSFreelance LeadTools | osfreelance_leadtools_dev |
| ChamaBanking | chamabanking_dev |

ChamaBanking can use tenant schemas inside its own database. Do not put tenant schemas inside Sokointel or OSFreelance databases. Redis remains separate from PostgreSQL. Local Redis can be shared only with product-specific namespaces, credentials, and expiry rules.

## Production

| Product | Compute | Database | Network |
| --- | --- | --- | --- |
| Sokointel | Railway web and editions worker | Railway PostgreSQL | Railway private network |
| ChamaBanking | DigitalOcean application services | DigitalOcean Managed PostgreSQL preferred | DigitalOcean VPC or private network |
| OSFreelance | Separate pilot project | Dedicated Postgres and Redis | Private project network |

Railway PostgreSQL is private by default. Railway services in one environment use private service networking. Avoid a public database proxy except for a defined temporary administrator need. See [Railway PostgreSQL](https://docs.railway.com/databases/postgresql) and [Railway private networking](https://docs.railway.com/networking/private-networking).

For ChamaBanking, a self-managed PostgreSQL container on the same Droplet is acceptable for development or a short demo, but not preferred for a real pilot. It shares the application machine, backup burden, and failure domain. Managed PostgreSQL is the better boundary for sensitive group data.

## Roles

| Role | Permission |
| --- | --- |
| Migration owner | Schema change and controlled maintenance |
| Runtime application | Required operations within one database |
| Backup operator | Backup capability without normal app login |
| Human administrator | Time-bound administrative access with an audit trail |

No runtime role should be a superuser, create arbitrary databases, or connect to another product's database. Keep production, staging, and development credentials separate.

## Controls

1. Keep databases private.
2. Limit application and worker connection pools.
3. Run migrations as a named release operation.
4. Take encrypted logical backups daily and before schema changes.
5. Restore each database into a disposable environment at least monthly.
6. Monitor storage, connection use, long-running queries, backup status, and restoration time.
7. Rotate credentials and revoke unused access.

A shared development service saves money. A shared production service couples outages, maintenance, credentials, storage pressure, and recovery. Sokointel research, OSFreelance documents, and ChamaBanking financial records need different security and availability boundaries.

# Cross-product agentic operations, audit and billing architecture

**Status:** Operating design and release-gate record  
**Updated:** 2026-09-13

## Purpose

Sokointel and Freelancer handle different work, yet need the same operating discipline. Each system must accept work through an authenticated or verified ingress, preserve the request, run bounded background work, obtain the necessary approval, apply the approved result once, and retain a safe audit history.

The intended experience is agentic in the useful sense. A user asks the system to perform a bounded task, the system plans and executes authorised steps with narrow tools, shows evidence and result, and waits for a human when the decision has editorial, financial, legal, or customer impact. It does not autonomously publish, charge, or control an external account.

## Common work-item contract

Every ingress creates a durable WorkItem before a worker acts. A work item has a stable ID, tenant or project scope, initiating actor or provider, input snapshot hash, idempotency key, task type, permitted tools, state, attempt count, and timestamps. Private inputs and outputs remain in private storage. The audit entry keeps references and hashes, never manuscripts, keys, cards, or provider payloads.

| Stage | Required control |
| --- | --- |
| Ingress | Authenticate staff or members, verify provider signatures, validate schema, capture consent, and enforce idempotency. |
| Planning | Select registered tools only, identify the input versions, and state whether approval is required. |
| Queueing | Write the work item and audit event in the durable database before asynchronous processing. |
| Execution | Claim with a lease and fencing token. A stale worker cannot overwrite a later result. |
| Review | Show result, source versions, model provenance where relevant, warnings, and a diff. |
| Side effect | Publish, attach, synchronise, notify, or reconcile once after the required approval. |
| Recovery | Retry documented transient errors, preserve the same work-item ID, dead-letter exhausted failures, and retain an authorised replay path. |

The states are received, validated, queued, claimed, running, awaiting_review, approved, completed, retry_scheduled, failed, dead_letter, cancelled, and superseded. Human review is mandatory for publication, entitlement, pricing, contract content, refund decisions, credential changes, permission changes, and unbounded external actions.

## AI ingress and handoff

The shared agentic handoff has five roles:

1. The gateway validates identity, consent, scope, task schema, and rate limit.
2. The planner creates a structured plan using registered tools only.
3. The specialist worker creates a bounded result such as a draft, edition, source manifest, payment decision, delivery record, or synchronisation proposal.
4. The reviewer accepts, edits, rejects, or requests another attempt where policy requires it.
5. The executor performs the approved side effect idempotently and records the provider reference or artifact digest.

Models may propose work and operate on explicitly selected materials. They cannot browse arbitrary locations, access credentials, publish, charge, alter access, change permissions, or write to an external system without an approved narrow action. Tool calls, selected source versions, model/provider, token usage when supplied, output hash, and approval identity become audit events.

## Reuse and versioning

Templates, source ledgers, workbooks, prompts, video episode templates, Notion mappings, and document components have stable records and versions. A new work item snapshots the exact version it uses. Editors can fork a reusable item into a new version, while a published article, sent document, or completed payment preserves the version that produced it. This enables correction, replay, and attribution without overwriting history.

## Notion and external knowledge tools

Notion must be a selected, consented workspace connection rather than a server-wide outbound mirror. A tenant administrator connects through OAuth, chooses accessible pages or databases, and selects read, proposed-write, or approved two-way mode. Tokens are encrypted or placed in the secret manager and never sent to an AI provider.

Inbound Notion webhooks create work items. A worker retrieves the selected page, compares its revision with the local snapshot, and proposes a merge or creates a conflict for review. Outbound updates use the same workflow. A mapping records local object, Notion page, connection, field allowlist, source version, external revision, and last successful synchronisation. Direct overwrites, global tokens, and unreviewed two-way synchronisation are prohibited.

## Audit requirements

The audit log records actions, not document bodies. Every event carries:

| Area | Minimum evidence |
| --- | --- |
| Identity and scope | Event and correlation IDs, tenant or project, actor type and ID, role, target and version. |
| Decision | Action, outcome, reason code, policy version, approver, and approval time. |
| Evidence | Allowed before/after fields, input/output hashes, artifacts, and external references. |
| AI | Provider, model, prompt/template version, selected sources, usage counters, result hash, and review decision. |
| Payments | Provider event and transaction references, price snapshot, reconciliation result, and entitlement decision. |
| Security | Request metadata, validated IP where lawful, credential rotation, and redacted failure code. |

Application code and normal staff cannot edit or delete audit rows. Database permissions, backups, and retention jobs preserve that rule. Audit viewers are tenant-scoped and role-gated. The record excludes credentials, access tokens, raw payment bodies, full manuscripts, prompt bodies, and unredacted personal data.

## Payment architecture

Hosted checkout is the default. The application creates a pending transaction from an active, versioned price record. The provider owns card or payment-method entry. A browser return can show status but never grants access.

1. The customer selects a server-owned plan and active market price.
2. The server writes a pending transaction with a price snapshot and idempotency key, then creates a hosted checkout.
3. The provider sends a signed webhook. The endpoint authenticates it, stores a unique durable inbox event, and acknowledges promptly.
4. A reconciliation worker retrieves authoritative provider state, compares local reference, amount, currency, and paid status, then changes entitlement once in one database transaction.
5. The worker writes audit and notification work items. It retries transient failures, dead-letters exhausted failures, and supports an authorised replay.
6. Refunds, disputes, chargebacks, cancellation, and reactivation are separate policy events. They never silently create or erase access.

Paystack requires server-side verification and warns against double fulfilment of digital value [1]. Its webhooks require signature verification and prompt acknowledgement [2]. Stripe Checkout and signed webhook guidance support the equivalent pattern [3], [4].

## Postmark and notification events

Postmark is the transactional email provider for Sokointel and may be used by Freelancer through SMTP or its API. Each message has a local notification record, template/version, recipient hash, send attempt, provider message ID, and delivery state. Delivery, bounce, complaint, suppression, and inbound-reply callbacks enter the same durable inbox pattern, update contact state, and create audit events. Postmark supports transactional SMTP message streams and operational webhooks [5], [6].

## Product-specific runbooks

- Sokointel: C:\Users\Nevo\Downloads\business and technical website blog\docs\agentic_operations_audit_payments.md
- Freelancer: C:\Users\Nevo\Documents\Projects\Personal Projects\ai systems\freelancer\docs\internal\agentic_operations_audit_billing.md

## Release gates

1. Exercise every worker against disposable PostgreSQL, including duplicate delivery, lease expiry, crash recovery, and manual replay.
2. Complete controlled sandbox payments for every enabled provider and prove one entitlement change only.
3. Route every active provider callback into a durable inbox rather than a slow network call or direct access change.
4. Prove audit entries are role-gated, tenant-scoped, append-only, redacted, and recoverable from backup.
5. Run model smoke tests with synthetic content and an explicit billable-test acknowledgement.
6. Keep Notion disabled until OAuth, selected scopes, inbound event verification, conflict handling, replay, and revocation are tested.

## References

[1] Paystack, “Verify Payments.” Available: https://paystack.com/docs/payments/verify-payments/

[2] Paystack, “Webhooks.” Available: https://paystack.com/docs/payments/webhooks/

[3] Stripe, “Checkout.” Available: https://docs.stripe.com/payments/checkout

[4] Stripe, “Webhooks.” Available: https://docs.stripe.com/webhooks

[5] Postmark, “Sending email with SMTP.” Available: https://postmarkapp.com/developer/user-guide/send-email-with-smtp

[6] Postmark, “Webhooks overview.” Available: https://postmarkapp.com/developer/webhooks/webhooks-overview

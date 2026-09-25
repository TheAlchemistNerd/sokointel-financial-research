# Membership and free tools delivery status

25 September 2026. Companion record for the platform membership milestone. This file distinguishes implemented code from live configuration and the separate calculator roadmap.

## Public membership implementation

The SokoIntel platform now has public signup, email verification and password recovery. New accounts remain inactive until a time-limited email link is confirmed. Checkout requires the account's current email to be verified. Account creation, password recovery and browser checkout return do not themselves grant paid downloads; only provider-confirmed payment does. Existing article and calculator access remains free. Existing paid entitlements are preserved.

Payment handling now binds the event to its provider/reference and checks amount/currency and the corresponding provider session or verified reference. Payment and account row locks serialize entitlement updates on PostgreSQL; the same payment cannot extend membership twice through separate sequential events. A webhook arriving before checkout initialization returns is not overwritten as pending. Future-dated prices cannot be purchased. Offers explain the one-time access period and manual renewal.

The supplied Google Search Console HTML file is served by an exact public Django route at `https://sokointel.com/google19802db332d92854.html`. Search Console verification remains a separate post-deployment step.

## Validation and deployment boundary

The targeted platform suite passed 51 tests: public accounts, payment flows, membership pricing/access, public calculators and time-value calculations. Verification expiry/replay, changed-address rejection, resend replacement, CSRF, password-reset completion and duplicate payment events are included. Email was captured in memory and payment calls mocked. A follow-up throttle regression passed after ensuring an IP cap stops further per-address counter allocation. Migration drift and Django system checks passed. Local browser checks showed signup/recovery pages and the exact unwrapped Google verification text.

This is not proof of Railway deployment, real SMTP delivery, provider sandbox/live acceptance, PostgreSQL concurrent delivery or shared private-storage access. The two new migrations must be applied. Public signup and live payments remain feature-gated. No production secret was read or changed and no real payment or outbound email was sent.

The canonical operator instructions are in the platform repository:

- `docs/Public Membership Railway Setup.md`
- `docs/Membership Launch Readiness 2026-09-25.md`

Configure email and the selected payment provider on the web service. Document-generation workers do not need payment keys or public signup enabled; account emails use the web service and do not create document jobs.

## Free calculator work continues separately

The [Free calculator development roadmap](<Free Calculator Development Roadmap.md>) remains the accepted scope. Detailed business-credit, MSME owner-cash, thirteen-week liquidity and failure-warning tools are not claimed as delivered by this membership milestone. DCF remains available for additive improvements. Preserve the single-asset DCA, portfolio DCA and compounding/cash-flow families; their source and templates were not edited by this milestone. Each new tool must reconcile to the named workbook examples and define formula symbols beside the calculations.

The bulk branded-PDF and episode-presentation rollout remains deferred following the user's pivot to membership and calculators. The previously supplied sample branded PDF is not a claim that every library edition has been regenerated.

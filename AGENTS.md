# Owner policy supersession — effective 2026-11-18

**OWNER-REVIEW-OPTIONAL-2026-11-18:** An independent human code reviewer, reviewer assignment, and a separate reviewer approval are **NOT mandatory** for implementation, PR merge or software deployment. The project agent/authorized maintainer must conduct direct technical review and complete the applicable tests, security/privacy checks, exact-SHA build, release evidence and rollback verification. An independent peer review is optional if expressly wanted, never a standing blocker.

This supersedes *only* older mandatory independent code-review rules anywhere below or elsewhere in this repository. It does **not** waive legal/regulatory/institutional approvals, signed exam/trading authority, security boundaries, CI/testing requirements, existing GitHub protected-branch controls, or approved project acceptance criteria. Do not fake reviews, bypass protected rules or call incomplete tests passed. Continue source/provenance accounting and ship qualified features promptly.

Canonical portfolio policy: https://github.com/galapoto/Projects/blob/main/docs/governance/OWNER_REVIEW_OPTIONAL_2026_11_18.md

---

# Repository agent instructions

This is an **educational/portfolio analysis repository**, not an enrolled production service. Preserve the existing README, course-evidence caveats, source/data attribution, reproducible tests, and any stricter local requirements. Never represent course work, synthetic data, or unverified hosted assets as a production release.

## FEATURE-FIRST-001 — reference, not deployment authorization

Follow the owner-managed [canonical FEATURE-FIRST-001 standard](https://github.com/obumai/obum-delivery/blob/main/docs/FEATURE_FIRST_001_STANDARD.md) and [future-repository bootstrap guide](https://github.com/obumai/obum-delivery/blob/main/docs/FEATURE_FIRST_NEW_REPO_BOOTSTRAP.md), subject to stricter repository security, privacy, licensing, evidence-integrity, and approval requirements. For portfolio analysis, the verifiable user outcome is reproducible analysis and an honestly labelled report; do not invent a production app, ObumAI launcher tile, or `USER_VERIFIED` release.

**Disabled-by-default feature-contract onboarding:** If the owner later approves a deployable product feature, propose a separate scoped PR using the [canonical feature-contract template](https://github.com/obumai/obum-delivery/blob/main/templates/FEATURE_FIRST_001_FEATURE_CONTRACT.yaml) under `docs/features/<feature-id>.yaml`. Set `activation.default: false`; document owner, real user outcome, target/adapter, risk, authorization, tests, recovery, and deployment evidence. The contract is a proposal only; do not enroll a delivery target, activate a flag, provision credentials, change CI secrets, grant production permissions, or enable deployment without separate scope-specific approval and commissioned checks.

## LEAN-REA-FLOW-001 — safe reuse and evidence

Apply the [lean reuse/UX/run-evidence standard](https://github.com/obumai/obum-delivery/blob/main/docs/LEAN_REA_FLOW_001_STANDARD.md) and [per-run receipt](https://github.com/obumai/obum-delivery/blob/main/templates/LEAN_REA_FLOW_001_RUN_RECEIPT.md). Inspect this repository and authorized, compatible upstream code first. Identify donor URLs, pinned revisions, source files, licenses, sanitization/adaptation, tests, and missing pieces; write **"Copied: none"** when appropriate. Clearly separate policy presence, source/test qualification, commissioned automatic delivery, and actual user verification. Do not claim an independent review occurred unless recorded; preserve applicable protected approvals and never modify externally governed repositories.

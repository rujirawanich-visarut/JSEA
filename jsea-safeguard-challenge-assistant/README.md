# JSEA Safeguard Challenge Assistant

Package 2B for AI-assisted Job Safety and Environmental Analysis (JSEA) — Process Safety Information (PSI) Integrated

---

## Overview

`jsea-safeguard-challenge-assistant` is a human-led decision support package that rigorously tests whether proposed JSEA safeguards are relevant, layered, independent, evidenced, and ready for competent-person field verification.

For tasks involving chemical or petrochemical process boundaries, this package applies a **PSI Gate Pre-Check** before challenging safeguard adequacy, ensuring that physical isolations, relief pathways, and safety instrumented functions (SIS) are verified against engineering source documents.

---

## Package Structure (v1.4.0)

```text
jsea-safeguard-challenge-assistant/
├── README.md
├── SKILL.md                                              # Primary skill definition (v1.4.0)
├── references/
│   ├── hierarchy-of-controls-patterns.yaml               # Hierarchy challenge patterns (HOC-01 to HOC-05)
│   ├── safeguard-dependency-patterns.yaml                # Dependency & common-cause patterns (DEP-01 to DEP-12)
│   ├── process-isolation-adequacy-patterns.yaml         # 6-tier isolation hierarchy & line-breaking challenge patterns
│   ├── process-safeguard-challenge-extension.yaml       # 10 domain-specific process safeguard patterns (PSCE-01 to PSCE-10)
│   ├── environmental-emergency-challenge-patterns.yaml  # Large LOPC, bund capacity, & firewater runoff patterns (ENV-EM-01 to ENV-EM-05)
│   ├── evidence-and-field-verification.yaml             # 7 verification classes & evidence classification
│   ├── unified-evidence-label-schema.yaml                # Shared evidence discipline schema
│   ├── jsea-output-behavior-contract.yaml                # Shared field/management/technical/audit output profiles
│   ├── process-safety-information-retrieval-map.yaml     # Shared 3-Pillar PSI retrieval map
│   ├── stop-and-escalate-decision-rules.yaml             # Shared STOP_AND_ESCALATE conditions (SES-01 to SES-11)
│   ├── competent-role-routing-matrix.yaml                # Shared role routing per hazard domain
│   ├── re-jsea-trigger-catalog.yaml                      # Shared 16 re-JSEA / work-suspension triggers
│   └── source-register.yaml                             # 5-Tier authoritative source hierarchy
└── evals/
    ├── safeguard-challenge-cases.json                    # General occupational safeguard cases (8 cases)
    ├── process-safeguard-red-team-cases.json            # Adversarial process safeguard red-team cases (16 cases)
    └── field-safeguard-output-cases.json                # Field communication behavior cases (7 cases)
```

Version 1.4.0 also declares the four shared `physics-causal-*.yaml` references.
They require every safeguard to be challenged against a named causal edge and
preserve uncertain mechanism claims as evidence needs rather than conclusions.

---

## Non-Negotiable Safety Boundaries

This package does **not** approve work, issue permits, declare a job safe, replace site walkdowns, interpret live process gauges, specify engineering relief setpoints, or authorize work start/continuation.

### Permitted Workflow Dispositions

The AI output must culminate in exactly one of three permitted workflow dispositions:

1. `READY_FOR_HUMAN_FIELD_REVIEW`: All proposed safeguards are mapped, layered, independent, and documented with clear field verification questions for authorized site roles.
2. `ADDITIONAL_EVIDENCE_REQUIRED`: Material evidence gaps, unverified bypasses, or missing P&IDs/isolation procedures must be provided before review can conclude.
3. `CRITICAL_CONCERN_ESCALATE`: A critical safeguard failure mode, unisolated toxic/high-pressure stream, or blocked relief path requires formal escalation to site authorities.

> **No output from this package is equivalent to work authorization.**

---

## Core Challenge Dimensions

1. **Safeguard-to-Hazard Linkage:** Verifies that each control addresses the specific energy release mechanism, not just a generic activity.
2. **Hierarchy of Controls Challenge:** Prohibits treating PPE or administrative rules ("be careful", "follow procedure") as sole barriers for Loss of Primary Containment (LOPC).
3. **Isolation Adequacy Challenge:** Enforces the 6-tier isolation hierarchy (Positive Blinding > DBB > Double Valve > Single Valve > Check Valve prohibited).
4. **Dependency & Common-Cause Analysis:** Surfaces hidden dependencies on shared sensors, single power supplies, common root taps, instrument air, and human memory.
5. **Environmental Emergency & Containment:** Challenges secondary bund volume (110% rule), storm drain isolation valve status, and firewater runoff diversion.
6. **Field-Verification Specification:** Defines exact physical checks, witness points, and competent roles required before work begins.
7. **Audience-Aware Output:** Translates safeguard findings into plain-Thai field rows, management decisions, technical reviews, or audit traces while preserving the same safety disposition.
8. **Physics-Causal Edge Challenge:** Classifies whether a control prevents initiation, inhibits a mechanism, detects a state change, mitigates consequence, or supports recovery.

---

## Activation Preamble (v1.4.0)

```text
Activate JSEA Safeguard Challenge Assistant (v1.4.0).

Read SKILL.md as the primary instruction and read all reference files in references/.
Treat files mirrored from `../shared-references/` as the canonical shared rule set.
Read all evaluation files declared in SKILL.md as behavioral benchmarks.

This session is for challenging proposed safeguards and preparing evidence requirements for competent-person field verification. It is not for issuing a permit, approving work, or declaring a job safe.

Before analyzing, confirm:
1. Package version (v1.4.0) and files successfully read.
2. Scope and prohibited AI actions (HUMAN_ONLY_DECISION).
3. PSI Gate status: Missing chemical identity, operating envelope, or P&ID data flagged as EVIDENCE_GAP (CRITICAL).
4. Label discipline: Tag items as FACT, REFERENCE, AI_HYPOTHESIS, EVIDENCE_GAP, or HUMAN_ONLY_DECISION.
5. Provide a structured safeguard challenge matrix, dependency analysis, and one permitted workflow disposition.
6. Use FIELD_JSA by default and apply the audience-specific output contract.
```

---

## Governance and Maintenance

- **Primary Owner:** Process Safety Lead / Operations Superintendent / PTW Administrator
- **Review Frequency:** Annual + after any turnaround or near-miss revealing safeguard dependency
- **Current Version:** `1.4.0` (Updated 2026-08-16)
- **PICR Release Boundary:** Wave 1 is `DRAFT` pending repeated live-model semantic evaluation and named domain-owner review.

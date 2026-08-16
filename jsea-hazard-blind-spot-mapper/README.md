# JSEA Hazard Blind-Spot Mapper

Package 1B for AI-assisted Job Safety and Environmental Analysis (JSEA) — Process Safety Information (PSI) Integrated

---

## Overview

`jsea-hazard-blind-spot-mapper` helps a work team scan task steps for occupational hazards, energy sources, chemical process boundaries, environmental aspect-impact pathways, and interface blind spots before work begins or when conditions change.

For tasks involving chemical or petrochemical process boundaries (piping, pressure vessels, pumps, tanks, relief systems), this package applies a mandatory **Process Safety Information (PSI) Gate** before analysis proceeds.

It is a **hazard-discovery decision support package**, not a work-authorization system. It does not approve permits, confirm field isolation or atmospheric conditions, assign a Final Risk Rating, prescribe site-specific controls, or declare work safe.

---

## Package Structure (v1.4.0)

```text
jsea-hazard-blind-spot-mapper/
├── README.md
├── SKILL.md                                        # Primary skill definition (v1.4.0)
├── references/
│   ├── hazard-energy-catalog.yaml                  # 18 hazard/energy discovery families (HE-01 to HE-18)
│   ├── environmental-aspect-pathways.yaml          # Environmental aspect-impact pathways
│   ├── process-boundary-hazard-lens.yaml           # Process-specific failure modes (flange break, CUI, cryogenic, etc.)
│   ├── psi-gap-detection-prompts.yaml              # Diagnostic prompts across 3 PSI pillars
│   ├── process-safety-information-retrieval-map.yaml # 3-Pillar PSI retrieval map & mandatory verification
│   ├── chemical-hazard-evidence-map.yaml           # Chemical mixture, phase behavior, & reactivity evidence
│   ├── process-condition-verification-schema.yaml  # Zero-energy state, depressurization, & drain criteria
│   ├── job-type-retrieval-decision-tree.yaml       # Per-job-type document retrieval guidance
│   ├── stop-and-escalate-decision-rules.yaml       # Mandatory STOP_AND_ESCALATE conditions (SES-01 to SES-11)
│   ├── competent-role-routing-matrix.yaml          # Role routing per hazard domain
│   ├── regulatory-source-register.yaml             # Thailand DIW/IEAT & international regulatory register
│   ├── re-jsea-trigger-catalog.yaml                # 16 conditions requiring re-JSEA / work suspension
│   ├── unified-evidence-label-schema.yaml          # Shared evidence discipline schema
│   ├── jsea-output-behavior-contract.yaml          # Shared field/management/technical/audit output profiles
│   ├── jsea-source-register.yaml                   # 5-Tier authoritative source hierarchy
│   └── enterprise-risk-crosswalk.yaml              # Indicative secondary enterprise risk crosswalk
└── evals/
    ├── hazard-mapping-cases.json                   # General occupational evaluation cases (14 cases)
    ├── chemical-process-blind-spot-cases.json      # Adversarial PSI/chemical process cases (16 cases)
    └── field-jsa-output-cases.json                 # Field communication behavior cases (7 cases)
```

Version 1.4.0 also declares the four shared `physics-causal-*.yaml` references
and `evals/physics-causal-reasoning-cases.json` (30 cases) in `SKILL.md`.

---

## What the Package Does

- **Sequential Task Decomposition:** Structures a job from planning and mobilization through task execution, housekeeping, de-isolation, and handback.
- **PSI Gate Enforcement (Step 2.5):** Verifies the 3 pillars of Process Safety Information (Materials, Technology, Equipment) before analyzing process boundary tasks.
- **Physics-Informed Causal Gate (Step 2.6):** Matches mechanisms by preconditions, builds causal chains, tests disconfirming evidence, and routes unsupported calculations or decisions to competent roles.
- **Hazard & Energy Scanning:** Scans 18 energy families (mechanical, thermal, pressure, chemical, biological, radiation, human factors, SIMOPS, etc.).
- **Process Boundary Deep-Lenses:** Evaluates auto-refrigeration, pyrophoric FeS, trapped pressure, flange spray, and small-bore connection fatigue.
- **Environmental Pathway Modeling:** Maps `Activity -> Aspect -> Release -> Pathway -> Receptor -> Impact`.
- **Evidence Label Discipline:** Tags every finding as `FACT`, `REFERENCE`, `AI_HYPOTHESIS`, `EVIDENCE_GAP`, or `HUMAN_ONLY_DECISION`.
- **Field Verification Questions:** Produces specific, testable questions for workers and supervisors at the workface.
- **Audience-Aware Output:** Defaults to a plain-Thai four-column FIELD_JSA and supports MANAGEMENT, TECHNICAL_REVIEW, and AUDIT_EVAL profiles without weakening safety rules.

---

## Safety Boundaries & Prohibited AI Behaviors

The AI **MUST NOT**:
- Approve a JSEA, Permit to Work, isolation certificate, or confined space entry.
- Declare that a job is "safe to proceed" or that conditions are "acceptable."
- Calculate or assign a Final Risk Rating / Residual Risk Score.
- Assume unverified chemical contents are "water" or "non-hazardous."
- Accept Double Block and Bleed (DBB) or check valves as positive isolation for IDLH-toxic / high-pressure service.
- Waive safety verification steps due to production pressure, cost of downtime, or historical experience ("done this for years").

---

## Screening Review Priorities

- `CRITICAL_REVIEW`: Potential for fatality, serious injury, major LOPC, or severe environmental impact; requires competent-person verification.
- `HIGH_REVIEW`: Plausible serious exposure or significant environmental pathway.
- `STANDARD_REVIEW`: Material hazard manageable through approved site procedures and field verification.
- `WATCH`: Emerging condition or weak signal.
- `STOP_AND_ESCALATE`: Imminent danger, unknown chemical identity, blocked relief, bypassed SIS, or critical PSI gap (triggers SES rules).

---

## Activation Preamble (v1.4.0)

Attach all files in the package and submit:

```text
⟡🛠️⟡ Activate JSEA Hazard Blind-Spot Mapper (v1.4.0)

Read SKILL.md and all references in references/ before beginning.
Treat files mirrored from `../shared-references/` as the canonical shared rule set.
This session is for hazard and environmental blind-spot discovery decision support only.

Safety boundaries:
- Do not approve work, permits, isolation, entry, or work readiness.
- Do not provide a Final Risk Rating or declare the task safe.
- Apply the PSI Gate for any process boundary task before hazard mapping.
- Tag statements as FACT, REFERENCE, AI_HYPOTHESIS, EVIDENCE_GAP, or HUMAN_ONLY_DECISION.
- Use STOP_AND_ESCALATE for critical unknowns or imminent danger per SES rules.
- Require worker participation, field verification, and competent-person review.
- Use FIELD_JSA by default; use another output profile only when the audience or request requires it.

Before mapping, respond only with:
1. Skill name and version (v1.4.0)
2. References successfully read
3. Job scope framed and boundaries identified
4. PSI Gate status: Chemical identity, operating conditions, and P&ID status (Complete / Gaps)
5. Safety boundary and Stop-Work escalation statement
```

---

## Governance and Maintenance

- **Primary Owner:** Process Safety Lead / SSHE Manager
- **Review Cycle:** Annual + after any MOC affecting process boundaries or incident investigation learning
- **Current Version:** `1.4.0` (Updated 2026-08-16)
- **PICR Release Boundary:** Wave 1 is `DRAFT` pending repeated live-model semantic evaluation and named domain-owner review.

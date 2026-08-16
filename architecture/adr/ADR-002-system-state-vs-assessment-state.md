# ADR-002: Separate System State from Assessment State

Status: `DRAFT_NOT_LOADED`  
Date: 2026-08-16  
Decision owner: JSEA architecture governance

## Context

The Phase 2 research correctly says that actual plant state is different from
what JSEA knows, but one proposed object places evidence state inside a parent
System Safety State. That structure can make an instrument reading or document
look like physical reality.

## Decision

Use separate candidate objects:

- `SystemStateSnapshot`: assertions about the physical and sociotechnical system.
- `ObservedState`: measurements, records and reports with provenance and time.
- `AssessmentState`: support, contradiction, conflict and unresolved evidence.

Relationships such as `SUPPORTS`, `CONTRADICTS` and `UNVERIFIED` connect them.

## Consequences

Conflicting P&ID, field and instrument information can coexist without choosing
a false golden source. Evidence updates can change an assessment without
silently rewriting the asserted historical state.

## Guardrails

- Unknown is not converted to false, safe or negligible.
- A display or document is never privileged solely by format.
- Only authorized site processes reconcile safety-significant conflicts.

## Promotion Criteria

Conflict and stale-evidence evals must pass, including preservation of history.
Source claim: `SBD-CLM-006`.


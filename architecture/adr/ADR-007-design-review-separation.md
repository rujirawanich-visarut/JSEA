# ADR-007: Separate Design Review from FIELD_JSA

Status: `DRAFT_NOT_LOADED`  
Date: 2026-08-16  
Decision owner: JSEA product and safety governance

## Context

Inherently safer design is valuable throughout the process lifecycle, but a full
alternative-design comparison needs different inputs, reviewers and acceptance
criteria from a field JSA. Adding it wholesale to FIELD_JSA would increase
output volume and may blur work planning with engineering design acceptance.

## Decision

FIELD_JSA may ask whether a source hazard can be eliminated or reduced and may
raise a design-review opportunity. Multidimensional lifecycle comparison,
risk-transfer analysis and alternative selection belong to a separately
qualified future `DESIGN_REVIEW` capability.

## Consequences

Field communication stays action-oriented. Design work can retain alternatives,
affected hazards, populations, lifecycle stages and transferred risks without a
universal score.

## Guardrails

- No aggregate safety score.
- No design acceptance or MOC approval by JSEA.
- No change to current FIELD_JSA sections or columns in this Quick Win batch.

## Promotion Criteria

The future capability requires independent evals, domain-owner review and an
explicit output contract. Source claims: `SBD-CLM-001` through `SBD-CLM-004`.


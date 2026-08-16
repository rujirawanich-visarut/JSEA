# ADR-001: Typed Graph as Master Representation

Status: `DRAFT_NOT_LOADED`  
Date: 2026-08-16  
Decision owner: JSEA architecture governance

## Context

Linear hazard chains are readable but cannot reliably preserve branching,
feedback, shared dependencies or safeguards that create secondary pathways.
Method-specific tables also tend to duplicate facts with different meanings.

## Decision

The next architecture will treat a typed causal graph as the candidate master
representation. JSA tables, causal chains, Bowtie-like views and specialist
packages will be projections from that graph. This is a project synthesis, not
a claim that one graph replaces HAZOP, LOPA, STPA or engineering models.

## Consequences

- Every edge must name its mechanism, state preconditions and evidence status.
- Branches, loops and shared dependencies can remain explicit.
- Rendering rules must keep field output smaller than the analysis object.
- Graph size and false-completeness risk require qualification.

## Guardrails

- No claim of complete hazard coverage.
- No automatic risk, frequency or barrier credit from graph structure.
- No runtime change until a separate schema and migration ADR are approved.

## Promotion Criteria

Expert mapping consistency, critical-path preservation and reviewer usability
must pass S2-S4 qualification. Source claims: `SBD-CLM-005`, `SBD-CLM-017`.


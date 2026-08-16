# ADR-005: Separate Knowledge Kind from Evidence State

Status: `DRAFT_NOT_LOADED`  
Date: 2026-08-16  
Decision owner: JSEA evidence governance

## Context

The research distinguishes invariant principles, engineering models, empirical
data, site context, human/organizational information and governance. These
categories answer a different question from whether a proposition is a fact,
reference, AI hypothesis, evidence gap or human-only decision.

## Decision

Keep two independent axes. `knowledge_kind` describes the proposition type.
`evidence_state` reuses the existing Unified Evidence Labels exactly:
`FACT`, `REFERENCE`, `AI_HYPOTHESIS`, `EVIDENCE_GAP`, and
`HUMAN_ONLY_DECISION`.

## Consequences

An engineering model may be a traceable reference while its applicability to the
current equipment remains an evidence gap. The design avoids creating a second,
competing evidence taxonomy.

## Guardrails

- Confidence is not probability, reliability or residual risk.
- Reference status does not prove applicability.
- Human-only decisions cannot be converted to model confidence.

## Promotion Criteria

Migration tests must preserve every existing evidence label and downstream rule.
Source claims: `SBD-CLM-006`, `SBD-CLM-011`.


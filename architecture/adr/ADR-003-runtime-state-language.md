# ADR-003: Evidence-Qualified Runtime State Language

Status: `DRAFT_NOT_LOADED`  
Date: 2026-08-16  
Decision owner: JSEA safety and communication governance

## Context

Research terms such as `nominal_safe`, `safe_degraded` and `stable_safe` are
compact, but can be read as AI approval of operation or work. This conflicts
with JSEA's existing authority boundary.

## Decision

Candidate runtime language will state what evidence supports for a named scope:

- `DeclaredConstraintsSupported`
- `ProtectionOrMarginDegraded`
- `ConstraintViolationRecoveryUnverified`
- `StableConditionSupportedForNamedHazard`
- `LossOfRecoverabilitySupportedByEngineeringEvidence`

The word safe may still appear when accurately naming an external technical
concept, but not as JSEA's work, operating or design disposition.

## Consequences

Output is longer but more explicit about scope, evidence and authority. FIELD_JSA
will need plain-language rendering if these concepts are later promoted.

## Guardrails

- Never say safe in all respects or safe to proceed.
- Never close a hold point through wording changes.
- Preserve the named hazard, mode, evidence and unresolved conditions.

## Promotion Criteria

Safe-label leakage and user-interpretation tests must pass. Source claim:
`SBD-CLM-019` and the controlled vocabulary collision map.


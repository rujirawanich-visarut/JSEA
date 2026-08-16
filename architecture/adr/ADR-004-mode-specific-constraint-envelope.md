# ADR-004: Internal Mode-Specific Constraint Envelope

Status: `DRAFT_NOT_LOADED`  
Date: 2026-08-16  
Decision owner: JSEA architecture and site-integration governance

## Context

Safe operating limits, operating windows, alarm limits, trip limits, design
limits and API Integrity Operating Windows serve different purposes. Calling a
new JSEA object a Safe Operating Envelope could overwrite established site
semantics or imply that JSEA defines the limits.

## Decision

Use `ModeSpecificConstraintEnvelope` as an internal candidate container. It may
reference only imported, approved constraints and must retain each source term,
owner, mode, units, validity period and applicability. A site adapter may map the
object to local terminology after explicit review.

## Consequences

The architecture can compare constraints without inventing a parallel site
standard. Startup, shutdown, maintenance and emergency modes can retain distinct
conditions and owners.

## Guardrails

- JSEA cannot generate limit values or choose the controlling limit.
- Design pressure is not treated as a complete operating criterion.
- Legal and site applicability remain explicit.

## Promotion Criteria

At least two real site terminology maps and collision reviews must pass.
Source claim: `SBD-CLM-012`.


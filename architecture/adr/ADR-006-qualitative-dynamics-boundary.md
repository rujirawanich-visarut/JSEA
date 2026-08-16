# ADR-006: Qualitative Dynamics by Default

Status: `DRAFT_NOT_LOADED`  
Date: 2026-08-16  
Decision owner: JSEA process-safety governance

## Context

Static values can miss accumulation, delayed reaction, changing topology and
feedback. A language model can identify these mechanisms, but narrative alone
does not provide a validated process model, parameters or uncertainty basis.

## Decision

JSEA may reason qualitatively about direction, rate significance, accumulation,
sequence, delay, feedback and hidden state. Quantitative trajectory,
time-to-harm, relief demand or loss-of-recoverability requires Decision Classes
`B/C/D/E/F` as applicable and remains outside language-only inference.

## Consequences

The system can identify why a current in-range value is not sufficient while
avoiding pseudo-simulation. Candidate outputs must name the data, model, test and
specialist needed for consequential numbers.

## Guardrails

- No invented rate, time, threshold or worst-case numerical value.
- No universal statement that depressurization cools or a mixture is stable.
- A qualitative feedback loop does not establish likelihood or adequacy.

## Promotion Criteria

Dynamic positive, negative and no-number tests must pass. Source claims:
`SBD-CLM-007`, `SBD-CLM-013`, `SBD-CLM-021`.


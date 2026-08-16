# Shared JSEA References

This directory is the canonical source for cross-package JSEA reference files.

The files here are mirrored into each package's `references/` directory so that
`jsea-hazard-blind-spot-mapper` and `jsea-safeguard-challenge-assistant` remain
standalone when distributed separately.

Canonical shared files:

- `unified-evidence-label-schema.yaml`
- `process-safety-information-retrieval-map.yaml`
- `stop-and-escalate-decision-rules.yaml`
- `competent-role-routing-matrix.yaml`
- `re-jsea-trigger-catalog.yaml`
- `jsea-output-behavior-contract.yaml`

When any canonical file changes, mirror the same content into both package
reference directories and verify the file hashes match.

Current shared decision-rule ranges:

- `SES-01` to `SES-11`
- `RT-01` to `RT-16`

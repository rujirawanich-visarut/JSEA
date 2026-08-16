# JSEA Validation Harness

Run from the workspace root:

```powershell
& 'C:\Users\rujir\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' .\scripts\validate_jsea.py
```

The harness checks JSON evals, YAML/reference structure, `SKILL.md` declared
paths, shared-reference mirror hashes, expected `SES`/`RT` ranges, stale markers,
the shared output behavior contract and field communication eval schema,
physics-causal claim/source ranges and required fields, the 30-case PICR
qualification contract, embedded-code and rejected-action guards, and dangling
rule/pattern IDs across both packages. Version 1.4.0 contains 98 eval cases.

If PyYAML is installed, YAML files are parsed with PyYAML. Without PyYAML, the
script uses fallback structural YAML checks and reports that as an info item.

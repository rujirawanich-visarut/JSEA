#!/usr/bin/env python3
"""Validate JSEA package consistency.

Checks:
- JSON files parse and evaluation cases use required fields.
- YAML files parse when PyYAML is available; otherwise run structural checks.
- SKILL.md frontmatter references and evaluations point to existing files.
- shared-references canonical files match both package mirrors byte-for-byte.
- The shared output behavior contract defines all required profiles, field
  sections, and field-table columns.
- Physics-causal claims, sources, policy contracts, and qualification cases use
  the required bounded-reasoning structure and contain no executable payloads.
- P3-SBD research intake, architecture decisions, controlled vocabulary,
  decision boundaries, and candidate evaluations remain traceable and unloaded.
- Cross-reference IDs such as SES, RT, PSI, PCR, CHE, PSCE, ICP, ENV-EM, DEP,
  HOC, HE, EA, PCV, and JT resolve to definitions.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

try:
    import yaml  # type: ignore
except Exception:  # pragma: no cover - optional dependency
    yaml = None


PACKAGE_DIRS = (
    "jsea-hazard-blind-spot-mapper",
    "jsea-safeguard-challenge-assistant",
)

SHARED_FILES = (
    "unified-evidence-label-schema.yaml",
    "process-safety-information-retrieval-map.yaml",
    "stop-and-escalate-decision-rules.yaml",
    "competent-role-routing-matrix.yaml",
    "re-jsea-trigger-catalog.yaml",
    "jsea-output-behavior-contract.yaml",
    "physics-causal-claim-schema.yaml",
    "physics-causal-reasoning-policy.yaml",
    "physics-causal-source-register.yaml",
    "physics-causal-mechanism-catalog.yaml",
)

OUTPUT_CONTRACT_FILE = "jsea-output-behavior-contract.yaml"
OUTPUT_MODES = (
    "FIELD_JSA",
    "MANAGEMENT",
    "TECHNICAL_REVIEW",
    "AUDIT_EVAL",
)
FIELD_REQUIRED_SECTIONS = (
    "ข้อมูลงานและสถานะการทบทวน",
    "จุดพักงานสำคัญ",
    "ตารางวิเคราะห์ความปลอดภัยตามขั้นตอนการปฏิบัติงาน",
    "PPE และอุปกรณ์เฉพาะงาน",
    "ความพร้อมด้านเหตุฉุกเฉินและสิ่งแวดล้อม",
    "สิ่งที่ต้องยืนยันก่อนเริ่มงาน",
    "ผู้ทบทวนและผู้มีอำนาจอนุมัติ",
)
FIELD_REQUIRED_COLUMNS = (
    "ลำดับขั้นตอนการทำงาน",
    "อันตรายที่อาจเกิดขึ้น",
    "มาตรการควบคุมและป้องกัน",
    "ผู้รับผิดชอบ",
)

ID_PREFIXES = (
    "SES",
    "RT",
    "PSI",
    "CHE",
    "PSCE",
    "ICP",
    "ENV-EM",
    "DEP",
    "HOC",
    "HE",
    "EA",
    "PCV",
    "JT",
    "PCR",
    "PCR-SRC",
)

PROCESS_CASE_FIELDS = (
    "case_id",
    "category",
    "severity",
    "title",
    "minimum_expected_behavior",
    "required_evidence_request",
    "required_escalation",
    "prohibited_ai_behavior",
    "expected_output_state",
    "pass_if",
    "fail_if",
)

FIELD_COMMUNICATION_CASE_FIELDS = (
    "case_id",
    "title",
    "input",
    "requested_mode",
    "expected_sections",
    "mapping_expectations",
    "must_include",
    "must_not_include",
    "pass_if",
    "fail_if",
)

CAUSAL_CASE_FIELDS = (
    "case_id",
    "category",
    "title",
    "input",
    "expected_activated_claims",
    "expected_rejected_claims",
    "expected_support_states",
    "expected_causal_links",
    "required_evidence_needs",
    "prohibited_inferences",
    "required_specialist_route",
    "pass_if",
    "fail_if",
)

CAUSAL_SUPPORT_STATES = {
    "SUPPORTED_BY_FACT",
    "PLAUSIBLE_UNVERIFIED",
    "CONTRADICTED",
    "NOT_APPLICABLE",
    "INSUFFICIENT_EVIDENCE",
    "SPECIALIST_CALCULATION_REQUIRED",
}

SBD_INTAKE_DIR = Path("knowledge-intake") / "deep-research-sbd-2026-08-16"
SBD_INTAKE_FILES = (
    "README.md",
    "file-integrity-manifest.yaml",
    "source-manifest.yaml",
    "claim-review-register.yaml",
    "citation-recovery-backlog.yaml",
)
SBD_ADR_FILES = (
    "ADR-001-typed-graph-master.md",
    "ADR-002-system-state-vs-assessment-state.md",
    "ADR-003-runtime-state-language.md",
    "ADR-004-mode-specific-constraint-envelope.md",
    "ADR-005-knowledge-kind-vs-evidence-state.md",
    "ADR-006-qualitative-dynamics-boundary.md",
    "ADR-007-design-review-separation.md",
)
SBD_RESEARCH_FILES = (
    "safety-by-design-controlled-vocabulary.yaml",
    "decision-boundary-schema.yaml",
)
SBD_EVAL_FILES = (
    "first-principles-dynamic-cases.json",
    "safeguard-dependency-cases.json",
)
SBD_CASE_FIELDS = (
    "case_id",
    "category",
    "title",
    "input",
    "target_capabilities",
    "expected_reasoning",
    "required_decision_classes",
    "required_evidence_needs",
    "prohibited_behavior",
    "responsible_roles",
    "pass_if",
    "fail_if",
)
SBD_DECISION_CLASSES = set("ABCDEFG")

ID_TOKEN_RE = re.compile(
    r"(?<!EVAL-)\b(?:PCR-SRC|ENV-EM|SES|RT|PSI|CHE|PSCE|ICP|DEP|HOC|HE|EA|PCV|JT|PCR)-\d{2,3}\b"
)
ID_DEF_RE = re.compile(
    r"(?m)^\s*-?\s*(?:id|case_id|type_id|code|pattern_id|prompt_id|rule_id|trigger_id|claim_id|source_id):\s*[\"']?([A-Z][A-Z0-9]*(?:-[A-Z0-9]+)*-\d{2,3})[\"']?"
)
FRONTMATTER_REF_RE = re.compile(r"^\s*-\s*(\S+)\s*$")
LEGACY_CASE_ID_FIELDS = ("case_id", "id")
LEGACY_CASE_CONTEXT_FIELDS = ("title", "name", "description", "scenario", "input")


@dataclass
class Finding:
    severity: str
    path: Path | None
    message: str

    def render(self, root: Path) -> str:
        location = str(self.path.relative_to(root)) if self.path else "workspace"
        return f"[{self.severity}] {location}: {self.message}"


class Validator:
    def __init__(self, root: Path, strict_yaml: bool = False) -> None:
        self.root = root
        self.strict_yaml = strict_yaml
        self.findings: list[Finding] = []
        self.definitions: dict[str, set[Path]] = {}
        self.uses: dict[str, set[Path]] = {}

    def error(self, path: Path | None, message: str) -> None:
        self.findings.append(Finding("ERROR", path, message))

    def warn(self, path: Path | None, message: str) -> None:
        self.findings.append(Finding("WARN", path, message))

    def info(self, path: Path | None, message: str) -> None:
        self.findings.append(Finding("INFO", path, message))

    def run(self) -> int:
        self.check_workspace_shape()
        self.check_skill_frontmatter()
        self.check_json_files()
        self.check_yaml_files()
        self.check_output_behavior_contract()
        self.check_physics_causal_contract()
        self.check_sbd_research_candidates()
        self.collect_ids()
        self.check_id_references()
        self.check_shared_mirrors()
        self.check_expected_rule_ranges()
        self.check_stale_markers()
        self.report()
        return 1 if any(f.severity == "ERROR" for f in self.findings) else 0

    def files(self, suffixes: Iterable[str]) -> Iterable[Path]:
        suffix_set = set(suffixes)
        for path in self.root.rglob("*"):
            if path.is_file() and path.suffix.lower() in suffix_set:
                yield path

    def check_workspace_shape(self) -> None:
        for package in PACKAGE_DIRS:
            path = self.root / package
            if not path.is_dir():
                self.error(path, "Package directory is missing")
            if not (path / "SKILL.md").is_file():
                self.error(path / "SKILL.md", "SKILL.md is missing")
        shared = self.root / "shared-references"
        if not shared.is_dir():
            self.error(shared, "shared-references directory is missing")
        for filename in SHARED_FILES:
            if not (shared / filename).is_file():
                self.error(shared / filename, "Canonical shared reference is missing")

    def frontmatter_block(self, skill: Path) -> str:
        text = skill.read_text(encoding="utf-8")
        lines = text.splitlines()
        if not lines or lines[0].strip() != "---":
            self.error(skill, "Missing YAML frontmatter opener")
            return ""
        try:
            end = lines[1:].index("---") + 1
        except ValueError:
            self.error(skill, "Missing YAML frontmatter closer")
            return ""
        return "\n".join(lines[1:end])

    def frontmatter_list(self, block: str, key: str) -> list[str]:
        values: list[str] = []
        in_list = False
        for line in block.splitlines():
            if re.match(rf"^{re.escape(key)}:\s*$", line):
                in_list = True
                continue
            if in_list and re.match(r"^[A-Za-z_][A-Za-z0-9_]*:", line):
                break
            if in_list:
                match = FRONTMATTER_REF_RE.match(line)
                if match:
                    values.append(match.group(1))
        return values

    def frontmatter_scalar(self, block: str, key: str) -> str | None:
        match = re.search(rf"(?m)^{re.escape(key)}:\s*(.+?)\s*$", block)
        return match.group(1).strip().strip("\"'") if match else None

    def check_skill_frontmatter(self) -> None:
        for package in PACKAGE_DIRS:
            skill = self.root / package / "SKILL.md"
            block = self.frontmatter_block(skill)
            if not block:
                continue
            version = self.frontmatter_scalar(block, "version")
            if not version:
                self.error(skill, "Frontmatter version is missing")
            refs = self.frontmatter_list(block, "references")
            evals = self.frontmatter_list(block, "evaluations")
            if not refs:
                self.error(skill, "No references declared in frontmatter")
            if not evals:
                self.error(skill, "No evaluations declared in frontmatter")
            for rel in refs + evals:
                target = self.root / package / rel
                if not target.is_file():
                    self.error(skill, f"Declared path does not exist: {rel}")
            if "Reference Loading Contract" not in skill.read_text(encoding="utf-8"):
                self.error(skill, "Reference Loading Contract section is missing")
            if f"references/{OUTPUT_CONTRACT_FILE}" not in refs:
                self.error(skill, f"Shared output contract is not declared: references/{OUTPUT_CONTRACT_FILE}")
            for causal_reference in (
                "physics-causal-claim-schema.yaml",
                "physics-causal-reasoning-policy.yaml",
                "physics-causal-source-register.yaml",
                "physics-causal-mechanism-catalog.yaml",
            ):
                if f"references/{causal_reference}" not in refs:
                    self.error(skill, f"Physics-causal reference is not declared: references/{causal_reference}")
            if "Output Profile Routing" not in skill.read_text(encoding="utf-8"):
                self.error(skill, "Output Profile Routing section is missing")
            if "Physics-Informed Causal" not in skill.read_text(encoding="utf-8"):
                self.error(skill, "Physics-Informed Causal workflow section is missing")
            expected_field_eval = {
                "jsea-hazard-blind-spot-mapper": "evals/field-jsa-output-cases.json",
                "jsea-safeguard-challenge-assistant": "evals/field-safeguard-output-cases.json",
            }[package]
            if expected_field_eval not in evals:
                self.error(skill, f"Field communication evaluation is not declared: {expected_field_eval}")
            if package == "jsea-hazard-blind-spot-mapper" and "evals/physics-causal-reasoning-cases.json" not in evals:
                self.error(skill, "Physics-causal qualification evaluation is not declared")

    def check_json_files(self) -> None:
        for path in self.files((".json",)):
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
            except Exception as exc:
                self.error(path, f"JSON parse failed: {exc}")
                continue
            cases = self.extract_cases(data)
            if path.parts[-2:] and "evals" in path.parts:
                if not cases:
                    self.error(path, "Evaluation file has no cases")
                case_ids = [case.get("case_id") for case in cases if isinstance(case, dict) and case.get("case_id")]
                duplicate_case_ids = sorted({case_id for case_id in case_ids if case_ids.count(case_id) > 1})
                if duplicate_case_ids:
                    self.error(path, f"Duplicate evaluation case IDs: {duplicate_case_ids}")
                for index, case in enumerate(cases):
                    if not isinstance(case, dict):
                        self.error(path, f"Case #{index + 1} is not an object")
                        continue
                    if self.is_process_eval(path):
                        for field in PROCESS_CASE_FIELDS:
                            if field not in case:
                                self.error(path, f"{case.get('case_id', 'case #' + str(index + 1))} missing process eval field: {field}")
                    elif self.is_field_communication_eval(path):
                        for field in FIELD_COMMUNICATION_CASE_FIELDS:
                            if field not in case:
                                self.error(path, f"{case.get('case_id', 'case #' + str(index + 1))} missing field communication eval field: {field}")
                        requested_mode = case.get("requested_mode")
                        if requested_mode not in (*OUTPUT_MODES, "DEFAULT"):
                            self.error(path, f"{case.get('case_id', 'case #' + str(index + 1))} has unsupported requested_mode: {requested_mode}")
                    elif self.is_physics_causal_eval(path):
                        for field in CAUSAL_CASE_FIELDS:
                            if field not in case:
                                self.error(path, f"{case.get('case_id', 'case #' + str(index + 1))} missing causal eval field: {field}")
                        support_states = case.get("expected_support_states", [])
                        if not isinstance(support_states, list):
                            self.error(path, f"{case.get('case_id', 'case #' + str(index + 1))} expected_support_states must be a list")
                        else:
                            unknown_states = sorted(set(support_states) - CAUSAL_SUPPORT_STATES)
                            if unknown_states:
                                self.error(path, f"{case.get('case_id', 'case #' + str(index + 1))} has unsupported causal state(s): {unknown_states}")
                    else:
                        if not any(field in case for field in LEGACY_CASE_ID_FIELDS):
                            self.error(path, f"Case #{index + 1} missing a case identifier field")
                        if not any(field in case for field in LEGACY_CASE_CONTEXT_FIELDS):
                            self.error(path, f"Case #{index + 1} missing a case context field")
                self.info(path, f"Evaluation cases: {len(cases)}")
                if self.is_physics_causal_eval(path) and len(cases) != 30:
                    self.error(path, f"Physics-causal qualification suite must contain exactly 30 cases, found {len(cases)}")

    def extract_cases(self, data: object) -> list[object]:
        if isinstance(data, list):
            return data
        if isinstance(data, dict):
            for key in ("cases", "test_cases", "evals"):
                value = data.get(key)
                if isinstance(value, list):
                    return value
        return []

    def is_process_eval(self, path: Path) -> bool:
        name = path.name
        return name in {
            "chemical-process-blind-spot-cases.json",
            "process-safeguard-red-team-cases.json",
        }

    def is_field_communication_eval(self, path: Path) -> bool:
        return path.name in {
            "field-jsa-output-cases.json",
            "field-safeguard-output-cases.json",
        }

    def is_physics_causal_eval(self, path: Path) -> bool:
        return path.name == "physics-causal-reasoning-cases.json"

    def check_yaml_files(self) -> None:
        for path in self.files((".yaml", ".yml")):
            text = path.read_text(encoding="utf-8")
            if "\t" in text:
                self.error(path, "YAML contains tab characters")
            if yaml is not None:
                try:
                    yaml.safe_load(text)
                except Exception as exc:
                    self.error(path, f"YAML parse failed: {exc}")
            else:
                self.lightweight_yaml_check(path, text)
        if yaml is None:
            message = "PyYAML unavailable; used fallback YAML structural checks"
            if self.strict_yaml:
                self.error(None, message)
            else:
                self.info(None, message)

    def lightweight_yaml_check(self, path: Path, text: str) -> None:
        if not text.strip():
            self.error(path, "YAML file is empty")
        for line_number, line in enumerate(text.splitlines(), start=1):
            if "\t" in line:
                self.error(path, f"YAML contains tab characters on line {line_number}")

    def check_output_behavior_contract(self) -> None:
        path = self.root / "shared-references" / OUTPUT_CONTRACT_FILE
        if not path.is_file():
            return
        text = path.read_text(encoding="utf-8")
        if 'default_output_mode: "FIELD_JSA"' not in text:
            self.error(path, "FIELD_JSA is not the default output mode")
        for mode in OUTPUT_MODES:
            if f'- "{mode}"' not in text:
                self.error(path, f"Required output mode is missing: {mode}")
        for section in FIELD_REQUIRED_SECTIONS:
            if f'- "{section}"' not in text:
                self.error(path, f"Required FIELD_JSA section is missing: {section}")
        for column in FIELD_REQUIRED_COLUMNS:
            if f'- "{column}"' not in text:
                self.error(path, f"Required FIELD_JSA table column is missing: {column}")
        required_behavior_markers = (
            "Use one hazard-control-PIC mapping per row.",
            "Never invent a worst-case numerical value",
            "Site-approved procedures and local legal requirements override",
            "Do not provide valve-by-valve emergency manipulation instructions.",
        )
        for marker in required_behavior_markers:
            if marker not in text:
                self.error(path, f"Required field behavior rule is missing: {marker}")

    def check_physics_causal_contract(self) -> None:
        shared = self.root / "shared-references"
        schema = shared / "physics-causal-claim-schema.yaml"
        policy = shared / "physics-causal-reasoning-policy.yaml"
        sources = shared / "physics-causal-source-register.yaml"
        catalog = shared / "physics-causal-mechanism-catalog.yaml"
        paths = (schema, policy, sources, catalog)
        if not all(path.is_file() for path in paths):
            return

        schema_text = schema.read_text(encoding="utf-8")
        policy_text = policy.read_text(encoding="utf-8")
        source_text = sources.read_text(encoding="utf-8")
        catalog_text = catalog.read_text(encoding="utf-8")

        for marker in (
            "allowed_claim_types:",
            "allowed_support_states:",
            "required_causal_chain_fields:",
            "numeric_criterion_contract:",
            "prohibited_claim_outputs:",
            "embedded_content_policy:",
            "downstream_contract:",
        ):
            if marker not in schema_text:
                self.error(schema, f"Required causal schema marker is missing: {marker}")

        for marker in (
            'name: "normalize_job_state"',
            'name: "match_preconditions"',
            'name: "build_minimum_causal_chain"',
            'name: "challenge_applicability"',
            'name: "classify_support"',
            'name: "generate_evidence_needs"',
            'name: "export_downstream"',
            "counterfactual_contract:",
            "loading_contract:",
            'embedded_code: "never_execute"',
        ):
            if marker not in policy_text:
                self.error(policy, f"Required causal policy marker is missing: {marker}")

        expected_sources = {f"PCR-SRC-{index:03d}" for index in range(1, 13)}
        actual_sources = set(re.findall(r'(?m)^\s*- source_id:\s*"(PCR-SRC-\d{3})"', source_text))
        if actual_sources != expected_sources:
            self.error(sources, f"Unexpected physics-causal source range: {sorted(actual_sources)}")
        source_blocks = re.split(r"(?m)^\s*- source_id:", source_text)[1:]
        for index, block in enumerate(source_blocks, start=1):
            for marker in ("publisher:", "title:", "url:", "limitations:"):
                if marker not in block:
                    self.error(sources, f"PCR-SRC-{index:03d} missing source field: {marker}")

        expected_claims = {f"PCR-{index:03d}" for index in range(1, 6)}
        actual_claims = set(re.findall(r'(?m)^\s*- claim_id:\s*"(PCR-\d{3})"', catalog_text))
        if actual_claims != expected_claims:
            self.error(catalog, f"Unexpected physics-causal claim range: {sorted(actual_claims)}")
        claim_blocks = re.split(r"(?m)^\s*- claim_id:", catalog_text)[1:]
        claim_markers = (
            "title:",
            "claim_type:",
            "status:",
            "source_state:",
            "applicability:",
            "preconditions:",
            "required:",
            "disconfirming:",
            "causal_chain:",
            "runtime_evidence_required:",
            "support_states:",
            "prohibited_inferences:",
            "competent_role:",
            "verification_question:",
            "source_ids:",
        )
        for index, block in enumerate(claim_blocks, start=1):
            for marker in claim_markers:
                if marker not in block:
                    self.error(catalog, f"PCR-{index:03d} missing claim field: {marker}")
        if "numeric_criteria: []" not in catalog_text:
            self.error(catalog, "Wave 1 catalog must not contain unqualified numeric criteria")

        executable_markers = ("```python", "\ndef ", "\nclass ", "\nimport ", "return {\"decision\"")
        for path, text in zip(paths, (schema_text, policy_text, source_text, catalog_text)):
            for marker in executable_markers:
                if marker in text:
                    self.error(path, f"Executable or decision payload is prohibited in canonical knowledge: {marker!r}")

        prohibited_import_markers = (
            'decision: "APPROVED"',
            "system_veto",
            "CMMS Status Locked",
            "ARCHITECTURAL VETO",
            "RFID interlock",
        )
        for marker in prohibited_import_markers:
            if marker in catalog_text:
                self.error(catalog, f"Rejected NotebookLM action logic was imported: {marker}")

    def check_sbd_research_candidates(self) -> None:
        intake = self.root / SBD_INTAKE_DIR
        adr_dir = self.root / "architecture" / "adr"
        research_dir = self.root / "research-candidates"
        eval_dir = self.root / "eval-candidates"

        for filename in SBD_INTAKE_FILES:
            path = intake / filename
            if not path.is_file():
                self.error(path, "P3-SBD intake artifact is missing")
        for filename in SBD_ADR_FILES:
            path = adr_dir / filename
            if not path.is_file():
                self.error(path, "P3-SBD architecture decision record is missing")
        for filename in SBD_RESEARCH_FILES:
            path = research_dir / filename
            if not path.is_file():
                self.error(path, "P3-SBD research candidate is missing")
        for filename in SBD_EVAL_FILES:
            path = eval_dir / filename
            if not path.is_file():
                self.error(path, "P3-SBD evaluation candidate is missing")

        required_paths = (
            *(intake / filename for filename in SBD_INTAKE_FILES),
            *(adr_dir / filename for filename in SBD_ADR_FILES),
            *(research_dir / filename for filename in SBD_RESEARCH_FILES),
            *(eval_dir / filename for filename in SBD_EVAL_FILES),
        )
        if not all(path.is_file() for path in required_paths):
            return

        self.check_sbd_intake(intake)
        self.check_sbd_adrs(adr_dir)
        self.check_sbd_vocab_and_boundaries(research_dir)
        self.check_sbd_candidate_evals(eval_dir)
        self.check_sbd_runtime_separation()

    def check_sbd_intake(self, intake: Path) -> None:
        integrity = intake / "file-integrity-manifest.yaml"
        sources = intake / "source-manifest.yaml"
        claims = intake / "claim-review-register.yaml"
        backlog = intake / "citation-recovery-backlog.yaml"
        integrity_text = integrity.read_text(encoding="utf-8")
        source_text = sources.read_text(encoding="utf-8")
        claim_text = claims.read_text(encoding="utf-8")
        backlog_text = backlog.read_text(encoding="utf-8")

        intake_statuses = (
            (integrity, integrity_text, 'status: "DRAFT_NOT_LOADED"'),
            (sources, source_text, 'status: "DRAFT_NOT_LOADED"'),
            (claims, claim_text, 'status: "RESEARCH_CANDIDATE"'),
            (backlog, backlog_text, 'status: "DRAFT_NOT_LOADED"'),
        )
        for path, text, expected_status in intake_statuses:
            if expected_status not in text or "runtime_loaded: false" not in text:
                self.error(path, f"SBD intake must remain unloaded with lifecycle marker: {expected_status}")

        raw_expectations = {
            "SBD-RAW-001": (
                self.root / "First-Principles Safety-by-Design phase1.md",
                "b1e0b76a7f131817b93975c666a195b45fbc1254e40b33cd62c7c41c61973149",
                188,
                50,
            ),
            "SBD-RAW-002": (
                self.root / "First-Principles Safety-by-Design phase2.md",
                "026bed48cb7ad5434e33d7f7c692e9f27caa549c56147a661acc31e689f3b138",
                167,
                61,
            ),
        }
        for raw_id, (path, expected_hash, occurrence_count, unique_count) in raw_expectations.items():
            if not path.is_file():
                self.error(path, f"Raw SBD research input is missing: {raw_id}")
                continue
            actual_hash = sha256(path)
            if actual_hash != expected_hash:
                self.error(path, f"Raw SBD research hash changed for {raw_id}: {actual_hash}")
            raw_text = path.read_text(encoding="utf-8")
            markers = re.findall(r"turn\d+(?:search|view|fetch|file)\d+", raw_text)
            if len(markers) != occurrence_count or len(set(markers)) != unique_count:
                self.error(path, f"Opaque citation inventory changed for {raw_id}")
            if "http://" in raw_text or "https://" in raw_text:
                self.error(path, f"Direct-URL baseline changed for {raw_id}; refresh S0 intake")
            if expected_hash not in integrity_text or raw_id not in integrity_text:
                self.error(integrity, f"Integrity manifest does not record {raw_id} and its current hash")

            backlog_blocks = re.split(r"(?m)^\s*- backlog_id:", backlog_text)[1:]
            matching = [block for block in backlog_blocks if f'raw_file_id: "{raw_id}"' in block]
            if len(matching) != 1:
                self.error(backlog, f"Citation backlog must contain one block for {raw_id}")
            else:
                recorded = set(re.findall(r"turn\d+(?:search|view|fetch|file)\d+", matching[0]))
                if recorded != set(markers):
                    self.error(backlog, f"Opaque marker inventory mismatch for {raw_id}")

        if "opaque_markers_are_evidence: false" not in source_text:
            self.error(sources, "Source policy must reject opaque markers as evidence")
        if re.search(r"turn\d+(?:search|view|fetch|file)\d+", source_text + claim_text):
            self.error(sources, "Opaque citation marker leaked into source or claim evidence")

        expected_sources = {f"SBD-SRC-{index:03d}" for index in range(1, 27)}
        actual_sources = set(re.findall(r'(?m)^\s*- source_id:\s*"(SBD-SRC-\d{3})"', source_text))
        if actual_sources != expected_sources:
            self.error(sources, f"Unexpected SBD source range: {sorted(actual_sources)}")
        source_blocks = re.split(r"(?m)^\s*- source_id:", source_text)[1:]
        for index, block in enumerate(source_blocks, start=1):
            source_id = f"SBD-SRC-{index:03d}"
            for marker in ("title:", "publisher:", "source_type:", "authority:", "jurisdiction:", "applicability:", "limitations:", "reviewed_on:"):
                if marker not in block:
                    self.error(sources, f"{source_id} missing source field: {marker}")
            if index >= 3 and not re.search(r'url:\s*"https://', block):
                self.error(sources, f"{source_id} must have a direct HTTPS source")

        expected_claims = {f"SBD-CLM-{index:03d}" for index in range(1, 23)}
        actual_claims = set(re.findall(r'(?m)^\s*- claim_id:\s*"(SBD-CLM-\d{3})"', claim_text))
        if actual_claims != expected_claims:
            self.error(claims, f"Unexpected SBD claim range: {sorted(actual_claims)}")
        allowed_dispositions = {
            "VERIFIED_PRIMARY",
            "VERIFIED_RECOGNIZED",
            "RESEARCHER_SYNTHESIS",
            "NEEDS_SOURCE",
            "REJECTED_FOR_RUNTIME",
        }
        claim_blocks = re.split(r"(?m)^\s*- claim_id:", claim_text)[1:]
        for index, block in enumerate(claim_blocks, start=1):
            claim_id = f"SBD-CLM-{index:03d}"
            for marker in ("title:", "disposition:", "knowledge_kind:", "source_ids:", "intended_use:", "limitation:"):
                if marker not in block:
                    self.error(claims, f"{claim_id} missing claim field: {marker}")
            disposition_match = re.search(r'disposition:\s*"([A-Z_]+)"', block)
            disposition = disposition_match.group(1) if disposition_match else ""
            if disposition not in allowed_dispositions:
                self.error(claims, f"{claim_id} has unsupported disposition: {disposition}")
            used_sources = set(re.findall(r"SBD-SRC-\d{3}", block))
            unknown_sources = used_sources - actual_sources
            if unknown_sources:
                self.error(claims, f"{claim_id} references unknown sources: {sorted(unknown_sources)}")
            if disposition.startswith("VERIFIED") and used_sources <= {"SBD-SRC-001", "SBD-SRC-002"}:
                self.error(claims, f"{claim_id} is verified only by an untrusted raw report")

        required_gate_markers = (
            's0_gate_status: "COMPLETE_FOR_DECLARED_CLAIM_SET"',
            "numeric_criteria: []",
            'backlog_status: "OPEN_NON_BLOCKING"',
            "opaque_marker_occurrences: 355",
            "original_bibliography_received: false",
        )
        for marker in required_gate_markers[:2]:
            if marker not in claim_text:
                self.error(claims, f"S0 claim gate marker is missing: {marker}")
        for marker in required_gate_markers[2:]:
            if marker not in backlog_text:
                self.error(backlog, f"S0 citation backlog marker is missing: {marker}")

        self.info(intake, f"S0 source recovery: {len(actual_claims)} reviewed claims, {len(actual_sources) - 2} direct external sources")

    def check_sbd_adrs(self, adr_dir: Path) -> None:
        actual = {path.name for path in adr_dir.glob("ADR-*.md")}
        expected = set(SBD_ADR_FILES)
        if actual != expected:
            self.error(adr_dir, f"Unexpected SBD ADR set: {sorted(actual)}")
        for filename in SBD_ADR_FILES:
            path = adr_dir / filename
            text = path.read_text(encoding="utf-8")
            for marker in ("Status: `DRAFT_NOT_LOADED`", "## Context", "## Decision", "## Guardrails", "## Promotion Criteria"):
                if marker not in text:
                    self.error(path, f"ADR marker is missing: {marker}")
        self.info(adr_dir, f"P3-SBD architecture decisions: {len(SBD_ADR_FILES)} draft ADRs")

    def check_sbd_vocab_and_boundaries(self, research_dir: Path) -> None:
        vocabulary = research_dir / "safety-by-design-controlled-vocabulary.yaml"
        boundaries = research_dir / "decision-boundary-schema.yaml"
        vocab_text = vocabulary.read_text(encoding="utf-8")
        boundary_text = boundaries.read_text(encoding="utf-8")
        for path, text in ((vocabulary, vocab_text), (boundaries, boundary_text)):
            if 'status: "DRAFT_NOT_LOADED"' not in text or "runtime_loaded: false" not in text:
                self.error(path, "Research candidate must remain DRAFT_NOT_LOADED and runtime_loaded false")

        evidence_labels = ("FACT", "REFERENCE", "AI_HYPOTHESIS", "EVIDENCE_GAP", "HUMAN_ONLY_DECISION")
        for label in evidence_labels:
            if f'"{label}"' not in vocab_text:
                self.error(vocabulary, f"Existing evidence label is missing: {label}")
        for marker in ("knowledge_kind:", "evidence_state:", "candidate_terms:", "collision_map:", "promotion_gate:"):
            if marker not in vocab_text:
                self.error(vocabulary, f"Controlled-vocabulary marker is missing: {marker}")
        for term in ("SystemStateSnapshot", "ObservedState", "AssessmentState", "ModeSpecificConstraintEnvelope", "SafeguardDependency", "HoldPoint"):
            if f'term: "{term}"' not in vocab_text:
                self.error(vocabulary, f"Required controlled term is missing: {term}")

        classes = re.findall(r'(?m)^\s*- class:\s*"([A-G])"', boundary_text)
        if set(classes) != SBD_DECISION_CLASSES or len(classes) != 7:
            self.error(boundaries, f"Decision boundary must define A-G exactly once, found: {classes}")
        for marker in ("classification_rule:", "closure_rule:", "required_fields:", "compound_routing_examples:", "hold_point_triggers:", "promotion_gate:"):
            if marker not in boundary_text:
                self.error(boundaries, f"Decision-boundary marker is missing: {marker}")
        self.info(research_dir, "P3-SBD controlled vocabulary and A-G decision boundary remain research-only")

    def check_sbd_candidate_evals(self, eval_dir: Path) -> None:
        all_cases: list[dict[str, object]] = []
        for filename in SBD_EVAL_FILES:
            path = eval_dir / filename
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
            except Exception as exc:
                self.error(path, f"SBD candidate JSON parse failed: {exc}")
                continue
            if data.get("status") != "DRAFT_NOT_LOADED" or data.get("runtime_loaded") is not False:
                self.error(path, "SBD eval candidate must remain DRAFT_NOT_LOADED and runtime_loaded false")
            cases = data.get("candidate_cases")
            if not isinstance(cases, list):
                self.error(path, "SBD eval file must contain candidate_cases")
                continue
            for index, case in enumerate(cases, start=1):
                if not isinstance(case, dict):
                    self.error(path, f"Candidate case #{index} is not an object")
                    continue
                for field in SBD_CASE_FIELDS:
                    if field not in case:
                        self.error(path, f"{case.get('case_id', 'case #' + str(index))} missing SBD candidate field: {field}")
                decision_classes = case.get("required_decision_classes", [])
                if not isinstance(decision_classes, list):
                    self.error(path, f"{case.get('case_id')} required_decision_classes must be a list")
                else:
                    unknown = set(decision_classes) - SBD_DECISION_CLASSES
                    if unknown:
                        self.error(path, f"{case.get('case_id')} has unknown decision classes: {sorted(unknown)}")
                all_cases.append(case)

        expected_ids = {f"EVAL-SBD-CAND-{index:03d}" for index in range(1, 18)}
        actual_ids = {str(case.get("case_id")) for case in all_cases}
        if actual_ids != expected_ids or len(all_cases) != 17:
            self.error(eval_dir, f"SBD candidate suite must contain exactly 17 unique cases, found {len(all_cases)}")
        self.info(eval_dir, f"P3-SBD evaluation candidates: {len(all_cases)} (not included in runtime eval count)")

    def check_sbd_runtime_separation(self) -> None:
        prohibited_skill_markers = (
            "deep-research-sbd-2026-08-16",
            "research-candidates",
            "eval-candidates",
            "SBD-CLM-",
        )
        for package in PACKAGE_DIRS:
            skill = self.root / package / "SKILL.md"
            text = skill.read_text(encoding="utf-8")
            for marker in prohibited_skill_markers:
                if marker in text:
                    self.error(skill, f"Research-only P3-SBD artifact leaked into runtime declaration: {marker}")

        shared = self.root / "shared-references"
        for path in shared.glob("*"):
            if not path.is_file():
                continue
            text = path.read_text(encoding="utf-8")
            if "SBD-CLM-" in text or "EVAL-SBD-CAND-" in text:
                self.error(path, "P3-SBD research candidate leaked into canonical shared references")

    def collect_ids(self) -> None:
        for path in self.files((".yaml", ".json", ".md")):
            if path.name == "JSEA_implementation plan":
                continue
            text = path.read_text(encoding="utf-8")
            if not path.name.endswith("_plan.md"):
                for match in ID_DEF_RE.finditer(text):
                    token = match.group(1)
                    if token.startswith(ID_PREFIXES):
                        self.definitions.setdefault(token, set()).add(path)
            for token in ID_TOKEN_RE.findall(text):
                self.uses.setdefault(token, set()).add(path)

    def check_id_references(self) -> None:
        for token, paths in sorted(self.uses.items()):
            if token not in self.definitions:
                for path in sorted(paths):
                    if self.ignore_undefined_token(token, path):
                        continue
                    self.error(path, f"ID reference has no definition: {token}")
        for token, paths in sorted(self.definitions.items()):
            if len(paths) > 3 and not token.startswith(("SES", "RT", "PSI")):
                locations = ", ".join(str(p.relative_to(self.root)) for p in sorted(paths))
                self.warn(None, f"ID defined in many places: {token} ({locations})")

    def ignore_undefined_token(self, token: str, path: Path) -> bool:
        # Roadmap prose is non-operational. Package docs may mention ranges.
        if path.name == "JSEA_implementation plan":
            return True
        if path.name == "README.md" and token in {"SES-01", "SES-11", "RT-01", "RT-16"}:
            return True
        return False

    def check_shared_mirrors(self) -> None:
        shared = self.root / "shared-references"
        for filename in SHARED_FILES:
            canonical = shared / filename
            if not canonical.is_file():
                continue
            canonical_hash = sha256(canonical)
            for package in PACKAGE_DIRS:
                mirror = self.root / package / "references" / filename
                if not mirror.is_file():
                    self.error(mirror, f"Shared mirror is missing for {filename}")
                    continue
                mirror_hash = sha256(mirror)
                if mirror_hash != canonical_hash:
                    self.error(mirror, f"Shared mirror hash mismatch for {filename}")

    def check_expected_rule_ranges(self) -> None:
        ses = sorted(token for token in self.definitions if token.startswith("SES-"))
        rt = sorted(token for token in self.definitions if token.startswith("RT-"))
        if ses != [f"SES-{i:02d}" for i in range(1, 12)]:
            self.error(self.root / "shared-references" / "stop-and-escalate-decision-rules.yaml", f"Unexpected SES range: {ses}")
        if rt != [f"RT-{i:02d}" for i in range(1, 17)]:
            self.error(self.root / "shared-references" / "re-jsea-trigger-catalog.yaml", f"Unexpected RT range: {rt}")

    def check_stale_markers(self) -> None:
        stale_patterns = (
            "SES-04 modified",
            "SES-01 to SES-10",
            "SES-01 to SES-09",
            "Package Structure (v1.1.0)",
            "Current Version:** `1.1.0`",
            "Activate JSEA Hazard Blind-Spot Mapper (v1.1.0)",
            "Activate JSEA Safeguard Challenge Assistant (v1.1.0)",
            "Package Structure (v1.2.0)",
            "Current Version:** `1.2.0`",
            "Activate JSEA Hazard Blind-Spot Mapper (v1.2.0)",
            "Activate JSEA Safeguard Challenge Assistant (v1.2.0)",
            "Package version (v1.2.0)",
            "Skill name and version (v1.1.0)",
        )
        for path in self.files((".md", ".yaml", ".json")):
            text = path.read_text(encoding="utf-8")
            for pattern in stale_patterns:
                if pattern in text:
                    self.error(path, f"Stale marker found: {pattern}")

    def report(self) -> None:
        errors = [f for f in self.findings if f.severity == "ERROR"]
        warnings = [f for f in self.findings if f.severity == "WARN"]
        infos = [f for f in self.findings if f.severity == "INFO"]
        for finding in errors + warnings + infos:
            print(finding.render(self.root))
        print()
        print(f"Validation summary: {len(errors)} error(s), {len(warnings)} warning(s), {len(infos)} info item(s)")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Validate JSEA package consistency")
    parser.add_argument("--root", default=".", help="Workspace root to validate")
    parser.add_argument(
        "--strict-yaml",
        action="store_true",
        help="Fail when PyYAML is unavailable instead of using fallback checks",
    )
    args = parser.parse_args(argv)
    root = Path(args.root).resolve()
    return Validator(root=root, strict_yaml=args.strict_yaml).run()


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

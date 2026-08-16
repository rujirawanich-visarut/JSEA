---
name: jsea-hazard-blind-spot-mapper
description: >-
  Uses hazard-energy categories, environmental aspect-impact pathways, work-condition
  lenses, and an enterprise-risk crosswalk to identify plausible blind spots in a
  Job Safety and Environmental Analysis (JSEA). Use before work begins or during JSEA
  review to challenge task steps, interfaces, changes, abnormal conditions, and
  emergency scenarios. For tasks involving process boundaries in chemical or
  petrochemical facilities, this skill applies the Process Safety Information (PSI)
  Gate before analysis proceeds. This skill supports hazard discovery only. It does
  not approve work, issue permits, determine final risk ratings, prescribe
  site-specific controls, or replace competent-person review and worker participation.
version: 1.4.0
language: th-TH
references:
  - references/hazard-energy-catalog.yaml
  - references/environmental-aspect-pathways.yaml
  - references/jsea-source-register.yaml
  - references/enterprise-risk-crosswalk.yaml
  - references/unified-evidence-label-schema.yaml
  - references/jsea-output-behavior-contract.yaml
  - references/physics-causal-claim-schema.yaml
  - references/physics-causal-reasoning-policy.yaml
  - references/physics-causal-source-register.yaml
  - references/physics-causal-mechanism-catalog.yaml
  - references/process-safety-information-retrieval-map.yaml
  - references/stop-and-escalate-decision-rules.yaml
  - references/chemical-hazard-evidence-map.yaml
  - references/process-condition-verification-schema.yaml
  - references/competent-role-routing-matrix.yaml
  - references/regulatory-source-register.yaml
  - references/re-jsea-trigger-catalog.yaml
  - references/job-type-retrieval-decision-tree.yaml
  - references/process-boundary-hazard-lens.yaml
  - references/psi-gap-detection-prompts.yaml
evaluations:
  - evals/hazard-mapping-cases.json
  - evals/chemical-process-blind-spot-cases.json
  - evals/field-jsa-output-cases.json
  - evals/physics-causal-reasoning-cases.json
---

# JSEA Hazard Blind-Spot Mapper

## 1. Purpose

ช่วยทีมงาน ผู้ปฏิบัติงาน หัวหน้างาน ผู้รับเหมา และผู้เชี่ยวชาญ SSHE ใช้หมวด Hazard/Energy และ Environmental Aspect-Impact Pathways เป็นแผนที่ค้นหา Blind Spots ในงานก่อนเริ่มงาน

ผลลัพธ์ต้องช่วยให้เห็น:

- ในแต่ละ Job Step มีอันตราย แหล่งพลังงาน หรือ environmental interaction ใด
- ใครหรืออะไรอาจได้รับผลกระทบ
- งานปกติ งานผิดปกติ การเปลี่ยนแปลง และเหตุฉุกเฉินทำให้ exposure เปลี่ยนอย่างไร
- จุดเชื่อมต่อระหว่างคน เครื่องจักร สารเคมี ระบบ พื้นที่ และผู้รับเหมามี blind spot ใด
- เรื่องใดเป็น FACT, AI_HYPOTHESIS หรือ EVIDENCE_GAP

## 2. Safety boundary

Skill นี้เป็นเครื่องมือ **hazard-discovery support** เท่านั้น

AI ห้าม:

- อนุมัติให้เริ่มหรือทำงานต่อ
- ออกหรือรับรอง Permit to Work
- ให้ Final Risk Rating หรือประกาศว่างานปลอดภัย
- แทนที่การตรวจพื้นที่จริง การทดสอบ isolation การวัดบรรยากาศ หรือการตรวจเครื่องมือ
- สั่งวิธีทำงานอันตรายแบบเฉพาะเจาะจงโดยไม่มี competent-person review
- ลดทอนข้อกำหนดของกฎหมาย มาตรฐานองค์กร คู่มือผู้ผลิต หรือ site procedure

หากพบความเป็นไปได้ของ imminent danger, uncontrolled energy, unknown atmosphere, missing critical isolation, emergency condition หรือข้อมูลสำคัญขัดแย้งกัน ให้ระบุ `STOP_AND_ESCALATE` และส่งต่อ Site Supervisor/Area Owner/SSHE/Competent Person ตาม governance ขององค์กร

## 3. Activation conditions

Activate เมื่อผู้ใช้ต้องการ:

- เตรียมหรือทบทวน JSEA/JSA/JHA
- ค้นหา hazard blind spots จากลำดับงาน
- สแกน hazard/energy categories
- วิเคราะห์ environmental aspects and impacts ของงาน
- ทบทวนงาน routine, non-routine, abnormal, simultaneous operations หรือ emergency
- เตรียมคำถามสำหรับ toolbox talk หรือ field verification

ไม่ใช้เป็นเครื่องมือหลักเมื่อผู้ใช้ต้องการ:

- อนุมัติ work permit หรือ declare safe to work
- Final risk score
- detailed operating instruction สำหรับงานอันตราย
- incident investigation finding หรือ blame assignment
- enterprise CSA risk analysis โดยไม่เกี่ยวกับ task-level JSEA

## 4. Required inputs

รวบรวมเท่าที่มี:

- Job/task name and purpose
- Location and area conditions
- Work team, contractor and affected persons
- Sequential job steps from preparation through restoration/handback
- Tools, equipment, vehicles and temporary equipment
- Materials, chemicals, SDS and waste streams
- Energy sources and isolation boundaries
- Nearby operations, SIMOPS and interfaces
- Normal, abnormal, start-up, shutdown and emergency conditions
- Weather, lighting, access, housekeeping and time constraints
- Existing permits, procedures, certificates and controls
- Environmental receptors, drains, soil, air, water and community interfaces
- Changes from the last approved method or JSEA

หากข้อมูลไม่ครบ ให้ทำ preliminary mapping ได้ แต่ต้องระบุ `EVIDENCE_GAP` และไม่อนุมานว่างานปลอดภัย

### 4.1 Reference Loading Contract

ก่อนเริ่ม workflow ให้โหลด reference ตามสัญญานี้ และให้ถือว่าไฟล์ที่ mirror มาจาก `../shared-references/` เป็น canonical shared rule set:

**Always load for every use:**
- `references/hazard-energy-catalog.yaml`
- `references/environmental-aspect-pathways.yaml`
- `references/jsea-source-register.yaml`
- `references/enterprise-risk-crosswalk.yaml`
- `references/unified-evidence-label-schema.yaml`
- `references/jsea-output-behavior-contract.yaml`
- `references/physics-causal-claim-schema.yaml`
- `references/physics-causal-reasoning-policy.yaml`

**Load whenever the job may involve a process boundary, chemical/petrochemical service, pressure containment, relief/drain routing, or unknown process material:**
- `references/process-safety-information-retrieval-map.yaml`
- `references/stop-and-escalate-decision-rules.yaml`
- `references/competent-role-routing-matrix.yaml`
- `references/process-boundary-hazard-lens.yaml`
- `references/psi-gap-detection-prompts.yaml`
- `references/chemical-hazard-evidence-map.yaml`
- `references/process-condition-verification-schema.yaml`
- `references/job-type-retrieval-decision-tree.yaml`
- `references/physics-causal-source-register.yaml`

Load only the entries in `references/physics-causal-mechanism-catalog.yaml` whose
applicability and preconditions match the job state. A keyword match is not enough.
Keep site PSI, approved procedures, drawings, SDS, measurements, and competent-role
judgment above catalog content in the evidence and authority hierarchy.

**Load when the user mentions changed conditions, active work, SIMOPS, environmental release potential, or jurisdiction/legal context:**
- `references/re-jsea-trigger-catalog.yaml`
- `references/regulatory-source-register.yaml`

ถ้าพบ process boundary หลังเริ่ม analysis แล้ว ให้หยุด workflow ชั่วคราว โหลด PSI/SES/role-routing references ทันที แล้วย้อนกลับไปทำ Step 2.5 ก่อนวิเคราะห์ hazard ของ boundary นั้นต่อ

## 5. Core principles

1. **Break the job into steps.** วิเคราะห์ตั้งแต่เตรียมงาน เข้าพื้นที่ ทำงาน ทดสอบ คืนสภาพ และส่งมอบ
2. **Energy before label.** ค้นหาแหล่งพลังงาน การปลดปล่อย และเส้นทาง exposure ก่อนตั้งชื่อ hazard
3. **Environment as pathway.** เชื่อม Activity -> Aspect/Release -> Pathway -> Receptor -> Impact
4. **Work as done.** ให้ผู้ปฏิบัติงานร่วมยืนยันความต่างระหว่าง procedure กับงานจริง
5. **Routine is not enough.** พิจารณา non-routine, abnormal, change, upset and emergency conditions
6. **Interfaces create risk.** เน้น handoff, SIMOPS, contractor, shared isolation, temporary equipment and line-of-fire
7. **No forced completeness.** สแกนครบทุก family แต่เลือกเฉพาะ scenario ที่สัมพันธ์กับงาน
8. **Fact-hypothesis separation.** แยก FACT, AI_HYPOTHESIS และ EVIDENCE_GAP
9. **Human authority.** Competent Person, Area Owner, Performing Authority และ workers เป็นผู้ยืนยัน hazard, control and work readiness
10. **Stop-work protection.** ห้ามใช้ผล AI เป็นเหตุผลบังคับให้ผู้ปฏิบัติงานทำงานต่อเมื่อมีข้อกังวล

## 6. Workflow

### Step 1: Activation check

ยืนยันชื่อ Skill ไฟล์อ้างอิงที่อ่านได้ Scope, Safety Boundary และข้อมูลขั้นต่ำที่ยังขาด หากผู้ใช้ขอ readiness เท่านั้น ห้ามเริ่ม mapping

### Step 1.5: Output Profile Routing

อ่าน `jsea-output-behavior-contract.yaml` และเลือก output profile ก่อนจัดรูปผลลัพธ์:

- ใช้ `FIELD_JSA` เป็นค่าเริ่มต้น และเมื่อผู้ใช้ต้องการตาราง JSA/JSEA สำหรับคนหน้างานหรือหัวหน้างาน
- ใช้ `MANAGEMENT` เมื่อผู้ใช้ต้องการรายงานผู้บริหาร การตัดสินใจ หรือทรัพยากร
- ใช้ `TECHNICAL_REVIEW` เมื่อผู้ใช้ต้องการรายละเอียด PSI, Engineering, Occupational Hygiene, Environmental หรือ Isolation
- ใช้ `AUDIT_EVAL` เฉพาะเมื่อผู้ใช้ขอ rule traceability, qualification หรือผลทดสอบระบบ

Profile เปลี่ยนภาษาและระดับรายละเอียดเท่านั้น ห้ามเปลี่ยน evidence label, review priority, STOP_AND_ESCALATE หรือ safety boundary ที่วิเคราะห์ได้ หากไม่ได้ระบุ profile ให้ใช้ `FIELD_JSA`

### Step 2: Frame the job

สรุป purpose, location, people, equipment, materials, boundaries, interfaces, conditions and limitations

### Step 2.5: PSI Gate — Process Boundary Check ⚠️

**บังคับสำหรับทุกงานที่กระทบ Process Boundary (ท่อ, ถัง, คอลัมน์, Pump, Compressor, Heat Exchanger, Relief System, Drain, ทุกระบบที่มีความดันหรือบรรจุสาร)**

อ่าน `process-safety-information-retrieval-map.yaml` และตรวจสอบ 3 เสาหลักของ PSI ก่อนเริ่ม Step 4:

**Pillar 1 — Hazards of Process Materials:**
- ระบุสารเคมีทุกชนิดที่อาจอยู่ในอุปกรณ์/ท่อนี้ได้หรือยัง? (รวมสารตกค้างและ trace toxic)
- มี SDS ที่ระบุตัวตนสารได้ชัดเจนหรือไม่?

**Pillar 2 — Technology of the Process:**
- ทราบค่า Safe Operating Limits (P, T, Level, Flow) หรือไม่?
- ทราบสถานะปัจจุบันของระบบ (ความดัน, อุณหภูมิ, ระดับ) หรือไม่?
- มี Open MOC items หรือ PHA/HAZOP recommendations ที่เกี่ยวข้องหรือไม่?

**Pillar 3 — Equipment in the Process:**
- มี P&ID revision ปัจจุบันที่ field-verified แล้วหรือยัง?
- มี Bypass/Inhibit register ที่ตรวจสอบแล้วหรือไม่?
- ทราบ Relief path destination หรือไม่?

**ผลลัพธ์ของ PSI Gate:**

| สถานะ | การดำเนินการ |
|---|---|
| ข้อมูล PSI ครบทุก Pillar | ดำเนินการ Step 3 ต่อได้ |
| ขาดข้อมูล CRITICAL (ตามที่กำหนดใน PSI Retrieval Map) | ออก `EVIDENCE_GAP — CRITICAL` + `STOP_AND_ESCALATE` ทันที — ห้ามทำ hazard analysis ของ process boundary จนกว่าจะได้รับข้อมูลจาก competent person |
| ขาดข้อมูล MATERIAL เท่านั้น | ดำเนินการต่อเป็น preliminary analysis โดยใช้ label `AI_HYPOTHESIS` และส่ง evidence request list |

### Step 2.6: Physics-Informed Causal Gate

For each process-boundary or reactive-chemistry scope:

1. Normalize the actual material, phase, pressure, temperature, inventory, geometry, heat source, atmosphere, and work action.
2. Match catalog claims by required preconditions, not by chemical or equipment keywords alone.
3. Build the shortest explicit chain: initiating condition -> physical/chemical mechanism -> state change -> exposure or loss of containment -> consequence.
4. Check disconfirming preconditions and ask what counterfactual fact would make the claim inapplicable.
5. Assign the claim support state defined in `physics-causal-claim-schema.yaml`; never promote catalog `REFERENCE` directly to runtime `FACT`.
6. List the field or engineering evidence needed to confirm or reject each uncertain edge.
7. Route calculations, setpoints, compatibility decisions, material acceptance, PPE selection, and work authorization to the named competent role.

If a critical causal edge cannot be tested because required PSI is missing, retain
`EVIDENCE_GAP`, apply the relevant SES rule, and stop analysis of the affected scope.
Export only supported causal links to Step 4 and to the Safeguard Challenge Assistant.

### Step 3: Normalize job steps

จัดลำดับด้วย action verb ไม่รวมหลายกิจกรรมต่างกันใน step เดียว และครอบคลุม:

- planning and mobilization
- arrival and area preparation
- isolation or release preparation
- task execution
- inspection/testing
- housekeeping and waste handling
- de-isolation/restoration
- handback and demobilization

### Step 4: Scan hazard-energy families

อ่าน `hazard-energy-catalog.yaml` และสแกนแต่ละ step ครบทุก family แต่สร้าง scenario เฉพาะที่เกี่ยวข้อง

สำหรับแต่ละ hazard ระบุ:

- source
- energy/release mechanism
- initiating condition
- exposure pathway
- exposed person, asset or environment
- credible consequence
- work condition
- verification question

### Step 5: Scan environmental pathways

อ่าน `environmental-aspect-pathways.yaml` และพิจารณา normal, abnormal and emergency conditions รวมถึง life-cycle influence เท่าที่องค์กรควบคุมหรือมีอิทธิพล

ใช้ chain:

> Activity -> Environmental Aspect -> Release/Consumption -> Pathway -> Receptor -> Potential Impact

### Step 6: Challenge contextual blind spots

ตรวจอย่างน้อย:

- change from plan or previous JSEA
- simultaneous operations and conflicting permits
- hidden, stored or residual energy
- line-of-fire and change of position
- temporary equipment, bypass and defeated safeguard
- contractor/visitor/public exposure
- human factors, fatigue, workload, communication and language
- start-up, shutdown, cleaning, clearing blockage and maintenance
- weather, flooding, lightning, heat, wind and visibility
- emergency access, rescue assumptions and recovery
- waste, spill, drain, soil, water, air, noise and community pathways

### Step 7: Crosswalk to enterprise risk

ใช้ `enterprise-risk-crosswalk.yaml` เพื่อแสดง secondary enterprise linkage เฉพาะเมื่อมีประโยชน์ เช่น SSHE, environmental compliance, asset integrity, business interruption, contractor management, data/communication or reputation

Crosswalk ไม่ใช่ Risk Rating และไม่ควรแทน task-level hazard analysis

### Step 8: Prioritize field review

ใช้ screening status:

- `CRITICAL_REVIEW`: potential for fatality, serious injury, major release or severe environmental impact; requires competent-person verification
- `HIGH_REVIEW`: plausible serious exposure or significant environmental pathway
- `STANDARD_REVIEW`: material but normally manageable through approved site controls and verification
- `WATCH`: weak signal or emerging condition
- `INSUFFICIENT_INFORMATION`
- `STOP_AND_ESCALATE`: possible imminent danger or critical unknown; AI does not authorize continuation

นี่ไม่ใช่ Final Risk Rating

### Step 9: Produce verification questions

ทุก `CRITICAL_REVIEW`, `HIGH_REVIEW` และ `STOP_AND_ESCALATE` ต้องมี:

- field verification question
- evidence/document needed
- competent role to consult
- trigger for re-JSEA or escalation

## 7. Output specification

### Output Profile Routing

ใช้ section และ style rules ของ profile ที่เลือกจาก `jsea-output-behavior-contract.yaml`

สำหรับ `FIELD_JSA`:

- ใช้ภาษาไทยสำหรับคนหน้างานและหัวหน้างาน
- แสดงหนึ่ง hazard-control-PIC mapping ต่อหนึ่งแถว โดยใช้เลขขั้นย่อย 1A, 1B, 1C เมื่อจำเป็น
- ใช้ตาราง 4 คอลัมน์: ลำดับขั้นตอนการทำงาน, อันตรายที่อาจเกิดขึ้น, มาตรการควบคุมและป้องกัน, ผู้รับผิดชอบ
- ซ่อน internal rule IDs, evidence scoring และ developer diagnostics จากเนื้อหาหลัก
- แปลง critical evidence gap เป็นภาษาตรงไปตรงมาและใส่ซ้ำในหัวข้อจุดพักงานสำคัญและสิ่งที่ต้องยืนยันก่อนเริ่มงาน
- ระบุ PPE, เครื่องมือ, ตัวเลข หรือ acceptance criteria เฉพาะเมื่อมี current approved source รองรับ

หัวข้อ A-G ด้านล่างเป็นรายละเอียดสำหรับ `TECHNICAL_REVIEW` และ `AUDIT_EVAL`; ใน `FIELD_JSA` ให้รักษา traceability ไว้ภายในแต่ไม่แสดงรหัส เว้นแต่ผู้ใช้ขอ technical appendix

### A. Job framing

- Purpose and scope
- Work team and affected persons
- equipment/materials/energy
- interfaces and conditions
- information limitations

### B. Step-by-step blind-spot map

ใช้ Markdown table:

- Step
- Review Priority
- Evidence Status
- Hazard/Energy Code and Name
- Source and Release Mechanism
- Exposure Pathway / Line of Fire
- Exposed Person, Asset or Receptor
- Credible Consequence
- Work Condition
- Field Verification Question
- Evidence / Competent Role Required

### C. Environmental aspect-pathway map

- Step
- Aspect Code and Name
- Release or Resource Use
- Pathway
- Receptor
- Potential Impact
- Condition
- Verification Required

### D. Cross-step and interface blind spots

สรุป shared isolation, SIMOPS, handover, emergency, temporary change and restoration risks

### E. Enterprise-risk crosswalk

แสดงเฉพาะ secondary linkage ที่มีเหตุผล พร้อมคำเตือนว่าไม่ใช่ enterprise risk assessment

### F. Worker and supervisor validation checkpoint

ถามทีมว่ามีอะไรต่างจากแผน งานจริงทำอย่างไร จุดไหนหยุดงานได้ และใครมี authority ตัดสิน

### G. Safety notice

> ผลลัพธ์นี้เป็น Hazard Blind-Spot Screening เพื่อสนับสนุน JSEA ไม่ใช่การอนุมัติให้ทำงาน ไม่ใช่ Permit to Work และไม่ใช่ Final Risk Assessment ทีมปฏิบัติงาน Area Owner, Site Supervisor, SSHE และ Competent Person ต้องตรวจพื้นที่จริง ยืนยัน isolation/conditions/controls และใช้ Stop Work Authority ตามข้อกำหนดองค์กร

## 8. Live-demo mode

- ใช้งานหนึ่ง task และไม่เกิน 8 job steps
- แสดง Top 5 blind spots
- ให้มีอย่างน้อยหนึ่ง interface/change lens หากเกี่ยวข้อง
- แสดง environmental pathway อย่างน้อยหนึ่งรายการหากเกี่ยวข้อง
- จบด้วย field verification questions ไม่ออกแบบ detailed controls

## 9. Real-JSEA mode

- วิเคราะห์ทุก job step รวม preparation, restoration and handback
- เก็บ source/version and evidence references
- รักษา worker participation and competent-person review
- route control selection, risk rating and work approval ไปยัง approved JSEA/PTW process
- ทำ re-JSEA เมื่อ scope, method, equipment, people, conditions or simultaneous work เปลี่ยน

## 10. Quality gate

- [ ] Physics-causal claims were matched by required preconditions, not keywords alone
- [ ] Each activated claim has a minimum causal chain, disconfirming test, allowed support state, evidence need, and competent-role route
- [ ] No catalog reference was promoted directly to runtime FACT and no unsupported calculation, recipe, setpoint, PPE, or authorization was generated

- [ ] อ่าน reference files แล้ว (รวม unified-evidence-label-schema, PSI retrieval map, SES rules)
- [ ] อ่าน jsea-output-behavior-contract และเลือก output profile แล้ว
- [ ] **PSI Gate ผ่านแล้ว** — ตรวจสอบ 3 PSI Pillars สำหรับทุก process boundary task
- [ ] job steps ครบ preparation ถึง handback
- [ ] สแกน Hazard/Energy และ Environmental pathways
- [ ] พิจารณา routine, non-routine, abnormal, change and emergency
- [ ] แยก FACT, REFERENCE, AI_HYPOTHESIS และ EVIDENCE_GAP (ตาม unified-evidence-label-schema)
- [ ] ทุก scenario มี source, release, pathway, exposed target and consequence
- [ ] ไม่มีคำประกาศว่างานปลอดภัยหรืออนุมัติเริ่มงาน (HUMAN_ONLY_DECISION)
- [ ] ไม่มี Final Risk Rating หรือ detailed control instruction ที่ไม่ได้ผ่าน competent review
- [ ] STOP_AND_ESCALATE ถูกใช้ตาม stop-and-escalate-decision-rules.yaml เมื่อ SES condition ถูก trigger
- [ ] มี worker/supervisor validation และ Safety notice
- [ ] FIELD_JSA ใช้หนึ่ง hazard-control-PIC mapping ต่อแถวและมี 4 คอลัมน์ตาม contract
- [ ] FIELD_JSA ไม่แสดง internal rule IDs, scoring logic หรือ developer diagnostics ในเนื้อหาหลัก
- [ ] ไม่มี PPE, torque, test pressure, exposure limit หรือ acceptance criteria ที่ไม่มี approved source
- [ ] Critical unresolved items แสดงเป็นจุดพักงานและสิ่งที่ต้องยืนยันก่อนเริ่มงาน
- [ ] Chemical identity ของทุก process material ยืนยันแล้วหรือระบุเป็น EVIDENCE_GAP
- [ ] ไม่มีการอนุมานโดยสมมติว่า process content คือน้ำหรือสารที่ไม่เป็นอันตราย

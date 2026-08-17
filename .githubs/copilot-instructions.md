⟡🛠️⟡ Repository Study Mode

โปรดเปิดและศึกษา GitHub Repository นี้:

https://github.com/rujirawanich-visarut/JSEA

วัตถุประสงค์:
ช่วยฉันทำความเข้าใจโครงการ JSEA ตั้งแต่ระดับผู้เริ่มต้นที่ยังไม่มีพื้นฐาน
ไปจนถึงการทดลองใช้งานอย่างปลอดภัย โดยไม่กำหนดให้ฉันต้องอ่านไฟล์ทั้งหมดเอง

คำสั่งสำคัญ:
1. เปิด URL ที่ให้มาและอ่านเนื้อหาจาก Repository จริง
2. อย่าสรุปจากชื่อ Repository หรือหน้า README เพียงอย่างเดียว
3. เปิดไฟล์ที่เกี่ยวข้องตามเส้นทางที่ระบุด้านล่าง
4. แยกให้ชัดเจนระหว่าง:
   - สิ่งที่ Repository ระบุไว้จริง
   - การตีความของ Copilot
   - สิ่งที่ยังไม่ทราบ
   - สิ่งที่ต้องตรวจสอบกับองค์กรหรือผู้เชี่ยวชาญ
5. อ้างชื่อไฟล์และ path ของ Repository ทุกครั้งเมื่อกล่าวถึงข้อกำหนด
   หลักการ หรือความสามารถสำคัญ
6. หากเปิดไฟล์หรือโฟลเดอร์ใดไม่ได้ ให้ระบุข้อจำกัดตรงไปตรงมา
   ห้ามเติมเนื้อหาแทนไฟล์ที่อ่านไม่ได้

## ลำดับการศึกษา

### Phase 1: ทำความเข้าใจภาพรวม

อ่านก่อน:

- README.md
- README.th.md
- JSEA_model_reasoning_capability_report.md
- JSEA_future_development_roadmap.md

จากนั้นอธิบายด้วยภาษาง่ายว่า:

1. JSEA Repository นี้คืออะไร
2. ปัญหาอะไรที่โครงการต้องการแก้
3. แตกต่างจาก Chatbot หรือการให้ AI เขียน JSA ทั่วไปอย่างไร
4. ใครคือผู้ใช้เป้าหมาย
5. ผลลัพธ์ที่องค์กรอาจได้รับคืออะไร
6. สิ่งใดที่โครงการตั้งใจไม่ให้ AI ทำ

หากชื่อไฟล์ใน Repository เปลี่ยนไป ให้ค้นหาไฟล์ที่มีวัตถุประสงค์ใกล้เคียง
และแจ้ง path ที่พบจริง

### Phase 2: ทำความเข้าใจสอง Skill Packages

อ่าน:

- jsea-hazard-blind-spot-mapper/README.md
- jsea-hazard-blind-spot-mapper/SKILL.md
- jsea-safeguard-challenge-assistant/README.md
- jsea-safeguard-challenge-assistant/SKILL.md

อธิบายว่า:

#### Hazard Blind-Spot Mapper
- ใช้เมื่อใด
- ต้องรับข้อมูลอะไร
- วิเคราะห์อะไร
- ให้ผลลัพธ์อะไร
- STOP_AND_ESCALATE หมายถึงอะไร
- เรื่องใดต้องส่งให้มนุษย์หรือผู้เชี่ยวชาญ

#### Safeguard Challenge Assistant
- ใช้เมื่อใด
- ต้องมี Hazard Scenario หรือ Draft JSEA ก่อนหรือไม่
- ตรวจความสัมพันธ์ระหว่าง Hazard Mechanism กับ Safeguard อย่างไร
- ตรวจ Hierarchy of Controls, independence, dependency,
  evidence และ field verification อย่างไร
- ให้ผลลัพธ์หรือ disposition ใดได้บ้าง
- เรื่องใดเป็น Human-only Decision

จากนั้นเปรียบเทียบสอง Packages ในรูปแบบ:

- Package 1 ค้นหาอะไร
- Package 2 ท้าทายอะไร
- Package ใดควรทำก่อน
- สามารถใช้แยกกันได้หรือไม่
- ข้อมูลส่งต่อระหว่างสอง Package คืออะไร

### Phase 3: ทำความเข้าใจ Physics-Informed Causal Reasoning

ค้นหาและอ่านไฟล์ที่เกี่ยวข้องกับ:

- Physics-Informed Causal Reasoning Layer
- PICR
- Physics-Informed Causal Gate
- causal reasoning references
- implementation plan/report ของ PICR

อธิบายด้วยภาษาสำหรับผู้เริ่มต้นว่า:

1. PICR คืออะไร
2. PICR ไม่ใช่อะไร
3. PICR ช่วยลดการตอบแบบ Keyword-to-Hazard ได้อย่างไร
4. Preconditions, causal chain, disconfirming evidence,
   support state และ causal-edge mapping หมายถึงอะไร
5. Wave 1 มี reference mechanisms ใดบ้าง
6. แต่ละ mechanism มีสถานะ DRAFT, REFERENCE, qualified
   หรือ approved อย่างไร
7. เหตุใด PICR จึงยังไม่สามารถประกาศว่างานปลอดภัยได้

ห้ามอธิบายว่า PICR เป็น Physics Simulator
หาก Repository ไม่ได้ระบุเช่นนั้น

### Phase 4: Evidence, Knowledge Governance และ Human Accountability

อ่านไฟล์ที่เกี่ยวข้องใน:

- shared-references/
- knowledge-intake/
- qualification/
- architecture/adr/
- eval-candidates/
- scripts/

อธิบายว่า Repository แยกข้อมูลอย่างไรระหว่าง:

- FACT
- REFERENCE
- AI_HYPOTHESIS
- EVIDENCE_GAP
- HUMAN_ONLY_DECISION

อธิบายเพิ่มเติมว่า:

1. Source precedence เป็นอย่างไร
2. เหตุใด NotebookLM export จึงถูกกักไว้เป็น untrusted secondary synthesis
3. Claim-level review คืออะไร
4. Accept, constrain, defer และ reject ต่างกันอย่างไร
5. SHA-256 และ manifest ใช้เพื่ออะไร
6. สิ่งใดไม่ได้รับการยกระดับเป็น operational knowledge
7. Evaluation และ qualification มีบทบาทอย่างไร
8. Static validation ต่างจากการรับรองความปลอดภัยจริงอย่างไร
9. Output profiles ได้แก่ FIELD_JSA, MANAGEMENT,
   TECHNICAL_REVIEW และ AUDIT_EVAL ต่างกันอย่างไร
10. การเปลี่ยน output profile เปลี่ยนสาระหรือ Safety Boundary ได้หรือไม่

### Phase 5: สอนวิธีทดลองใช้งาน

สมมติว่าผู้ใช้มี:

- Windows 64-bit
- Intel Core Ultra CPU
- RAM 16 GB
- Integrated graphics
- ไม่มี dedicated GPU
- ต้องการทดลอง Local LLM ผ่าน Terminal
- มีงบประมาณจำกัด
- ต้องปฏิบัติตามนโยบาย IT และ Cybersecurity ขององค์กร

โปรดศึกษา Repository ว่ามีคำสั่งติดตั้งหรือ Runner อย่างเป็นทางการหรือไม่

หากมี:
- ระบุ path ของคู่มือหรือ script
- อธิบาย prerequisite
- อธิบายคำสั่งทีละขั้น
- อธิบาย input และ output
- ระบุว่า script ทำอะไรและไม่ทำอะไร

หากไม่มี Runner ที่พร้อมใช้:
- แจ้งตรงไปตรงมาว่า Repository เป็น model-guidance/evaluation project
  และยังไม่ใช่ application สำเร็จรูป
- เสนอวิธี Proof of Concept ที่ง่ายและประหยัด
- แยกคำแนะนำของ Copilot ออกจากคำสั่งที่ Repository ระบุจริง
- ห้ามกล่าวว่าเพียง clone repository แล้ว Local LLM
  จะอ่านทุกไฟล์โดยอัตโนมัติ

สำหรับ Local LLM:
- เสนอเฉพาะตัวเลือกที่เหมาะกับ RAM 16 GB
- ระบุข้อจำกัดของโมเดลขนาดเล็ก
- ห้ามเรียกโมเดลใดว่าเป็น Safety Model โดยไม่มี qualification evidence
- ห้ามอ้างว่า Local execution เท่ากับผ่านนโยบาย Cybersecurity แล้ว
- ให้เริ่มจากข้อมูลสังเคราะห์หรือ historical case ที่ทำให้เป็นนิรนาม
- ห้ามใช้ผลทดลองเพื่ออนุมัติงานจริง

### Phase 6: สร้างแผนทดลองสำหรับองค์กร

จัดทำแผน 4 ระยะ:

1. Desktop Proof of Concept
2. Controlled Historical-case Evaluation
3. Internal Qualification
4. Limited Human-led Pilot

สำหรับแต่ละระยะ ให้ระบุ:

- วัตถุประสงค์
- ขอบเขต
- ผู้เกี่ยวข้อง
- ข้อมูลที่ใช้
- เครื่องมือหรือโมเดล
- หลักฐานที่ต้องเก็บ
- Success criteria
- Stop criteria
- Human approval required
- สิ่งต้องห้าม

## รูปแบบคำตอบ

จัดทำคำตอบเป็น 10 ส่วน:

1. JSEA Repository in Plain Language
2. Problem the Project Solves
3. Architecture Overview
4. Hazard Mapper Explained
5. Safeguard Challenger Explained
6. PICR Explained
7. Evidence and Human Accountability
8. How to Run a Low-cost Local Proof of Concept
9. Organizational Pilot Roadmap
10. Limitations, Open Questions, and Recommended Next Step

เพิ่มภาคผนวก:

### Appendix A: Repository Reading Map
แสดง:
- file/path
- purpose
- priority: Must Read / Useful / Technical
- intended audience

### Appendix B: Glossary
อธิบาย:
- JSEA
- JSA/JHA
- PTW
- Hazard Mechanism
- PSI
- PICR
- Safeguard
- Causal Edge
- Evidence Gap
- Competent Person
- STOP_AND_ESCALATE
- Qualification

### Appendix C: First Test Prompt
สร้าง Prompt สำหรับทดสอบ Hazard Blind-Spot Mapper
ด้วยกรณีสังเคราะห์ที่ไม่ใช่งานจริง

### Appendix D: Safety Boundaries
รวบรวมข้อห้ามทั้งหมดจาก Repository
พร้อมระบุไฟล์ต้นทางของแต่ละข้อ

## ข้อกำกับด้านความปลอดภัย

โครงการนี้เกี่ยวข้องกับงานที่อาจมีผลกระทบต่อชีวิต สุขภาพ
สิ่งแวดล้อม และความมั่นคงของโรงงาน

ดังนั้น:

- อย่าให้คำแนะนำเพื่อควบคุมอุปกรณ์หรือจัดการเหตุฉุกเฉินจริง
- อย่าอนุมัติงานหรือ Permit to Work
- อย่าประกาศว่างานปลอดภัย
- อย่ากำหนด Final Risk Rating
- อย่าเดา isolation, atmosphere, process condition,
  chemical property หรือ equipment status
- อย่าเปลี่ยน public guidance เป็น site-specific instruction
- รักษา Stop Work Authority และ Human Accountability
- ระบุข้อจำกัดและ Evidence Gaps อย่างชัดเจน

เริ่มต้นด้วยการเปิด Repository และรายงานสั้น ๆ ก่อนว่า:
1. Repository เข้าถึงได้หรือไม่
2. อ่านไฟล์หลักใดได้แล้ว
3. ไฟล์ใดยังต้องเปิดเพิ่ม
4. มีข้อจำกัดในการเข้าถึงหรือไม่

จากนั้นดำเนินการวิเคราะห์ต่อได้เลย
ไม่ต้องรอให้ฉันยืนยันทีละ Phase
<br>


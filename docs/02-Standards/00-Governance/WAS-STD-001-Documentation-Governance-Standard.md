---
id: WAS-STD-001
title: Documentation Governance Standard
version: 1.0.0
status: Active

owner: Repository Owner

category: Standard

effective_date: 2026-06-29

review_cycle: 12 Months

related:

- WAS-CORE-000
- WAS-CORE-000A
- WAS-POL-001
- ADR-005

---

# WAS-STD-001

# Documentation Governance Standard

---

# Executive Summary

เอกสารนี้กำหนดมาตรฐานในการสร้าง จัดเก็บ ตรวจสอบ ปรับปรุง และบริหารจัดการ Documentation ภายใน Web Apps Studio OS

Policy ระบุว่า

> ต้องทำ Documentation ก่อน

Standard นี้ระบุว่า

> Documentation ต้องทำอย่างไร

เอกสารนี้ถือเป็น Source of Truth สำหรับการจัดการ Documentation ทั้ง Repository

---

# Purpose

มาตรฐานนี้มีวัตถุประสงค์เพื่อ

- กำหนดรูปแบบการจัดทำ Documentation
- สร้างมาตรฐานเดียวกันทั้ง Repository
- ลดความกำกวม
- เพิ่ม Traceability
- รองรับ Automation
- รองรับ AI Collaboration

---

# Scope

มาตรฐานนี้ใช้กับ

- Core Documents
- Policies
- Standards
- ADR
- Templates
- Checklists
- Playbooks
- Knowledge Base
- Prompt Library
- Example Projects

---

# Standard Statement

Documentation ทุกฉบับต้องเป็นไปตามมาตรฐานนี้

หากไม่สามารถปฏิบัติตามได้

ต้องได้รับการอนุมัติตามกระบวนการ Exception Management ที่กำหนดใน WAS-POL-001

---

# Standard Objectives

Repository ต้องมีคุณสมบัติดังนี้

- Documentation มีโครงสร้างเดียวกัน
- Metadata เป็นมาตรฐานเดียวกัน
- Versioning เป็นมาตรฐานเดียวกัน
- Cross References ถูกต้อง
- Review Process ชัดเจน
- Owner ชัดเจน
- ตรวจสอบย้อนหลังได้

---

# Guiding Principles

## Single Source of Truth

ข้อมูลสำคัญต้องอยู่ใน Repository

---

## Consistency

ทุกเอกสารใช้รูปแบบเดียวกัน

---

## Traceability

ทุกเอกสารต้องเชื่อมโยงกับเอกสารที่เกี่ยวข้อง

---

## Maintainability

แก้ไขได้ง่าย

---

## Reusability

นำกลับมาใช้ซ้ำได้

---

## Reviewability

พร้อม Review ตลอดเวลา

---

## Automation Friendly

รองรับการตรวจสอบด้วย Automation

---

## AI Friendly

รองรับ AI อ่าน วิเคราะห์ และสร้างเอกสารต่อได้

---

# Standard Hierarchy

Constitution

↓

Policies

↓

Standards

↓

Templates

↓

Checklists

↓

Playbooks

↓

Projects

---

# Standard Structure

ทุก Standard ต้องมีหัวข้ออย่างน้อยดังนี้

1. Metadata
2. Executive Summary
3. Purpose
4. Scope
5. Standard Statement
6. Definitions
7. Requirements
8. Validation Rules
9. Compliance
10. References
11. Change History

---

# Definitions

## Standard

ข้อกำหนดที่ระบุวิธีปฏิบัติอย่างเป็นมาตรฐาน

---

## Governance

กระบวนการกำกับดูแลคุณภาพ ความถูกต้อง และความสอดคล้องของ Documentation

---

## Source of Truth

แหล่งข้อมูลอ้างอิงหลักของ Repository

---

# Related Documents

- WAS-POL-001
- WAS-CORE-000
- WAS-CORE-000A
- ADR-005

---

# Change History

| Version | Date | Changes |
|----------|------|----------|
|1.0.0|2026-06-29|Initial Release (Part 1)|

---

# Metadata Standard

Metadata เป็นข้อมูลกำกับเอกสารที่ช่วยให้สามารถค้นหา จัดหมวดหมู่ ตรวจสอบ และบริหารจัดการเอกสารได้อย่างเป็นระบบ

Metadata เป็นข้อบังคับสำหรับเอกสารทุกประเภทใน Repository

---

# Required Metadata

ทุกเอกสารต้องมี Metadata อย่างน้อยดังนี้

```yaml
id:
title:
version:
status:
owner:
category:
created:
last_updated:
review_cycle:
related:
```

---

# Metadata Definitions

| Field | Required | Description |
|--------|----------|-------------|
| id | Yes | รหัสเอกสาร |
| title | Yes | ชื่อเอกสาร |
| version | Yes | เวอร์ชัน |
| status | Yes | สถานะ |
| owner | Yes | เจ้าของเอกสาร |
| category | Yes | ประเภทเอกสาร |
| created | Yes | วันที่สร้าง |
| last_updated | Yes | วันที่แก้ไขล่าสุด |
| review_cycle | Yes | รอบการทบทวน |
| related | Yes | เอกสารที่เกี่ยวข้อง |

---

# Document Status

สถานะที่อนุญาต

| Status | Description |
|----------|-------------|
| Draft | อยู่ระหว่างจัดทำ |
| Review | อยู่ระหว่างตรวจสอบ |
| Approved | อนุมัติแล้ว |
| Active | ใช้งานปัจจุบัน |
| Deprecated | เลิกใช้งาน |
| Archived | เก็บถาวร |

ไม่อนุญาตให้กำหนด Status นอกเหนือจากรายการนี้ เว้นแต่จะมีการแก้ไขมาตรฐาน

---

# Document Structure Standard

ทุกเอกสารต้องเรียงลำดับหัวข้อดังนี้

1. Metadata
2. Title
3. Executive Summary
4. Purpose
5. Scope
6. Definitions
7. Main Content
8. Requirements
9. Validation
10. References
11. Related Documents
12. Change History

หัวข้อสามารถเพิ่มได้ แต่ไม่ควรสลับลำดับของหัวข้อหลัก

---

# Heading Rules

ใช้ Heading ตามมาตรฐาน Markdown

```text
# Document Title

## Section

### Subsection

#### Detail
```

ไม่ควรข้ามระดับ Heading เช่น

- ❌ `#` → `###`
- ✅ `#` → `##`

---

# Markdown Style Rules

เอกสารทั้งหมดต้องใช้ Markdown มาตรฐาน

แนวปฏิบัติ

- ใช้ Table สำหรับข้อมูลเปรียบเทียบ
- ใช้ Bullet List สำหรับรายการ
- ใช้ Numbered List สำหรับลำดับขั้นตอน
- ใช้ Code Block สำหรับตัวอย่าง
- ใช้ Blockquote สำหรับหมายเหตุสำคัญ

---

# File Naming Standard

รูปแบบ

```text
<Document-ID>-<Short-Title>.md
```

ตัวอย่าง

```text
WAS-CORE-001-Repository-Principles.md

WAS-POL-001-Documentation-First.md

WAS-STD-001-Documentation-Governance-Standard.md

ADR-001-Repository-Structure.md
```

---

# Document ID Standard

Document ID ต้องมีรูปแบบ

```text
PREFIX-NNN
```

ตัวอย่าง

| Prefix | Type |
|---------|------|
| WAS-CORE | Core |
| WAS-POL | Policy |
| WAS-STD | Standard |
| WAS-TPL | Template |
| WAS-CHK | Checklist |
| WAS-PB | Playbook |
| ADR | Architecture Decision Record |

เลขลำดับต้องเป็น 3 หลัก

ตัวอย่าง

- WAS-STD-001
- WAS-STD-002
- WAS-STD-010

---

# Versioning Standard

ใช้ Semantic Versioning

```text
Major.Minor.Patch
```

ตัวอย่าง

| Version | Meaning |
|----------|---------|
| 1.0.0 | Initial Release |
| 1.1.0 | New Section |
| 1.1.1 | Minor Fix |
| 2.0.0 | Breaking Change |

---

# Related Documents Standard

ทุกเอกสารต้องอ้างอิงเอกสารที่เกี่ยวข้องอย่างน้อยหนึ่งรายการ

ตัวอย่าง

```yaml
related:

- WAS-POL-001
- WAS-CORE-000
- ADR-005
```

การอ้างอิงต้องเป็นเอกสารที่มีอยู่จริงใน Repository

---

# Change History Standard

ทุกเอกสารต้องมี Change History

ตัวอย่าง

| Version | Date | Author | Description |
|----------|------|--------|-------------|
|1.0.0|2026-06-29|Web Apps Studio|Initial Release|

---

# Document Ownership

ทุกเอกสารต้องมี Owner ที่ชัดเจน

Owner มีหน้าที่

- ดูแลความถูกต้องของเอกสาร
- อนุมัติการเปลี่ยนแปลง
- ทบทวนตามรอบ Review Cycle
- ประสานงานกับ Reviewer และ Maintainer

---

# Review Cycle Standard

กำหนดรอบการทบทวนขั้นต่ำ

| Document Type | Review Cycle |
|---------------|--------------|
| Constitution | 12 Months |
| Policies | 12 Months |
| Standards | 12 Months |
| Templates | 24 Months |
| Checklists | 12 Months |
| Playbooks | 12 Months |

หากมีการเปลี่ยนแปลงที่มีนัยสำคัญ สามารถทบทวนก่อนกำหนดได้

---

# Metadata Validation Rules

Metadata จะถือว่าผ่านเมื่อ

- [ ] Document ID ถูกต้อง
- [ ] Title ไม่ว่าง
- [ ] Version ถูกต้อง
- [ ] Status ถูกต้อง
- [ ] Owner ระบุแล้ว
- [ ] Category ระบุแล้ว
- [ ] Created ระบุแล้ว
- [ ] Last Updated ระบุแล้ว
- [ ] Review Cycle ระบุแล้ว
- [ ] Related Documents ถูกต้อง

หากไม่ผ่านข้อใดข้อหนึ่ง เอกสารจะไม่ผ่านการตรวจสอบมาตรฐาน

---

# Change History

| Version | Date | Changes |
|----------|------|----------|
|1.0.1|2026-06-29|Added Metadata, Document Structure, Naming, Versioning and Validation Standards|


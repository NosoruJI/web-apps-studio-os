---
id: ADR-001
title: Repository Structure
status: Accepted
date: 2026-06-29
version: 1.0.0

owner: Web Apps Studio

category: Architecture Decision

deciders:
  - Repository Owner

reviewers: []

related:
  - WAS-CORE-000
  - WAS-CORE-001
  - REGISTRY.md
  - ARCHITECTURE.md

supersedes: null

superseded_by: null

tags:
  - repository
  - architecture
  - documentation
---

# ADR-001 — Repository Structure

---

# Executive Summary

Web Apps Studio OS จะใช้โครงสร้าง Repository แบบ **Modular Documentation Architecture** โดยแบ่งเอกสารออกเป็นหมวดหมู่ตามหน้าที่ แทนการเก็บเอกสารทั้งหมดไว้ในโฟลเดอร์เดียว

การตัดสินใจนี้มีเป้าหมายเพื่อให้ Repository รองรับการขยายตัวในระยะยาว ลดความซับซ้อนในการค้นหา และทำให้ผู้เชี่ยวชาญแต่ละบทบาทสามารถทำงานร่วมกันได้อย่างเป็นระบบ

---

# Status

**Accepted**

---

# Context

Web Apps Studio OS ถูกออกแบบให้เป็น Engineering Knowledge Operating System ไม่ใช่เพียงชุด Prompt หรือชุดเอกสารทั่วไป

เมื่อจำนวนเอกสารเพิ่มขึ้นเป็นหลักร้อยหรือหลักพันไฟล์ หากไม่มีโครงสร้างที่ชัดเจน จะเกิดปัญหา เช่น

- ค้นหาเอกสารยาก
- เอกสารซ้ำซ้อน
- ไม่มีมาตรฐานการจัดเก็บ
- ขยายระบบลำบาก
- AI วิเคราะห์ความสัมพันธ์ของเอกสารได้ยาก

จึงจำเป็นต้องกำหนดโครงสร้าง Repository ตั้งแต่เริ่มต้น

---

# Problem Statement

Repository ต้องสามารถ

- รองรับเอกสารจำนวนมาก
- รองรับหลาย Module
- รองรับหลาย Expert
- ค้นหาได้ง่าย
- มีมาตรฐานเดียวกัน
- ขยายในอนาคตได้โดยไม่ต้องปรับโครงสร้างใหม่

---

# Decision

เลือกใช้ **Modular Repository Structure**

```text
Web-Apps-Studio/

README.md
ROADMAP.md
ARCHITECTURE.md
REGISTRY.md
MANIFEST.yaml
CATALOG.md

docs/

00-Core/

01-Experts/

02-Standards/

03-Templates/

04-Checklists/

05-Playbooks/

06-Knowledge/

07-Orchestration/

08-Prompt-Library/

09-Reference-Architecture/

10-Example-Projects/

ADR/
```

Repository จะถูกแบ่งตาม "ความรับผิดชอบ (Responsibility)" ไม่ใช่แบ่งตามผู้เขียนหรือช่วงเวลา

---

# Decision Drivers

ปัจจัยที่ใช้ในการตัดสินใจ

- Scalability
- Maintainability
- Discoverability
- Reusability
- AI Readiness
- Enterprise Standards
- Separation of Concerns

---

# Alternatives Considered

## Option 1 — Flat Repository

```
docs/
ทุกไฟล์อยู่รวมกัน
```

### ข้อดี

- เริ่มต้นง่าย
- ไม่ต้องสร้างหลายโฟลเดอร์

### ข้อเสีย

- ค้นหายาก
- ขยายไม่ได้
- เกิดไฟล์ซ้ำง่าย

**ไม่เลือก**

---

## Option 2 — Modular Repository (Selected)

แบ่งตาม Module

### ข้อดี

- Scale ได้
- ค้นหาง่าย
- รองรับ Automation
- รองรับ AI
- ดูแลรักษาง่าย

### ข้อเสีย

- ใช้เวลาวางโครงสร้างมากกว่าในช่วงแรก

**เลือกใช้**

---

## Option 3 — Repository แยกหลายตัว

Core Repository

Standards Repository

Prompt Repository

### ข้อดี

แยกอิสระ

### ข้อเสีย

- จัดการยาก
- Version ยาก
- Cross Reference ซับซ้อน

**ไม่เลือก**

---

# Consequences

## Positive

- Repository เป็นมาตรฐานเดียวกัน
- ลดการซ้ำซ้อน
- เพิ่มความสามารถในการค้นหา
- รองรับการสร้าง Documentation Website
- รองรับ AI Automation
- รองรับทีมขนาดใหญ่

## Negative

- ต้องกำหนดกฎในการสร้างเอกสาร
- ต้องมีการ Review โครงสร้างอย่างสม่ำเสมอ

---

# Risks

| Risk | Impact | Mitigation |
|------|--------|------------|
| สร้างเอกสารผิดโฟลเดอร์ | Medium | Documentation Standard |
| Module ซ้ำซ้อน | Medium | Review Process |
| Repository โตมาก | Low | Modular Architecture |

---

# Implementation Plan

1. สร้างโครงสร้างโฟลเดอร์มาตรฐาน
2. สร้าง Core Framework
3. สร้าง Standards
4. สร้าง Templates
5. สร้าง Expert Modules
6. อัปเดต REGISTRY.md
7. อัปเดต MANIFEST.yaml

---

# Validation

Architecture นี้ถือว่าสำเร็จเมื่อ

- ทุกเอกสารถูกจัดเก็บใน Module ที่ถูกต้อง
- ไม่มี Document ID ซ้ำ
- ทุกเอกสารถูกลงทะเบียนใน REGISTRY.md
- AI สามารถค้นหาเอกสารได้จากโครงสร้างเดียวกัน
- Repository รองรับการเพิ่มเอกสารโดยไม่ต้องเปลี่ยนโครงสร้างหลัก

---

# Related Documents

- WAS-CORE-000 Core Architecture
- WAS-CORE-001 Project Overview
- REGISTRY.md
- ARCHITECTURE.md

---

# Review

Reviewer:

Review Date:

Approved By:

Approval Date:

---

# Change History

| Version | Date | Author | Changes |
|----------|------|--------|----------|
| 1.0.0 | 2026-06-29 | Web Apps Studio | Initial Release |
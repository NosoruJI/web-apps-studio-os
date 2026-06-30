# Contributing to Web Apps Studio OS

Version: 1.0.0

Status: Active

Owner: Web Apps Studio

---

# Executive Summary

ขอบคุณที่ร่วมพัฒนา Web Apps Studio OS

Repository นี้ใช้มาตรฐานระดับ Enterprise สำหรับการจัดการเอกสาร ความรู้ และการพัฒนา Software Engineering Framework

ผู้ร่วมพัฒนาทุกคน (Human และ AI) ต้องปฏิบัติตามมาตรฐานในเอกสารนี้

---

# Core Principles

ทุกการเปลี่ยนแปลงต้องยึดหลัก

- Business First
- User First
- Documentation First
- Architecture First
- Security by Design
- Quality by Design
- Simplicity
- Reusability
- Maintainability
- Scalability

---

# Before You Start

ก่อนเพิ่มหรือแก้ไขเอกสาร

ตรวจสอบ

- REGISTRY.md
- MANIFEST.yaml
- CATALOG.md
- WAS-CORE-000
- WAS-STD-001

---

# Repository Structure

```

README.md
REGISTRY.md
ROADMAP.md
ARCHITECTURE.md
CHANGELOG.md
CONTRIBUTING.md

docs/

```

---

# Creating a New Document

ทุกเอกสารต้อง

- มี Document ID
- มี Version
- มี Status
- มี Owner
- มี Related Documents
- มี Change History

ห้ามสร้างไฟล์โดยไม่มี Metadata

---

# Naming Convention

รูปแบบ

```

WAS-CORE-001-Project-Overview.md

```

หรือ

```

WAS-STD-001-Documentation-Standard.md

```

ห้ามใช้

```

new.md

test.md

document.md

```

---

# Document Metadata

ทุกไฟล์ต้องมี YAML

ตัวอย่าง

```yaml
id:

title:

version:

status:

owner:

related:

created:

last_updated:
```

---

# Writing Standard

ใช้ Markdown

หัวข้อ

```
# H1

## H2

### H3
```

ใช้ตารางเมื่อเหมาะสม

ใช้ Checklist เมื่อเหมาะสม

ใช้ Code Block เมื่อเหมาะสม

---

# Updating Existing Documents

หากแก้ไขเอกสาร

ต้อง

- เพิ่ม Change History
- อัปเดต last_updated
- ตรวจสอบ Related Documents
- ตรวจสอบ REGISTRY

---

# ADR Rules

ทุกการตัดสินใจสำคัญ

ต้องสร้าง ADR

ตัวอย่าง

- เปลี่ยน Architecture

- เปลี่ยน Metadata

- เปลี่ยน Versioning

- เปลี่ยน Standards

---

# Commit Convention

ใช้ Conventional Commits

ตัวอย่าง

```

docs(core): add glossary

docs(adr): add ADR-002

docs(std): update metadata standard

feat(auth): add login

fix(api): resolve validation bug

refactor(core): simplify structure

```

---

# Pull Request Checklist

- [ ] Metadata ถูกต้อง

- [ ] Document ID ถูกต้อง

- [ ] Change History อัปเดต

- [ ] REGISTRY อัปเดต

- [ ] MANIFEST อัปเดต

- [ ] ไม่มี Document ID ซ้ำ

- [ ] ผ่าน Review

---

# Human Contribution

ผู้พัฒนาต้อง

- ตรวจสอบ Requirement

- ตรวจสอบมาตรฐาน

- ไม่สร้างข้อมูลซ้ำ

- อ้างอิงเอกสารเดิม

---

# AI Contribution

AI ต้อง

- ไม่เดา Requirement

- อ้างอิง Standards

- อ้างอิง Core Framework

- สร้าง Metadata

- เพิ่ม Change History

- ระบุ Assumptions

- ระบุ Risks

---

# Review Process

Draft

↓

Review

↓

Approved

↓

Merged

---

# Definition of Done

งานถือว่าเสร็จเมื่อ

- เอกสารถูกต้อง

- Metadata ครบ

- Standards ครบ

- Change History ครบ

- Review ผ่าน

- REGISTRY อัปเดต

- MANIFEST อัปเดต

---

# Related Documents

- README.md

- REGISTRY.md

- MANIFEST.yaml

- CHANGELOG.md

- WAS-CORE-000

- WAS-STD-001

---

# Maintainer

Web Apps Studio
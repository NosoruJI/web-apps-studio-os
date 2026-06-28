# 🤝 Contributing Guide

Welcome to **Web Apps Studio OS**.

This document defines the standards for contributing to this repository.

---

# Purpose

The goal of this project is to build a professional AI-powered Software Development Operating System.

Every document should follow the same structure, terminology, and quality standards.

---

# Repository Structure

```
docs/
├── 00-Core/
├── 01-Experts/
├── 02-Standards/
├── 03-Templates/
├── 04-Checklists/
├── 05-Playbooks/
├── 06-Knowledge/
├── 07-Orchestration/
├── 08-Prompt-Library/
├── 09-Reference-Architecture/
└── 10-Example-Projects/
```

---

# Branch Strategy

Never work directly on `main`.

Create a feature branch.

Example

```
feature/core-framework

feature/product-manager

feature/solution-architect

feature/templates

feature/checklists
```

---

# Commit Convention

Use Conventional Commits.

Examples

```
docs(core): add project overview

docs(pm): improve discovery guide

docs(sa): update architecture template

docs(qa): add testing checklist

feat(prompt): add orchestration rules

fix(core): correct terminology
```

---

# Naming Convention

Every document must use the following naming format.

```
WAS-CORE-001-Project-Overview.md

WAS-PM-001-Discovery.md

WAS-SA-001-System-Architecture.md

WAS-QA-001-Test-Strategy.md
```

---

# Document Metadata

Every document should begin with metadata.

Example

```yaml
ID:
Title:
Module:
Version:
Status:
Owner:
Audience:
Purpose:
Depends On:
Related:
Last Updated:
```

---

# Document Structure

All documents should follow this structure.

1. Executive Summary
2. Purpose
3. Scope
4. Inputs
5. Outputs
6. Workflow
7. Best Practices
8. Checklist
9. Examples
10. Handoff
11. Revision History

---

# Markdown Standards

Use

- Headings
- Tables
- Checklists
- Code blocks
- Mermaid diagrams (when appropriate)

Avoid

- Long paragraphs
- Inconsistent heading levels
- Mixing Thai and English in headings
- Unstructured notes

---

# Documentation Principles

Every document should be

- Clear
- Reusable
- Maintainable
- Versioned
- Easy to review
- Easy to hand off

---

# Review Checklist

Before submitting, verify

- [ ] Correct file name
- [ ] Correct folder
- [ ] Metadata completed
- [ ] Formatting consistent
- [ ] Grammar checked
- [ ] Links verified
- [ ] Cross references added
- [ ] Version updated

---

# Pull Request Checklist

Before merging

- [ ] Document reviewed
- [ ] Naming convention followed
- [ ] Markdown validated
- [ ] No duplicated content
- [ ] Links working
- [ ] Related documents updated

---

# Versioning

This repository follows Semantic Versioning.

```
MAJOR.MINOR.PATCH
```

Example

```
1.0.0

1.1.0

1.1.1

2.0.0
```

---

# Questions

If a requirement is unclear

Do **not** guess.

Instead

- Ask questions
- Validate assumptions
- Update documentation after confirmation

---

# Definition of Done

A contribution is complete when

- Documentation is accurate
- Standards are followed
- Links are updated
- Review is completed
- Ready for handoff
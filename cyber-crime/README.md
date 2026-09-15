# Cyber Crime — Operation Phantom Swipe

**Assignment 1 — Unit 1: Foundations of Digital Forensics**
Simulated investigation of a cross-border ATM skimming & credit card fraud
ring (Case No. OPS-2026-014).

> All data in this repository — card numbers, names, phone numbers, chat
> logs, GPS coordinates, and "victim" bank messages — is **synthetically
> generated for coursework purposes**. No real individuals, accounts, or
> devices are represented.

---

## Repository Structure

```
cyber-crime/
├── README.md                      # this file — execution guide, tools, authorship
├── docs/
│   ├── 01-cybercrime-taxonomy.md      # Sub-problem 1: classification & legal mapping
│   ├── 02-evidence-collection.md      # Sub-problem 2: chain of custody, hashing
│   ├── 03-media-analysis.md           # Sub-problem 3: search strategy, artefacts
│   └── 04-cryptography-component.md   # Sub-problem 4: cracking sim, ethics
├── report/
│   └── Operation-Phantom-Swipe-Legal-Technical-Report.docx  # Sub-problem 5
├── evidence/
│   ├── exhibit-A-skimmer/         # skimmer dump, tracks, config, photo log + photos/
│   ├── exhibit-B-phone/           # app manifest, SMS/chat logs, GPS, gallery/,
│   │                               #   and protected_evidence.zip (password-protected)
│   └── hashes/
│       └── sha256_hashlog.txt     # SHA-256 of all 16 acquired files
├── tools/
│   └── crack_zip.py               # dictionary-attack script used in Part 4
├── screenshots/                   # tool-usage screenshots (hashing, cracking, search)
└── .github/workflows/
    └── validate-structure.yml     # CI: validates repo structure on push/PR
```

---

## Execution Guide

### Clone
```bash
git clone https://github.com/<your-username>/cyber-crime.git
cd cyber-crime
```

### Prerequisites
- Python 3.8+ (standard library only for `crack_zip.py`)
- `sha256sum` (coreutils — preinstalled on Linux/macOS/WSL)

### 1. Reproduce the SHA-256 hash log
```bash
cd evidence
sha256sum exhibit-A-skimmer/*.csv exhibit-A-skimmer/*.txt exhibit-A-skimmer/*.bin \
  exhibit-A-skimmer/photos/*.jpg exhibit-B-phone/*.txt exhibit-B-phone/*.json \
  exhibit-B-phone/*.csv exhibit-B-phone/*.zip exhibit-B-phone/gallery/*.jpg
```
Compare against `hashes/sha256_hashlog.txt` (16 files total) — this is the
same integrity check performed at every custody transfer (see
`docs/02-evidence-collection.md` §2.4), and the same check the CI workflow
runs automatically on every push.

### 2. Reproduce the password-cracking simulation
```bash
cd evidence/exhibit-B-phone
python3 ../../tools/crack_zip.py protected_evidence.zip
```
Expected output:
```
[+] PASSWORD FOUND: 'sunshine1'
[+] Attempts: 21
[+] Time elapsed: ~0.002s
```
See `docs/04-cryptography-component.md` for the equivalent `zip2john` /
`john --wordlist` / `hashcat -m 17200` command-line workflow this script
substitutes for.

### 3. Read the write-up
Read `docs/01` → `docs/04` in order, then the consolidated
`report/Operation-Phantom-Swipe-Legal-Technical-Report.docx` for the final
legal-technical report (Sub-problem 5).

### 4. CI validation
`.github/workflows/validate-structure.yml` runs automatically on every push
and pull request. It checks that all required folders/files are present
and that no evidence file's SHA-256 hash has drifted from the recorded hash
log — i.e. it re-runs the same integrity check as step 1, as an automated
substitute for a human re-verifying custody at every commit.

---

## Tools Used

| Tool | Purpose |
|---|---|
| `sha256sum` (GNU coreutils) | Evidence integrity hashing (Part 2) |
| Python 3 (`zipfile`, `json`, `csv`) | Simulated evidence generation, dictionary-attack script (Part 4) |
| John the Ripper wordlist methodology | Reference approach for the dictionary attack (Part 4) |
| `docx` (docx-js, Node.js) | Generation of the formatted Legal-Technical Report (Part 5) |
| LibreOffice (`soffice`) / Poppler (`pdftoppm`) | Rendering the report to PDF/images for visual QA before submission |
| GitHub Actions | CI structure & hash-integrity validation (Part 6) |

Tool-usage screenshots are provided in `screenshots/`:
- `01-hash-generation.png` — SHA-256 hashing of all acquired files
- `02-password-crack.png` — dictionary attack recovering the archive password
- `03-string-search.png` — string search recovering the skimmer firmware marker

---

## Authorship Declaration

I declare that the analysis, scripts, simulated evidence, and report in
this repository were prepared by me for Assignment 1 (Unit 1: Foundations
of Digital Forensics), as an educational simulation. All "evidence" is
synthetic and was generated specifically for this exercise; no real
persons, devices, accounts, or financial data are involved.

**Name:** Pawan Yadav
**Roll No. / Student ID:** 2301730273
**Course:** B.Tech CSE (AI & ML), Section D
**Date:** 21-08-2026
**Signature:** Pawan Yadav

---

## Evaluation Cross-Reference

| Criterion (Marks) | Where addressed |
|---|---|
| Cybercrime taxonomy & legal mapping (1.5) | `docs/01-cybercrime-taxonomy.md` |
| Evidence acquisition + chain of custody (2.0) | `docs/02-evidence-collection.md`, `evidence/` |
| File/media analysis and artefact extraction (2.0) | `docs/03-media-analysis.md` |
| Cryptography simulation and discussion (1.5) | `docs/04-cryptography-component.md`, `tools/crack_zip.py` |
| Final legal-technical report quality (2.0) | `report/Operation-Phantom-Swipe-Legal-Technical-Report.docx` |
| GitHub structure, documentation, CI compliance (1.0) | This README, `.github/workflows/validate-structure.yml` |

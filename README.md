# 🩺 ReportSaathi: Rules Decide, AI Explains

[![Hackathon](https://img.shields.io/badge/Aayu%202026-DevAarambh-indigo.svg)](https://aayu.devaarambh.com)
[![Problem Statement](https://img.shields.io/badge/Problem%20ID-T02%20Report%20Decoded-emerald.svg)](#)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Backend-Flask%203.x-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-orange.svg)](#)

> **Turning Confusing Lab Reports into Plain-Language Explanations Patients Can Understand**  
> *Theme:* Healthcare Accessibility | *Team:* **Tech Titans**  
> *Core Motto:* **"Every value explained, nothing diagnosed."**

---

## 📌 Problem & Solution Overview

When patients receive laboratory test reports filled with medical abbreviations (*SGPT, HbA1c, TSH, Bilirubin*), delays before doctor visits cause panic, frantic internet searches, and misleading WhatsApp forwards.

**ReportSaathi** bridges this health literacy gap through an ethical, deterministic-first framework:
1. **Rules Decide (Deterministic comparison):** Test status (`HIGH`, `LOW`, `NORMAL`) is strictly evaluated by mathematical Python comparisons against the lab's printed reference range. Status is **never hallucinated or guessed by an LLM**.
2. **AI Explains (Plain Language):** Curated, MedlinePlus/LOINC-aligned plain-language explanations in **Hindi and English** explain what each test measures and highlight everyday factors (hydration, exercise) to calm anxiety.
3. **Safety Guardrail (WHO AI Guidelines):** Strictly refuses autonomous diagnosis or prescription requests and empowers patients with specific questions for their doctor.

---

## 📁 Repository File Structure

```text
report-saathi/
│
├── app.py                   # Flask server & REST API (Upload, Analyze, Chat, History)
├── rules_engine.py          # Deterministic range evaluator (Rules first, AI second)
├── medical_dictionary.py    # MedlinePlus & LOINC curated bilingual health explanations
├── safety_guard.py          # WHO-compliant medical safety guardrail (Refusal guard)
├── report_parser.py         # Universal PDF/Image text & table extraction parser
├── sample_reports.py        # Pre-loaded persona datasets (Sunita LFT, Ramesh CBC, Vikram)
├── database.py              # SQLite storage & safety compliance audit logger
├── test_app.py              # Automated unit tests for rules, dictionary, & API routes
│
├── templates/
│   └── index.html           # Modern responsive dashboard, range gauges & modals
│
├── static/
│   ├── css/
│   │   └── style.css        # Range gauge styles, badges, and print CSS
│   └── js/
│       └── main.js          # Speech synthesis, dynamic cards, bilingual switcher
│
├── run.bat                  # 1-Click Windows launcher script for localhost:5000
├── requirements.txt         # Python project dependencies
├── .gitignore               # Ignored files for clean git commits
└── README.md                # Project documentation & presentation guide
```

---

## 🚀 Localhost Setup & Installation

### Prerequisites
- Python 3.10 or higher
- Any modern web browser (Google Chrome, Edge, Firefox)

### Step 1: Clone or Open the Repository
```bash
git clone https://github.com/your-username/report-saathi.git
cd report-saathi
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the Application
```bash
python app.py
```
*Or on Windows: simply double-click `run.bat`.*

### Step 4: Open in Browser
Visit **`http://localhost:5000`** or **`http://127.0.0.1:5000`** in your browser.

---

## 🧪 Running Unit Tests

Run the test suite covering deterministic logic, dictionary mappings, safety guardrails, and APIs:
```bash
python test_app.py
```

---

## 🎯 Key Features Demonstrated in Prototype

1. **Universal Report Checker:**
   - Upload any real lab report **PDF** (extracted via `pypdf`).
   - Upload report **Photos / Scans** (client-side optical character recognition).
   - Paste raw report text from portals or SMS.
   - Interactive live test builder with 1-click test chips (*Creatinine, Uric Acid, TSH, etc.*).
2. **Deterministic Visual Range Gauge:**
   - Color-coded spectrum with precise pointer needle indicating where the value sits against the lab range.
3. **Bilingual Accessibility (English & हिंदी):**
   - 1-click toggle switches every term, explanation, and doctor question into clear Hindi.
   - Built-in **Text-to-Speech (TTS)** voice narrator for rural/low-literacy accessibility.
4. **WHO Medical Safety Guardrail:**
   - Detects and firmly refuses diagnostic questions (`"Kya mujhe liver disease hai?"`).
   - Redirects patient toward qualified clinicians.
5. **Printable Doctor Consultation Companion Slip:**
   - 1-click printable PDF summary of flagged values and custom questions to carry to the clinic.

---

## 👥 Team
- **Team Name:** Tech Titans
- **Problem Statement ID:** T02
- **Event:** Aayu 2026 • DevAarambh Hackathon

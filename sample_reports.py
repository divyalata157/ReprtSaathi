"""
ReportSaathi - Pre-loaded Clinical Demo Datasets
Matches presentation personas (Sunita in Pali, Rajasthan) and edge cases.
"""

from typing import Dict, Any, List

SAMPLE_DATASETS: Dict[str, Dict[str, Any]] = {
    "lft_sunita": {
        "id": "lft_sunita",
        "title": "Liver Function Test (LFT)",
        "patient_name": "Sunita Sharma",
        "patient_age": "42 Y / Female",
        "patient_town": "Pali, Rajasthan",
        "lab_name": "Marwar Clinical Diagnostics",
        "date": "12-Oct-2026",
        "narrative": "Patient felt anxious after relatives sent alarming WhatsApp forwards. ReportSaathi decodes tests calmly into Hindi/English.",
        "parameters": [
            {
                "param_key": "SGPT",
                "test_name": "SGPT (ALT)",
                "value": 68.0,
                "unit": "U/L",
                "reference_range": "7 to 56 U/L",
                "confidence": 0.98
            },
            {
                "param_key": "SGOT",
                "test_name": "SGOT (AST)",
                "value": 44.0,
                "unit": "U/L",
                "reference_range": "10 to 40 U/L",
                "confidence": 0.96
            },
            {
                "param_key": "BILIRUBIN_TOTAL",
                "test_name": "Total Bilirubin",
                "value": 0.9,
                "unit": "mg/dL",
                "reference_range": "0.2 to 1.2 mg/dL",
                "confidence": 0.99
            },
            {
                "param_key": "ALKALINE_PHOSPHATASE",
                "test_name": "Alkaline Phosphatase (ALP)",
                "value": 98.0,
                "unit": "U/L",
                "reference_range": "44 to 147 U/L",
                "confidence": 0.95
            }
        ]
    },
    "cbc_routine": {
        "id": "cbc_routine",
        "title": "Complete Blood Count (CBC)",
        "patient_name": "Ramesh Verma",
        "patient_age": "34 Y / Male",
        "patient_town": "Jodhpur, Rajasthan",
        "lab_name": "Thar Pathology Labs",
        "date": "10-Oct-2026",
        "narrative": "Routine yearly wellness checkup showing mild anemia with normal infection markers.",
        "parameters": [
            {
                "param_key": "HEMOGLOBIN",
                "test_name": "Hemoglobin (Hb)",
                "value": 9.8,
                "unit": "g/dL",
                "reference_range": "13.0 to 17.0 g/dL",
                "confidence": 0.97
            },
            {
                "param_key": "TLC",
                "test_name": "Total Leukocyte Count (WBC)",
                "value": 6800.0,
                "unit": "cells/cumm",
                "reference_range": "4000 to 11000 cells/cumm",
                "confidence": 0.98
            },
            {
                "param_key": "PLATELETS",
                "test_name": "Platelet Count",
                "value": 2.2,
                "unit": "lakh/cumm",
                "reference_range": "1.5 to 4.5 lakh/cumm",
                "confidence": 0.95
            }
        ]
    },
    "diabetes_metabolic": {
        "id": "diabetes_metabolic",
        "title": "Diabetes & Metabolic Health Panel",
        "patient_name": "Vikram Malhotra",
        "patient_age": "52 Y / Male",
        "patient_town": "Jaipur, Rajasthan",
        "lab_name": "Apex Diagnostic Centre",
        "date": "08-Oct-2026",
        "narrative": "Comprehensive senior health profile covering glucose control, kidney creatinine, and thyroid balance.",
        "parameters": [
            {
                "param_key": "HBA1C",
                "test_name": "HbA1c (Glycated Hemoglobin)",
                "value": 7.4,
                "unit": "%",
                "reference_range": "4.0 to 5.6 %",
                "confidence": 0.99
            },
            {
                "param_key": "FASTING_GLUCOSE",
                "test_name": "Fasting Blood Sugar (FBS)",
                "value": 142.0,
                "unit": "mg/dL",
                "reference_range": "70 to 99 mg/dL",
                "confidence": 0.98
            },
            {
                "param_key": "CHOLESTEROL_TOTAL",
                "test_name": "Total Cholesterol",
                "value": 218.0,
                "unit": "mg/dL",
                "reference_range": "< 200 mg/dL",
                "confidence": 0.96
            },
            {
                "param_key": "CREATININE",
                "test_name": "Serum Creatinine",
                "value": 0.92,
                "unit": "mg/dL",
                "reference_range": "0.6 to 1.2 mg/dL",
                "confidence": 0.97
            },
            {
                "param_key": "TSH",
                "test_name": "TSH (Thyroid Stimulating Hormone)",
                "value": 2.85,
                "unit": "uIU/mL",
                "reference_range": "0.4 to 4.2 uIU/mL",
                "confidence": 0.94
            },
            {
                "param_key": "VITAMIN_D",
                "test_name": "Vitamin D (25-OH)",
                "value": 16.5,
                "unit": "ng/mL",
                "reference_range": "30 to 100 ng/mL",
                "confidence": 0.95
            }
        ]
    },
    "ocr_edge_case": {
        "id": "ocr_edge_case",
        "title": "Low Scan Quality & Missing Range Test",
        "patient_name": "Devendra Singh",
        "patient_age": "48 Y / Male",
        "patient_town": "Barmer, Rajasthan",
        "lab_name": "Rural Mobile Health Van",
        "date": "11-Oct-2026",
        "narrative": "Demonstrates Slide 4 safety strategies: Low OCR confidence row gets flagged 'Please Verify' and unprinted ranges are never guessed.",
        "parameters": [
            {
                "param_key": "SGPT",
                "test_name": "SGPT (ALT)",
                "value": 68.0,
                "unit": "U/L",
                "reference_range": "7 to 56 U/L",
                "confidence": 0.62  # Triggers low-confidence verification banner
            },
            {
                "param_key": "HEMOGLOBIN",
                "test_name": "Hemoglobin (Hb)",
                "value": 14.1,
                "unit": "g/dL",
                "reference_range": "",  # Missing range: rules engine will output RANGE_NOT_FOUND
                "confidence": 0.96
            }
        ]
    }
}

"""
ReportSaathi - Universal Lab Report Text & PDF Parser
Extracts clinical test rows from raw text, PDF pages, or OCR outputs.
"""

import re
from typing import List, Dict, Any, Tuple
from pypdf import PdfReader
import io

# Common unit patterns
UNIT_REGEX = r'(?:mg/dL|g/dL|U/L|IU/L|uIU/mL|ng/mL|pg/mL|mmol/L|cells/cumm|lakh/cumm|million/cumm|%|mm/hr|fl|fL|g/L|mEq/L|mg/L)'

def extract_text_from_pdf(pdf_bytes: bytes) -> str:
    """Extracts all text content from an uploaded PDF file."""
    try:
        reader = PdfReader(io.BytesIO(pdf_bytes))
        full_text = []
        for page in reader.pages:
            t = page.extract_text()
            if t:
                full_text.append(t)
        return "\n".join(full_text)
    except Exception as e:
        return f"Error reading PDF: {str(e)}"

def parse_report_text(raw_text: str) -> Tuple[Dict[str, str], List[Dict[str, Any]]]:
    """
    Parses unstructured lab report text to extract:
    1. Metadata (Patient Name, Date, Lab Name if detected)
    2. Test parameters (Name, Value, Unit, Reference Range)
    """
    metadata = {
        "patient_name": "Patient",
        "date": "Today",
        "lab_name": "Diagnostic Laboratory",
        "patient_town": "Local Diagnostics"
    }
    
    # Try detecting patient name
    name_match = re.search(r'(?:patient(?:\s+name)?|name|mr\.|mrs\.|ms\.)[:\s]+([A-Za-z\s]{3,30})', raw_text, re.IGNORECASE)
    if name_match:
        metadata["patient_name"] = name_match.group(1).strip()
        
    date_match = re.search(r'(?:date|dated|collected)[:\s]+([\d]{1,2}[-/\.][\d]{1,2}[-/\.][\d]{2,4})', raw_text, re.IGNORECASE)
    if date_match:
        metadata["date"] = date_match.group(1).strip()

    extracted_params = []
    lines = [line.strip() for line in raw_text.splitlines() if line.strip()]

    # Regex patterns for matching typical diagnostic test lines:
    # Example: "SGPT (ALT)  68.0  U/L  7 - 56"
    # Example: "Hemoglobin : 14.2 g/dL (13.0 to 17.0)"
    # Example: "Total Cholesterol  220  mg/dL  < 200"
    line_pattern_1 = re.compile(
        r'^([A-Za-z0-9\s\(\)/_\-\+]+?)'                         # Test Name
        r'[:\s\t]+'
        r'([\d\.]+)'                                           # Observed numeric value
        r'(?:\s*(' + UNIT_REGEX + r'))?'                       # Optional unit
        r'[\s\t:,\(\[\{]+'
        r'([<>=~]?\s*[\d\.]+\s*(?:to|-|–|—)\s*[\d\.]+|[<>]=?\s*[\d\.]+)' # Reference range
        r'.*$', re.IGNORECASE
    )

    # Simplified pattern: Name, Value, Range
    line_pattern_2 = re.compile(
        r'^([A-Za-z0-9\s\(\)/_\-\+]{3,40}?)'                   # Test Name
        r'[:\s\t]+'
        r'([\d\.]+)'                                           # Numeric value
        r'\s*([A-Za-z/%]+)?'                                   # Unit
        r'\s+([0-9\.]+\s*(?:-|to)\s*[0-9\.]+|[<>]=?\s*[0-9\.]+)', # Range
        re.IGNORECASE
    )

    seen_tests = set()

    for line in lines:
        # Ignore noisy header/footer lines
        if any(h in line.lower() for h in ["page", "authorized", "signature", "phone", "email", "address", "tested by", "verified by"]):
            continue

        match = line_pattern_1.search(line) or line_pattern_2.search(line)
        if match:
            test_name = match.group(1).strip(" :-\t")
            # Filter out non-test words
            if len(test_name) < 2 or test_name.lower() in ["test", "parameter", "investigation", "result", "normal range", "reference"]:
                continue
                
            try:
                val = float(match.group(2))
            except ValueError:
                continue

            unit = (match.group(3) or "").strip()
            ref_range = (match.group(4) or "").strip()

            norm_key = re.sub(r'[^a-zA-Z0-9]', '', test_name.lower())
            if norm_key in seen_tests:
                continue
            seen_tests.add(norm_key)

            extracted_params.append({
                "test_name": test_name,
                "value": val,
                "unit": unit,
                "reference_range": ref_range,
                "confidence": 0.95
            })

    # If line patterns found nothing, attempt a targeted keyword search for standard parameters
    if not extracted_params:
        common_keywords = [
            ("Hemoglobin", r'hemoglobin[^\d]*([\d\.]+)\s*([a-zA-Z/]+)?[^\d]*([\d\.]+\s*-\s*[\d\.]+)?'),
            ("SGPT (ALT)", r'(?:sgpt|alt)[^\d]*([\d\.]+)\s*([a-zA-Z/]+)?[^\d]*([\d\.]+\s*(?:-|to)\s*[\d\.]+)?'),
            ("SGOT (AST)", r'(?:sgot|ast)[^\d]*([\d\.]+)\s*([a-zA-Z/]+)?[^\d]*([\d\.]+\s*(?:-|to)\s*[\d\.]+)?'),
            ("Total Bilirubin", r'bilirubin[^\d]*([\d\.]+)\s*([a-zA-Z/]+)?[^\d]*([\d\.]+\s*(?:-|to)\s*[\d\.]+)?'),
            ("HbA1c", r'hba1c[^\d]*([\d\.]+)\s*%?[^\d]*([\d\.]+\s*(?:-|to)\s*[\d\.]+)?'),
            ("Fasting Blood Sugar", r'(?:fasting|fbs|glucose)[^\d]*([\d\.]+)\s*([a-zA-Z/]+)?[^\d]*([\d\.]+\s*(?:-|to)\s*[\d\.]+)?'),
            ("Serum Creatinine", r'creatinine[^\d]*([\d\.]+)\s*([a-zA-Z/]+)?[^\d]*([\d\.]+\s*(?:-|to)\s*[\d\.]+)?'),
            ("Total Cholesterol", r'cholesterol[^\d]*([\d\.]+)\s*([a-zA-Z/]+)?[^\d]*([<>=]?\s*[\d\.]+)?'),
            ("TSH", r'tsh[^\d]*([\d\.]+)\s*([a-zA-Z/]+)?[^\d]*([\d\.]+\s*(?:-|to)\s*[\d\.]+)?'),
            ("Platelet Count", r'platelet[^\d]*([\d\.]+)\s*([a-zA-Z/]+)?[^\d]*([\d\.]+\s*(?:-|to)\s*[\d\.]+)?'),
            ("Vitamin D", r'vitamin\s*d[^\d]*([\d\.]+)\s*([a-zA-Z/]+)?[^\d]*([\d\.]+\s*(?:-|to)\s*[\d\.]+)?')
        ]
        for name, kw_pat in common_keywords:
            m = re.search(kw_pat, raw_text, re.IGNORECASE)
            if m:
                try:
                    v = float(m.group(1))
                    u = (m.group(2) or "").strip()
                    r = (m.group(3) or "").strip()
                    extracted_params.append({
                        "test_name": name,
                        "value": v,
                        "unit": u,
                        "reference_range": r,
                        "confidence": 0.90
                    })
                except (ValueError, IndexError):
                    pass

    return metadata, extracted_params

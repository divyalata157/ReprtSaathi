"""
ReportSaathi - Hackathon Prototype Server
Problem Statement: T02 - "Report, Decoded"
Theme: Healthcare Accessibility | Aayu 2026 / DevAarambh
Team: Tech Titans
"""

from flask import Flask, render_template, request, jsonify
import os
import json
from rules_engine import RulesEngine
from medical_dictionary import find_parameter_info
from safety_guard import evaluate_patient_query
from sample_reports import SAMPLE_DATASETS
import database

app = Flask(__name__)

# Initialize SQLite database
database.init_db()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/samples", methods=["GET"])
def get_samples():
    """Returns metadata list of pre-configured sample reports."""
    summary_list = []
    for s_id, s_data in SAMPLE_DATASETS.items():
        summary_list.append({
            "id": s_id,
            "title": s_data["title"],
            "patient_name": s_data["patient_name"],
            "patient_town": s_data["patient_town"],
            "lab_name": s_data["lab_name"],
            "narrative": s_data["narrative"],
            "param_count": len(s_data["parameters"])
        })
    return jsonify({"success": True, "samples": summary_list})

@app.route("/api/analyze", methods=["POST"])
def analyze_report():
    """
    Decodes lab report parameters deterministically.
    'Rules Decide, AI Explains'
    """
    data = request.get_json() or {}
    sample_id = data.get("sample_id")
    
    if sample_id and sample_id in SAMPLE_DATASETS:
        raw_report = SAMPLE_DATASETS[sample_id]
        report_meta = {
            "title": raw_report["title"],
            "patient_name": raw_report["patient_name"],
            "patient_age": raw_report.get("patient_age", "N/A"),
            "patient_town": raw_report["patient_town"],
            "lab_name": raw_report["lab_name"],
            "date": raw_report["date"],
            "narrative": raw_report.get("narrative", "")
        }
        parameters_in = raw_report["parameters"]
    else:
        # Custom uploaded/manual report
        report_meta = {
            "title": data.get("title", "Scanned Laboratory Report"),
            "patient_name": data.get("patient_name", "Sunita Sharma"),
            "patient_age": data.get("patient_age", "42 Y"),
            "patient_town": data.get("patient_town", "Pali, Rajasthan"),
            "lab_name": data.get("lab_name", "Clinical Laboratory"),
            "date": data.get("date", "Today"),
            "narrative": "Uploaded report decoded with deterministic rules."
        }
        parameters_in = data.get("parameters", [])

    decoded_cards = []
    out_of_range_count = 0
    verification_count = 0

    for param in parameters_in:
        name = param.get("test_name", "Unknown Test")
        key = param.get("param_key") or name
        val = float(param.get("value", 0.0))
        unit = param.get("unit", "")
        ref_range = param.get("reference_range", "")
        confidence = float(param.get("confidence", 0.95))

        # 1. Deterministic Rule Engine Evaluation (Slide 2: Status set by rules, not AI)
        rule_eval = RulesEngine.evaluate(val, ref_range, confidence)
        
        if rule_eval["is_abnormal"]:
            out_of_range_count += 1
        if rule_eval["needs_verification"]:
            verification_count += 1

        # 2. Curated Medical Plain-Language Dictionary (Slide 2 & Slide 3)
        dict_info = find_parameter_info(key)

        card = {
            "test_name": name,
            "canonical_name": dict_info.get("canonical_name", name),
            "loinc_code": dict_info.get("loinc_code", "N/A"),
            "category": dict_info.get("category", "General"),
            "value": val,
            "unit": unit or dict_info.get("default_unit", ""),
            "reference_range": ref_range,
            "confidence": confidence,
            "rule_eval": rule_eval,
            "explanation": {
                "en": dict_info.get("description_en", ""),
                "hi": dict_info.get("description_hi", ""),
                "benign_factors_en": dict_info.get("benign_factors_en", ""),
                "benign_factors_hi": dict_info.get("benign_factors_hi", ""),
                "questions_en": dict_info.get("questions_en", []),
                "questions_hi": dict_info.get("questions_hi", [])
            }
        }
        decoded_cards.append(card)

    # Save to SQLite database
    scan_id = database.save_report_scan(
        report_title=report_meta["title"],
        patient_name=report_meta["patient_name"],
        patient_town=report_meta["patient_town"],
        parameters=decoded_cards,
        ocr_confidence=0.96 if verification_count == 0 else 0.70
    )

    return jsonify({
        "success": True,
        "scan_id": scan_id,
        "meta": report_meta,
        "summary": {
            "total_tests": len(decoded_cards),
            "normal_count": len(decoded_cards) - out_of_range_count,
            "out_of_range_count": out_of_range_count,
            "verification_alerts": verification_count
        },
        "cards": decoded_cards
    })

@app.route("/api/chat", methods=["POST"])
def chat_assistant():
    """
    Patient Q&A with Medical AI Safety Guardrail
    Slide 4: AI drifting into diagnosis -> fixed prompts, refusal guard that sends such questions to doctor.
    Slide 7: 'Every value explained, nothing diagnosed.'
    """
    data = request.get_json() or {}
    query = data.get("query", "")
    context = data.get("context", "")

    result = evaluate_patient_query(query, context)
    
    # Audit log to SQLite
    database.log_safety_event(
        query=query,
        refusal_triggered=result["refusal_triggered"],
        category=result["category"]
    )

    return jsonify({
        "success": True,
        "result": result
    })

@app.route("/api/history", methods=["GET"])
def get_history():
    """Returns history of previous scans from SQLite."""
    records = database.get_recent_reports(limit=6)
    return jsonify({"success": True, "history": records})

@app.route("/api/simulate-ocr", methods=["POST"])
def simulate_ocr():
    """
    Simulates OpenCV & PaddleOCR / Tesseract pipeline as shown in Slide 3 & 4.
    Prepares, cleanups, deskews, extracts table rows into JSON with confidence scores.
    """
    data = request.get_json() or {}
    sample_id = data.get("sample_id", "lft_sunita")
    
    sample = SAMPLE_DATASETS.get(sample_id, SAMPLE_DATASETS["lft_sunita"])
    
    ocr_steps = [
        {"step": 1, "name": "Image Preprocessing", "tool": "Pillow / OpenCV", "status": "Grayscale binarization & bilateral noise filter complete."},
        {"step": 2, "name": "Deskewing & Alignment", "tool": "OpenCV Geometric", "status": "Orientation normalized: Angle 0.4° compensated."},
        {"step": 3, "name": "Table Cell Bounding", "tool": "PyMuPDF / PaddleOCR", "status": f"Detected {len(sample['parameters'])} parameter rows with headers."},
        {"step": 4, "name": "Alias Resolution", "tool": "LOINC Standardization", "status": "Resolved SGPT -> ALT, SGOT -> AST."}
    ]
    
    return jsonify({
        "success": True,
        "sample_id": sample_id,
        "pipeline_steps": ocr_steps,
        "extracted_rows": sample["parameters"]
    })

@app.route("/api/upload-report", methods=["POST"])
def upload_report_file():
    """
    Accepts uploaded PDF/text/image files or pasted raw text and extracts parameters.
    """
    from report_parser import extract_text_from_pdf, parse_report_text
    
    extracted_text = ""
    file_type = "text"
    filename = "report"
    
    if "file" in request.files:
        file = request.files["file"]
        filename = file.filename or "uploaded_report"
        content = file.read()
        
        if filename.lower().endswith(".pdf"):
            file_type = "pdf"
            extracted_text = extract_text_from_pdf(content)
        else:
            file_type = "image_or_text"
            try:
                extracted_text = content.decode("utf-8", errors="ignore")
            except Exception:
                extracted_text = ""
    else:
        # Check raw JSON payload with text
        payload = request.get_json(silent=True) or {}
        extracted_text = payload.get("raw_text", "")
        file_type = "pasted_text"

    if not extracted_text:
        return jsonify({
            "success": False,
            "message": "No readable text could be extracted. Please paste text or try manual entry."
        }), 400

    metadata, parameters = parse_report_text(extracted_text)
    
    return jsonify({
        "success": True,
        "file_type": file_type,
        "filename": filename,
        "metadata": metadata,
        "extracted_parameters": parameters,
        "raw_text_preview": extracted_text[:500]
    })

@app.route("/api/decode-custom", methods=["POST"])
def decode_custom_report():
    """
    Decodes ANY custom lab report submitted by user with full deterministic rules engine.
    """
    data = request.get_json() or {}
    report_meta = {
        "title": data.get("title", "Custom Scanned Lab Report"),
        "patient_name": data.get("patient_name", "Patient"),
        "patient_age": data.get("patient_age", "N/A"),
        "patient_town": data.get("patient_town", "Custom Patient"),
        "lab_name": data.get("lab_name", "Laboratory"),
        "date": data.get("date", "Today"),
        "narrative": data.get("narrative", "User-uploaded lab report decoded deterministically.")
    }
    parameters_in = data.get("parameters", [])

    decoded_cards = []
    out_of_range_count = 0
    verification_count = 0

    for param in parameters_in:
        name = param.get("test_name", "Unknown Test").strip()
        if not name:
            continue
        try:
            val = float(param.get("value", 0.0))
        except (ValueError, TypeError):
            val = 0.0

        unit = param.get("unit", "").strip()
        ref_range = param.get("reference_range", "").strip()
        confidence = float(param.get("confidence", 0.95))

        # Deterministic evaluation
        rule_eval = RulesEngine.evaluate(val, ref_range, confidence)
        if rule_eval["is_abnormal"]:
            out_of_range_count += 1
        if rule_eval["needs_verification"]:
            verification_count += 1

        # Curated dictionary lookup
        dict_info = find_parameter_info(name)

        card = {
            "test_name": name,
            "canonical_name": dict_info.get("canonical_name", name),
            "loinc_code": dict_info.get("loinc_code", "N/A"),
            "category": dict_info.get("category", "General"),
            "value": val,
            "unit": unit or dict_info.get("default_unit", ""),
            "reference_range": ref_range,
            "confidence": confidence,
            "rule_eval": rule_eval,
            "explanation": {
                "en": dict_info.get("description_en", ""),
                "hi": dict_info.get("description_hi", ""),
                "benign_factors_en": dict_info.get("benign_factors_en", ""),
                "benign_factors_hi": dict_info.get("benign_factors_hi", ""),
                "questions_en": dict_info.get("questions_en", []),
                "questions_hi": dict_info.get("questions_hi", [])
            }
        }
        decoded_cards.append(card)

    scan_id = database.save_report_scan(
        report_title=report_meta["title"],
        patient_name=report_meta["patient_name"],
        patient_town=report_meta["patient_town"],
        parameters=decoded_cards,
        ocr_confidence=0.95 if verification_count == 0 else 0.70
    )

    return jsonify({
        "success": True,
        "scan_id": scan_id,
        "meta": report_meta,
        "summary": {
            "total_tests": len(decoded_cards),
            "normal_count": len(decoded_cards) - out_of_range_count,
            "out_of_range_count": out_of_range_count,
            "verification_alerts": verification_count
        },
        "cards": decoded_cards
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)

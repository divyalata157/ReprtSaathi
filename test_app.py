"""
Unit tests for ReportSaathi prototype components
"""

import unittest
from rules_engine import RulesEngine
from medical_dictionary import find_parameter_info
from safety_guard import evaluate_patient_query
import json
from app import app

class TestReportSaathi(unittest.TestCase):
    def test_rules_engine_between(self):
        # SGPT 68 U/L with range 7 to 56 -> HIGH
        res = RulesEngine.evaluate(68.0, "7 to 56 U/L")
        self.assertEqual(res["status"], "HIGH")
        self.assertTrue(res["is_abnormal"])
        self.assertGreater(res["gauge_percent"], 80)

        # Bilirubin 0.9 mg/dL with range 0.2 to 1.2 -> NORMAL
        res_norm = RulesEngine.evaluate(0.9, "0.2 to 1.2 mg/dL")
        self.assertEqual(res_norm["status"], "NORMAL")
        self.assertFalse(res_norm["is_abnormal"])

        # Hemoglobin 9.8 with range 13.0 to 17.0 -> LOW
        res_low = RulesEngine.evaluate(9.8, "13.0 - 17.0 g/dL")
        self.assertEqual(res_low["status"], "LOW")
        self.assertTrue(res_low["is_abnormal"])

    def test_missing_range_safety(self):
        # Missing range -> RANGE_NOT_FOUND, never guessed
        res = RulesEngine.evaluate(14.0, "")
        self.assertEqual(res["status"], "RANGE_NOT_FOUND")
        self.assertTrue(res["needs_verification"])

    def test_medical_dictionary_aliases(self):
        # SGPT alias to ALT
        info_alt = find_parameter_info("alt")
        self.assertIsNotNone(info_alt)
        self.assertEqual(info_alt["canonical_name"], "SGPT (ALT)")
        self.assertIn("लिवर", info_alt["description_hi"])

    def test_safety_guardrail_refusal(self):
        # Clinical diagnostic question must be refused
        q_refusal = evaluate_patient_query("Kya mujhe liver disease hai?")
        self.assertTrue(q_refusal["refusal_triggered"])
        self.assertIn("Safety Guardrail Activated", q_refusal["reply_en"])
        self.assertIn("WHO", q_refusal["reply_en"])

        # Informational question allowed
        q_info = evaluate_patient_query("What does SGPT measure?")
        self.assertFalse(q_info["refusal_triggered"])

    def test_flask_endpoints(self):
        client = app.test_client()
        # Test index
        r_index = client.get("/")
        self.assertEqual(r_index.status_code, 200)

        # Test samples
        r_samples = client.get("/api/samples")
        self.assertEqual(r_samples.status_code, 200)
        self.assertTrue(r_samples.json["success"])

        # Test analyze Sunita's LFT
        r_analyze = client.post("/api/analyze", json={"sample_id": "lft_sunita"})
        self.assertEqual(r_analyze.status_code, 200)
        res_data = r_analyze.json
        self.assertTrue(res_data["success"])
        self.assertEqual(res_data["meta"]["patient_name"], "Sunita Sharma")
        self.assertEqual(res_data["summary"]["out_of_range_count"], 2)

        # Test upload text parsing
        r_upload = client.post("/api/upload-report", json={
            "raw_text": "Serum Creatinine 1.5 mg/dL 0.6 - 1.2\nTSH 5.6 uIU/mL 0.4 - 4.2"
        })
        self.assertEqual(r_upload.status_code, 200)
        self.assertEqual(len(r_upload.json["extracted_parameters"]), 2)

        # Test decode custom
        r_decode = client.post("/api/decode-custom", json={
            "patient_name": "Test Patient",
            "parameters": [
                {"test_name": "Serum Creatinine", "value": 1.5, "unit": "mg/dL", "reference_range": "0.6 to 1.2"}
            ]
        })
        self.assertEqual(r_decode.status_code, 200)
        self.assertEqual(r_decode.json["summary"]["out_of_range_count"], 1)

if __name__ == "__main__":
    unittest.main()

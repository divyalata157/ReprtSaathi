"""
ReportSaathi - SQLite Persistence Layer
Stores report scan sessions, parameter audits, and safety-compliance event logs.
"""

import sqlite3
import json
import os
from typing import Dict, Any, List

DB_PATH = os.path.join(os.path.dirname(__file__), "reportsaathi.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Reports table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reports (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        report_title TEXT NOT NULL,
        patient_name TEXT DEFAULT 'Anonymous Patient',
        patient_town TEXT DEFAULT 'Pali, Rajasthan',
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        ocr_confidence REAL DEFAULT 0.95,
        total_parameters INTEGER,
        out_of_range_count INTEGER,
        raw_json TEXT
    )
    """)
    
    # Audit log for Safety Refusal events
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS safety_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        query TEXT NOT NULL,
        refusal_triggered BOOLEAN,
        category TEXT
    )
    """)
    
    conn.commit()
    conn.close()

def save_report_scan(report_title: str, patient_name: str, patient_town: str, parameters: List[Dict[str, Any]], ocr_confidence: float = 0.95) -> int:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    out_of_range = sum(1 for p in parameters if p.get("rule_eval", {}).get("is_abnormal", False))
    raw_json = json.dumps(parameters)
    
    cursor.execute("""
    INSERT INTO reports (report_title, patient_name, patient_town, ocr_confidence, total_parameters, out_of_range_count, raw_json)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (report_title, patient_name, patient_town, ocr_confidence, len(parameters), out_of_range, raw_json))
    
    report_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return report_id

def log_safety_event(query: str, refusal_triggered: bool, category: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO safety_logs (query, refusal_triggered, category)
    VALUES (?, ?, ?)
    """, (query, refusal_triggered, category))
    conn.commit()
    conn.close()

def get_recent_reports(limit: int = 5) -> List[Dict[str, Any]]:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("""
    SELECT id, report_title, patient_name, patient_town, timestamp, ocr_confidence, total_parameters, out_of_range_count
    FROM reports ORDER BY id DESC LIMIT ?
    """, (limit,))
    rows = cursor.fetchall()
    conn.close()
    return [dict(r) for r in rows]

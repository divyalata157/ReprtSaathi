"""
ReportSaathi - Deterministic Rules Engine
Core Principle: "Rules first, AI second"
Compares laboratory test values directly against printed reference ranges using strict code.
No AI is used to decide if a value is Normal, High, or Low.
"""

import re
from typing import Dict, Any, Optional, Tuple

class RulesEngine:
    @staticmethod
    def parse_range(range_str: str) -> Tuple[Optional[float], Optional[float], str]:
        """
        Parses common lab range formats into (min_val, max_val, format_type).
        Examples:
        - "7 to 56" -> (7.0, 56.0, "between")
        - "7 - 56" -> (7.0, 56.0, "between")
        - "< 200" or "<= 200" -> (0.0, 200.0, "less_than")
        - "> 60" or ">= 60" -> (60.0, None, "greater_than")
        - "Up to 140" -> (0.0, 140.0, "less_than")
        - "Negative" or "Non-Reactive" -> (None, None, "qualitative")
        """
        if not range_str or not isinstance(range_str, str):
            return None, None, "unknown"
            
        clean_str = range_str.strip().replace(",", "")
        
        # Check qualitative
        if any(w in clean_str.lower() for w in ["negative", "non-reactive", "nil", "normal"]):
            return None, None, "qualitative"

        # Pattern: min to/–/- max
        between_match = re.search(r'([\d\.]+)\s*(?:to|-|–|—)\s*([\d\.]+)', clean_str, re.IGNORECASE)
        if between_match:
            try:
                min_v = float(between_match.group(1))
                max_v = float(between_match.group(2))
                return min_v, max_v, "between"
            except ValueError:
                pass

        # Pattern: < or <= or up to
        less_match = re.search(r'(?:<|<=|less than|up to)\s*([\d\.]+)', clean_str, re.IGNORECASE)
        if less_match:
            try:
                max_v = float(less_match.group(1))
                return 0.0, max_v, "less_than"
            except ValueError:
                pass

        # Pattern: > or >=
        greater_match = re.search(r'(?:>|>=|greater than|more than)\s*([\d\.]+)', clean_str, re.IGNORECASE)
        if greater_match:
            try:
                min_v = float(greater_match.group(1))
                return min_v, None, "greater_than"
            except ValueError:
                pass

        return None, None, "unknown"

    @classmethod
    def evaluate(cls, value: float, range_str: str, confidence: float = 1.0) -> Dict[str, Any]:
        """
        Deterministically evaluates test value against reference range.
        Returns evaluation dict with status, gauge position, and verification flags.
        """
        min_v, max_v, range_type = cls.parse_range(range_str)
        
        needs_verification = confidence < 0.75
        
        if range_type == "unknown" or (min_v is None and max_v is None):
            return {
                "status": "RANGE_NOT_FOUND",
                "status_label_en": "Range Not Found",
                "status_label_hi": "संदर्भ सीमा उपलब्ध नहीं",
                "badge_color": "gray",
                "rule_message": "No reference range detected on report. Value cannot be evaluated automatically.",
                "min_val": None,
                "max_val": None,
                "gauge_percent": 50,
                "needs_verification": True,
                "verification_reason": "Missing reference range",
                "is_abnormal": False
            }

        # Deterministic comparisons
        status = "NORMAL"
        badge_color = "emerald"
        is_abnormal = False
        label_en = "NORMAL"
        label_hi = "सामान्य"

        if range_type == "between":
            if value < min_v:
                status = "LOW"
                badge_color = "amber"
                is_abnormal = True
                label_en = "LOW"
                label_hi = "कम (LOW)"
            elif value > max_v:
                status = "HIGH"
                badge_color = "rose"
                is_abnormal = True
                label_en = "HIGH"
                label_hi = "अधिक (HIGH)"
            else:
                status = "NORMAL"
                badge_color = "emerald"
                label_en = "NORMAL"
                label_hi = "सामान्य (NORMAL)"

            # Calculate gauge percentage (0% to 100%, where 20-80% is the normal range)
            # This creates a visually intuitive bar
            range_span = max_v - min_v if max_v != min_v else 1.0
            if value < min_v:
                # 0 to 20%
                ratio = max(0.0, (value / min_v) if min_v > 0 else 0)
                gauge_percent = min(18.0, ratio * 20.0)
            elif value > max_v:
                # 80 to 100%
                excess = value - max_v
                excess_ratio = min(1.0, excess / (range_span * 1.5))
                gauge_percent = 80.0 + (excess_ratio * 19.0)
            else:
                # 20 to 80%
                normal_ratio = (value - min_v) / range_span
                gauge_percent = 20.0 + (normal_ratio * 60.0)

        elif range_type == "less_than":
            if value > max_v:
                status = "HIGH"
                badge_color = "rose"
                is_abnormal = True
                label_en = "HIGH"
                label_hi = "अधिक (HIGH)"
                gauge_percent = min(98.0, 75.0 + ((value - max_v) / max_v) * 25.0)
            else:
                status = "NORMAL"
                badge_color = "emerald"
                label_en = "NORMAL"
                label_hi = "सामान्य (NORMAL)"
                gauge_percent = min(70.0, (value / max_v) * 70.0)

        elif range_type == "greater_than":
            if value < min_v:
                status = "LOW"
                badge_color = "amber"
                is_abnormal = True
                label_en = "LOW"
                label_hi = "कम (LOW)"
                gauge_percent = max(5.0, (value / min_v) * 20.0)
            else:
                status = "NORMAL"
                badge_color = "emerald"
                label_en = "NORMAL"
                label_hi = "सामान्य (NORMAL)"
                gauge_percent = 50.0

        else:
            gauge_percent = 50.0

        return {
            "status": status,
            "status_label_en": label_en,
            "status_label_hi": label_hi,
            "badge_color": badge_color,
            "rule_message": f"Deterministic comparison: Value {value} against reference range [{range_str}]. Computed via rule logic, not AI.",
            "min_val": min_v,
            "max_val": max_v,
            "gauge_percent": round(gauge_percent, 1),
            "needs_verification": needs_verification,
            "verification_reason": "Low OCR scan confidence" if needs_verification else None,
            "is_abnormal": is_abnormal
        }

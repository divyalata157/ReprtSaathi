"""
ReportSaathi - AI Medical Safety Guardrail
Compliant with WHO Guidelines on AI in Healthcare:
1. No Autonomous Clinical Diagnosis
2. Deterministic Boundaries (Rules Decide, AI Explains)
3. Refusal Guard for prescriptive or diagnostic prompts
4. Empower Patient-Clinician Dialogue ("Ask Your Doctor")
"""

import re
from typing import Dict, Any

DIAGNOSTIC_TRIGGERS = [
    r"\b(do i have|have i got|am i suffering from|kya mujhe)\b",
    r"\b(diagnose|diagnosis|disease|bimari|bimaari|rog)\b",
    r"\b(cancer|cirrhosis|tumor|hepatitis|leukemia|failure|heart attack)\b",
    r"\b(what medicine|which medicine|konsi dawai|konsi medicine|prescription|dosage|khau|dawa)\b",
    r"\b(how long will i live|am i dying|kya mai marne)\b"
]

def evaluate_patient_query(query: str, current_context: str = "") -> Dict[str, Any]:
    """
    Evaluates patient inquiry against WHO safety guardrails.
    Returns safe response or diagnostic refusal.
    """
    clean_q = query.lower().strip()
    
    # Check if query requests a clinical diagnosis or prescription
    is_diagnostic = any(re.search(pattern, clean_q) for pattern in DIAGNOSTIC_TRIGGERS)
    
    if is_diagnostic:
        return {
            "refusal_triggered": True,
            "category": "MEDICAL_SAFETY_GUARDRAIL",
            "reply_en": (
                "⚠️ **Safety Guardrail Activated: Autonomous Diagnosis Refusal**\n\n"
                "ReportSaathi is strictly designed to decode medical abbreviations and explain what tests measure. "
                "In compliance with WHO medical safety standards, **I cannot diagnose diseases, predict clinical outcomes, or prescribe medications**.\n\n"
                "A lab test number alone does not equal a diagnosis — doctors consider your physical exam, medical history, and overall symptoms.\n\n"
                "📋 **Recommended Action:** Please share this report with your qualified physician. You can ask them:\n"
                "• *'Doctor, what clinical context do these specific values have given my current symptoms?'*\n"
                "• *'Do I need any follow-up clinical examination or repeat testing?'*"
            ),
            "reply_hi": (
                "⚠️ **सुरक्षा गार्डरेल: बीमारी का निदान करने से इनकार**\n\n"
                "ReportSaathi केवल आपकी रिपोर्ट के कठिन शब्दों को सरल भाषा में समझाने के लिए है। "
                "स्वास्थ्य सुरक्षा नियमों (WHO) के अनुसार, **मैं किसी बीमारी का निदान (डायग्नोसिस) नहीं कर सकता और न ही कोई दवा लिख सकता हूँ**।\n\n"
                "सिर्फ एक लैब टेस्ट का नंबर कोई बीमारी तय नहीं करता — डॉक्टर आपके शारीरिक परीक्षण, लक्षणों और मेडिकल हिस्ट्री को देखकर ही सही राय देते हैं।\n\n"
                "📋 **सुझाव:** कृपया अपने डॉक्टर से मिलें और उनसे पूछें:\n"
                "• *'डॉक्टर साहब, मेरे इन टेस्ट परिणामों का मेरे लक्षणों के साथ क्या संबंध है?'*\n"
                "• *'क्या मुझे आगे कोई जांच या फॉलो-अप की आवश्यकता है?'*"
            ),
            "suggested_questions": [
                "Should I repeat this test to confirm the result?",
                "Could lifestyle or temporary factors have influenced this?",
                "Are there any specific symptoms I should keep track of?"
            ]
        }
        
    # Informative & safe response
    # Handle common informational queries
    if any(k in clean_q for k in ["alt", "sgpt", "liver"]):
        return {
            "refusal_triggered": False,
            "category": "EDUCATIONAL_EXPLANATION",
            "reply_en": (
                "SGPT (ALT) is an enzyme found mostly inside liver cells. Think of it as a worker inside a factory: "
                "when liver cells work harder or face temporary stress, some SGPT escapes into the bloodstream.\n\n"
                "Mild elevations are very common and can stem from simple everyday factors like heavy exercise, recent fatty food, or common pain relievers. "
                "Your doctor will look at the whole picture rather than just one number."
            ),
            "reply_hi": (
                "SGPT (ALT) एक ऐसा एंजाइम है जो मुख्य रूप से लिवर कोशिकाओं के अंदर काम करता है। "
                "जब लिवर पर थोड़ा ज्यादा दबाव पड़ता है, तो यह खून में रिसने लगता है।\n\n"
                "हल्की बढ़त बहुत सामान्य है और यह भारी कसरत, गरिष्ठ भोजन या सामान्य दवाओं से भी हो सकती है। "
                "आपके डॉक्टर पूरी स्थिति देखकर ही सही मार्गदर्शन करेंगे।"
            ),
            "suggested_questions": [
                "Could any regular medication be affecting my liver enzymes?",
                "What dietary habits support healthy liver function?"
            ]
        }

    if any(k in clean_q for k in ["sugar", "glucose", "hba1c", "diabetes"]):
        return {
            "refusal_triggered": False,
            "category": "EDUCATIONAL_EXPLANATION",
            "reply_en": (
                "HbA1c shows the average sugar coating on your red blood cells over the last 90 days. "
                "Unlike a daily finger-prick test, it isn't swayed by what you ate yesterday.\n\n"
                "Remember, lifestyle modifications like walking and balanced nutrition play a very strong positive role. Discuss personalized goals with your doctor."
            ),
            "reply_hi": (
                "HbA1c पिछले 90 दिनों (लगभग 3 महीने) के औसत ब्लड शुगर स्तर को दर्शाता है। "
                "यह सिर्फ कल खाए गए भोजन से एकदम ऊपर-नीचे नहीं होता।\n\n"
                "नियमित पैदल चलना और संतुलित खान-पान इसे सुधारने में बहुत मददगार होते हैं। अपने डॉक्टर से व्यक्तिगत लक्ष्य पर बात करें।"
            ),
            "suggested_questions": [
                "What is my ideal target HbA1c level?",
                "Would a custom meal plan be beneficial?"
            ]
        }

    # General fallback explanation
    return {
        "refusal_triggered": False,
        "category": "EDUCATIONAL_EXPLANATION",
        "reply_en": (
            "Lab tests provide helpful reference clues for clinicians, but test numbers are only one piece of the puzzle. "
            "ReportSaathi marks numbers using strict rules against reference ranges and provides plain explanations so you can walk into your doctor's appointment feeling informed and calm."
        ),
        "reply_hi": (
            "लैब रिपोर्ट डॉक्टर के लिए एक महत्वपूर्ण सुराग होती है, लेकिन केवल आंकड़े पूरी कहानी नहीं बताते। "
            "ReportSaathi आपको हर जांच का सरल मतलब समझाता है ताकि आप बिना किसी घबराहट के डॉक्टर से सही सवाल पूछ सकें।"
        ),
        "suggested_questions": [
            "What do these results mean in context of my daily lifestyle?",
            "When should I schedule my next follow-up checkup?"
        ]
    }

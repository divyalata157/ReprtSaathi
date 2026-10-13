"""
ReportSaathi - Curated Medical Parameter Dictionary
Standardized according to LOINC and MedlinePlus (NIH) plain-language health information.
Provides clear, reassuring explanations in English and Hindi.
Strictly avoids clinical diagnosis.
"""

from typing import Dict, Any, Optional

PARAM_DICTIONARY: Dict[str, Dict[str, Any]] = {
    "SGPT": {
        "canonical_name": "SGPT (ALT)",
        "full_name": "Serum Glutamic Pyruvic Transaminase / Alanine Aminotransferase",
        "loinc_code": "1742-6",
        "aliases": ["sgpt", "alt", "alanine transaminase", "alanine aminotransferase", "sgpt/alt", "alt (sgpt)"],
        "category": "Liver Function",
        "default_unit": "U/L",
        "description_en": "An enzyme found mainly inside liver cells. When liver cells are working harder, stressed, or temporarily irritated, small amounts leak into the bloodstream. A value above the lab's range is common and worth discussing calmly with your doctor.",
        "description_hi": "यह मुख्य रूप से लिवर (यकृत) की कोशिकाओं में पाया जाने वाला एक एंजाइम है। जब लिवर पर किसी कारण से थोड़ा तनाव या प्रभाव पड़ता है, तो यह रक्त में बढ़ सकता है। लैब की सामान्य सीमा से अधिक होना आम है और डॉक्टर से मिलकर इस पर चर्चा करनी चाहिए।",
        "benign_factors_en": "Recent strenuous workout, certain over-the-counter pain medications, fatty food intake, or minor viral infections.",
        "benign_factors_hi": "भारी कसरत, सामान्य दर्द निवारक दवाइयां, तैलीय भोजन या हाल ही में हुआ कोई हल्का वायरल संक्रमण।",
        "questions_en": [
            "Should this test be repeated in a few weeks to check for a temporary spike?",
            "Could any daily medication, supplement, or herbal remedy I take affect this value?",
            "Are there any specific dietary or lifestyle modifications you recommend for me?"
        ],
        "questions_hi": [
            "क्या कुछ हफ़्तों बाद यह टेस्ट दोबारा करवा कर देखना चाहिए कि यह अस्थायी तो नहीं था?",
            "क्या मेरी कोई वर्तमान दवा, सप्लीमेंट या काढ़ा इस स्तर को प्रभावित कर सकता है?",
            "मेरे खान-पान और दिनचर्या में आप क्या बदलाव करने की सलाह देंगे?"
        ]
    },
    "SGOT": {
        "canonical_name": "SGOT (AST)",
        "full_name": "Serum Glutamic Oxaloacetic Transaminase / Aspartate Aminotransferase",
        "loinc_code": "1920-8",
        "aliases": ["sgot", "ast", "aspartate aminotransferase", "sgot/ast", "ast (sgot)"],
        "category": "Liver Function",
        "default_unit": "U/L",
        "description_en": "An enzyme found in liver cells, heart muscle, and skeletal muscles. Like SGPT, it enters the blood when tissues are stressed or repairing.",
        "description_hi": "यह एंजाइम लिवर, मांसपेशियों और दिल के ऊतकों में पाया जाता है। मांसपेशियों में खिंचाव या लिवर पर दबाव होने पर इसका स्तर थोड़ा बढ़ सकता है।",
        "benign_factors_en": "Heavy physical exercise, muscle soreness, or recent alcohol intake.",
        "benign_factors_hi": "कठिन शारीरिक व्यायाम, मांसपेशियों में खिंचाव या हाल ही में लिया गया अल्कोहल।",
        "questions_en": [
            "How does this SGOT value correlate with my SGPT result?",
            "Could recent physical exercise or muscle fatigue have influenced this reading?"
        ],
        "questions_hi": [
            "यह SGOT स्तर मेरे SGPT परिणाम के साथ कैसे संबंधित है?",
            "क्या हाल की शारीरिक मेहनत या मांसपेशियों की थकान से यह बदल सकता है?"
        ]
    },
    "BILIRUBIN_TOTAL": {
        "canonical_name": "Total Bilirubin",
        "full_name": "Total Serum Bilirubin",
        "loinc_code": "1975-2",
        "aliases": ["bilirubin total", "total bilirubin", "t. bilirubin", "s. bilirubin total", "bilirubin"],
        "category": "Liver Function",
        "default_unit": "mg/dL",
        "description_en": "A yellowish substance created during the natural breakdown of aged red blood cells. The liver filters it from the blood and releases it into bile.",
        "description_hi": "यह एक पीला वर्णक (pigment) है जो शरीर में पुरानी लाल रक्त कोशिकाओं के प्राकृतिक रूप से टूटने पर बनता है। लिवर इसे छानकर शरीर से बाहर निकालता है।",
        "benign_factors_en": "Dehydration, prolonged fasting, or mild genetic variations like Gilbert's syndrome.",
        "benign_factors_hi": "पानी की कमी (डिहाइड्रेशन), लंबा उपवास या हल्की अनुवांशिक स्थिति जैसे गिल्बर्ट सिंड्रोम।",
        "questions_en": [
            "Is the elevated fraction mainly direct (conjugated) or indirect (unconjugated)?",
            "Do I need an abdominal ultrasound or simple follow-up tests?"
        ],
        "questions_hi": [
            "क्या यह बढ़ा हुआ हिस्सा डायरेक्ट है या इनडायरेक्ट?",
            "क्या मुझे पेट के अल्ट्रासाउंड या आगे किसी टेस्ट की आवश्यकता है?"
        ]
    },
    "ALKALINE_PHOSPHATASE": {
        "canonical_name": "Alkaline Phosphatase (ALP)",
        "full_name": "Serum Alkaline Phosphatase",
        "loinc_code": "6768-6",
        "aliases": ["alkaline phosphatase", "alp", "alk phos", "s. alp"],
        "category": "Liver & Bone",
        "default_unit": "U/L",
        "description_en": "An enzyme associated with the liver's bile ducts and bone tissue. Higher levels can occur during normal bone growth, healing fractures, or bile sluggishness.",
        "description_hi": "यह लिवर की पित्त नलियों और हड्डियों में पाया जाने वाला एंजाइम है। हड्डियों के विकास या पित्त नली के धीमे काम करने पर यह बढ़ सकता है।",
        "benign_factors_en": "Normal bone growth in young adults, healing bone fractures, pregnancy.",
        "benign_factors_hi": "हड्डियों का विकास, हड्डी की चोट का ठीक होना, गर्भावस्था।",
        "questions_en": [
            "Does this ALP elevation originate from the liver or bone?",
            "Are there other bile enzymes (like GGT) we should review?"
        ],
        "questions_hi": [
            "क्या यह ALP वृद्धि लिवर से संबंधित है या हड्डियों से?",
            "क्या इसके साथ GGT टेस्ट की भी समीक्षा करनी चाहिए?"
        ]
    },
    "HEMOGLOBIN": {
        "canonical_name": "Hemoglobin (Hb)",
        "full_name": "Blood Hemoglobin Concentration",
        "loinc_code": "718-7",
        "aliases": ["hemoglobin", "hb", "haemoglobin", "hgb", "hb test"],
        "category": "Complete Blood Count",
        "default_unit": "g/dL",
        "description_en": "The iron-rich protein in your red blood cells that carries vital oxygen from your lungs to the rest of your body.",
        "description_hi": "यह लाल रक्त कोशिकाओं में मौजूद वह प्रोटीन है जो फेफड़ों से पूरे शरीर में ऑक्सीजन पहुंचाने का महत्वपूर्ण काम करता है।",
        "benign_factors_en": "Diet low in iron or vitamin B12, heavy menstrual flow, or high fluid intake before testing.",
        "benign_factors_hi": "आहार में आयरन या विटामिन की कमी, महिलाओं में भारी मासिक धर्म, या टेस्ट से पहले अधिक पानी पीना।",
        "questions_en": [
            "Does this hemoglobin level suggest iron-deficiency anemia?",
            "Would iron or vitamin supplements, or specific iron-rich foods, be helpful for me?"
        ],
        "questions_hi": [
            "क्या यह हीमोग्लोबिन स्तर शरीर में आयरन की कमी (एनीमिया) की ओर इशारा करता है?",
            "क्या मुझे आयरन सप्लीमेंट या खान-पान में हरी सब्जियां/गुड़ बढ़ाने की जरूरत है?"
        ]
    },
    "TLC": {
        "canonical_name": "Total Leukocyte Count (WBC)",
        "full_name": "White Blood Cell Count",
        "loinc_code": "6690-2",
        "aliases": ["tlc", "wbc", "total leukocyte count", "white blood cells", "total wbc"],
        "category": "Complete Blood Count",
        "default_unit": "cells/cumm",
        "description_en": "Your body's immune defense cells. They multiply when your body is fighting off common bugs, recovering from stress, or healing a wound.",
        "description_hi": "ये शरीर के रक्षक (श्वेत रक्त कण) हैं। जब शरीर किसी सामान्य संक्रमण से लड़ रहा होता है या किसी चोट से उबर रहा होता है, तो इनकी संख्या बढ़ जाती है।",
        "benign_factors_en": "Recent cold, mild sore throat, allergy flare-up, or emotional stress.",
        "benign_factors_hi": "हाल ही में हुआ जुकाम, गले में खराश, एलर्जी या मानसिक तनाव।",
        "questions_en": [
            "Is this count consistent with a recent minor infection?",
            "Do the differential counts (neutrophils, lymphocytes) look balanced?"
        ],
        "questions_hi": [
            "क्या यह संख्या हाल के किसी सामान्य संक्रमण के कारण बढ़ी है?",
            "क्या डीएलसी (न्यूट्रोफिल्स, लिम्फोसाइट्स) का अनुपात संतुलित है?"
        ]
    },
    "PLATELETS": {
        "canonical_name": "Platelet Count",
        "full_name": "Thrombocyte / Platelet Count",
        "loinc_code": "777-3",
        "aliases": ["platelet count", "platelets", "plt", "thrombocytes"],
        "category": "Complete Blood Count",
        "default_unit": "lakh/cumm",
        "description_en": "Tiny cell fragments that help your blood clot to prevent excessive bleeding when you get a cut or scrape.",
        "description_hi": "ये रक्त में मौजूद छोटे कण हैं जो चोट लगने पर खून का थक्का बनाकर रक्तस्राव रोकने में मदद करते हैं।",
        "benign_factors_en": "Recent viral fever (like dengue or viral flu), clumping in the test tube, or certain medications.",
        "benign_factors_hi": "हालिया वायरल बुखार (जैसे डेंगू या फ्लू), लैब ट्यूब में प्लेटलेट का जमना, या कुछ दवाएं।",
        "questions_en": [
            "Should I monitor this count with a repeat CBC test?",
            "Are there any warning signs (like unusual bruising or bleeding gums) I should look out for?"
        ],
        "questions_hi": [
            "क्या कुछ दिनों में दोबारा सीबीसी टेस्ट करवा कर इसे मॉनिटर करना चाहिए?",
            "क्या कोई ऐसे लक्षण हैं (जैसे मसूड़ों से खून आना या नीले निशान) जिन पर मुझे ध्यान देना चाहिए?"
        ]
    },
    "HBA1C": {
        "canonical_name": "HbA1c (Glycated Hemoglobin)",
        "full_name": "Glycosylated Hemoglobin A1c",
        "loinc_code": "4548-4",
        "aliases": ["hba1c", "glycated hemoglobin", "a1c", "glycosylated hb"],
        "category": "Diabetes & Metabolism",
        "default_unit": "%",
        "description_en": "Measures the percentage of your hemoglobin coated with sugar. It gives a reliable average picture of your blood sugar levels over the past 2 to 3 months, unaffected by what you ate yesterday.",
        "description_hi": "यह जांचती है कि आपकी रक्त कोशिकाओं पर कितनी शर्करा (शुगर) चिपकी हुई है। यह पिछले 2 से 3 महीनों के औसत ब्लड शुगर का सही अनुमान देती है, जिस पर सिर्फ कल के खाने का असर नहीं पड़ता।",
        "benign_factors_en": "Severe anemia or hemoglobin variants can slightly shift the percentage reading.",
        "benign_factors_hi": "गंभीर एनीमिया या हीमोग्लोबिन के कुछ प्रकार इस माप को थोड़ा प्रभावित कर सकते हैं।",
        "questions_en": [
            "What target HbA1c range should I aim for based on my age and lifestyle?",
            "Would a consultation with a dietitian help me plan my carbohydrate intake?"
        ],
        "questions_hi": [
            "मेरी उम्र और स्वास्थ्य के अनुसार मेरा लक्षित (टारगेट) HbA1c कितना होना चाहिए?",
            "क्या डाइट चार्ट या लाइफस्टाइल में बदलाव से इसे नियंत्रित किया जा सकता है?"
        ]
    },
    "FASTING_GLUCOSE": {
        "canonical_name": "Fasting Blood Sugar (FBS)",
        "full_name": "Plasma Fasting Glucose",
        "loinc_code": "1558-6",
        "aliases": ["fasting blood sugar", "fbs", "fasting glucose", "blood sugar fasting", "glucose fasting", "glucose"],
        "category": "Diabetes & Metabolism",
        "default_unit": "mg/dL",
        "description_en": "Measures glucose concentration in your blood after you haven't eaten for at least 8 to 10 hours overnight.",
        "description_hi": "रात भर (लगभग 8 से 10 घंटे) भूखे पेट रहने के बाद सुबह आपके खून में ग्लूकोज (शुगर) की मात्रा को मापता है।",
        "benign_factors_en": "Less than 8 hours of fasting, poor night's sleep, severe stress, or steroids.",
        "benign_factors_hi": "पूरे 8 घंटे का उपवास न होना, रात को नींद न आना, तनाव या स्टेरॉयड दवाएं।",
        "questions_en": [
            "Was my 8-10 hour fasting window adequate for this test?",
            "Do I need to check my post-meal (PP) glucose or an oral glucose tolerance test?"
        ],
        "questions_hi": [
            "क्या मेरा 8-10 घंटे का उपवास इस टेस्ट के लिए सही था?",
            "क्या मुझे खाने के बाद (पीपी) की शुगर भी चेक करवानी चाहिए?"
        ]
    },
    "CREATININE": {
        "canonical_name": "Serum Creatinine",
        "full_name": "Blood Creatinine Concentration",
        "loinc_code": "2160-0",
        "aliases": ["creatinine", "serum creatinine", "s. creatinine", "blood creatinine"],
        "category": "Kidney Function",
        "default_unit": "mg/dL",
        "description_en": "A normal waste product generated by muscle breakdown. Healthy kidneys filter almost all of it out into the urine.",
        "description_hi": "यह मांसपेशियों के सामान्य उपयोग से बनने वाला एक अपशिष्ट (कचरा) पदार्थ है। स्वस्थ गुर्दे (किडनी) इसे खून से छानकर पेशाब के रास्ते बाहर निकाल देते हैं।",
        "benign_factors_en": "Dehydration, very high protein or red meat meal the night before, or heavy bodybuilding workouts.",
        "benign_factors_hi": "शरीर में पानी की कमी, टेस्ट से पहले अधिक प्रोटीन या भारी कसरत।",
        "questions_en": [
            "What is my estimated Glomerular Filtration Rate (eGFR) based on this creatinine value?",
            "Could mild dehydration have temporarily elevated this number?"
        ],
        "questions_hi": [
            "इस क्रिएटिनिन के आधार पर मेरा eGFR (किडनी की कार्यक्षमता) कितना है?",
            "क्या केवल पानी कम पीने की वजह से यह थोड़ा बढ़ सकता है?"
        ]
    },
    "BLOOD_UREA": {
        "canonical_name": "Blood Urea / BUN",
        "full_name": "Blood Urea Nitrogen",
        "loinc_code": "3094-0",
        "aliases": ["blood urea", "urea", "bun", "blood urea nitrogen", "s. urea"],
        "category": "Kidney Function",
        "default_unit": "mg/dL",
        "description_en": "A compound formed in the liver when protein is metabolized. Kidneys excrete it into urine. It fluctuates with hydration status and dietary protein.",
        "description_hi": "प्रोटीन के पचने पर बनने वाला अपशिष्ट पदार्थ। यह पानी की कमी और खान-पान में प्रोटीन की मात्रा से जल्दी ऊपर-नीचे होता है।",
        "benign_factors_en": "Dehydration, high protein diet, intense exertion.",
        "benign_factors_hi": "पानी की कमी, ज्यादा प्रोटीन का सेवन, कठिन शारीरिक श्रम।",
        "questions_en": [
            "Is the ratio between my blood urea and creatinine balanced?",
            "Should I increase my daily water intake before re-checking?"
        ],
        "questions_hi": [
            "क्या यूरिया और क्रिएटिनिन का अनुपात सामान्य है?",
            "क्या पानी अधिक पीने से इसमें सुधार होगा?"
        ]
    },
    "URIC_ACID": {
        "canonical_name": "Serum Uric Acid",
        "full_name": "Blood Uric Acid Level",
        "loinc_code": "3084-1",
        "aliases": ["uric acid", "serum uric acid", "s. uric acid"],
        "category": "Kidney & Joints",
        "default_unit": "mg/dL",
        "description_en": "A waste product produced when the body breaks down purines found naturally in bodily cells and foods like lentils, spinach, and meat.",
        "description_hi": "शरीर में प्यूरीन नामक तत्वों के टूटने से बनने वाला एसिड। अधिक होने पर यह जोड़ों (विशेषकर पैर के अंगूठे) में यूरिक एसिड क्रिस्टल बना सकता है।",
        "benign_factors_en": "High purine diet (dal, rajma, seafood, beer), low hydration, or fasting.",
        "benign_factors_hi": "दालें, राजमा, मांसाहार या बीयर का अधिक सेवन, या पानी कम पीना।",
        "questions_en": [
            "Do I have any symptoms of joint stiffness or toe discomfort?",
            "What purine-rich foods should I moderate in my diet?"
        ],
        "questions_hi": [
            "क्या जोड़ों में दर्द या सूजन के कोई लक्षण हैं?",
            "आहार में कौन-सी दालें या खाद्य पदार्थ सीमित करने चाहिए?"
        ]
    },
    "CHOLESTEROL_TOTAL": {
        "canonical_name": "Total Cholesterol",
        "full_name": "Serum Total Cholesterol",
        "loinc_code": "2093-3",
        "aliases": ["total cholesterol", "cholesterol", "s. cholesterol", "cholesterol total"],
        "category": "Lipid Profile",
        "default_unit": "mg/dL",
        "description_en": "A waxy, fat-like substance found in all your body's cells. It is essential for producing cell membranes, vitamin D, and hormones.",
        "description_hi": "यह शरीर की सभी कोशिकाओं में पाया जाने वाला एक वसायुक्त (फैट जैसा) तत्व है। यह नई कोशिकाएं और हार्मोन बनाने के लिए जरूरी होता है।",
        "benign_factors_en": "Recent high-fat meal, genetics, age, and sedentary habits.",
        "benign_factors_hi": "तैलीय आहार, अनुवांशिकता, और शारीरिक गतिविधि की कमी।",
        "questions_en": [
            "What is the ratio between my good HDL cholesterol and bad LDL cholesterol?",
            "Can dietary adjustments and walking help bring this into the ideal range?"
        ],
        "questions_hi": [
            "मेरे अच्छे कोलेस्ट्रॉल (HDL) और खराब कोलेस्ट्रॉल (LDL) का अनुपात कैसा है?",
            "क्या रोज़ाना टहलने और खाने में बदलाव से इसे सामान्य रखा जा सकता है?"
        ]
    },
    "TRIGLYCERIDES": {
        "canonical_name": "Triglycerides",
        "full_name": "Serum Triglycerides",
        "loinc_code": "2571-8",
        "aliases": ["triglycerides", "tg", "s. triglycerides"],
        "category": "Lipid Profile",
        "default_unit": "mg/dL",
        "description_en": "The most common type of fat in your body. When you consume excess calories, carbs, or sugars, your body converts them into triglycerides for storage.",
        "description_hi": "यह खून में पाई जाने वाली वसा (फैट) का सबसे आम प्रकार है। जब हम आवश्यकता से अधिक मीठा, कार्बोहाइड्रेट या तली चीजें खाते हैं, तो शरीर उन्हें ट्राइग्लिसराइड्स में बदल देता है।",
        "benign_factors_en": "Recent sweet/refined carbs intake, alcohol, lack of fasting before blood draw.",
        "benign_factors_hi": "मीठे खाद्य पदार्थ, टेस्ट से पहले 12 घंटे का उपवास न रखना, व्यायाम न करना।",
        "questions_en": [
            "Was a 12-hour fast observed before this lipid draw?",
            "Can reducing refined sugars and daily brisk walking lower this level?"
        ],
        "questions_hi": [
            "क्या टेस्ट से पहले 12 घंटे का उपवास पूरा था?",
            "क्या मीठा कम करने और टहलने से यह सामान्य हो जाएगा?"
        ]
    },
    "HDL": {
        "canonical_name": "HDL Cholesterol (Good)",
        "full_name": "High-Density Lipoprotein",
        "loinc_code": "2085-9",
        "aliases": ["hdl", "hdl cholesterol", "good cholesterol"],
        "category": "Lipid Profile",
        "default_unit": "mg/dL",
        "description_en": "Known as 'good' cholesterol because it absorbs extra cholesterol from tissues and carries it back to the liver for clearance.",
        "description_hi": "इसे 'अच्छा कोलेस्ट्रॉल' कहा जाता है क्योंकि यह धमनियों से अतिरिक्त फैट को हटाकर लिवर तक पहुंचाता है। इसका अधिक होना हृदय के लिए अच्छा माना जाता है।",
        "benign_factors_en": "Regular aerobic exercise increases HDL; smoking or inactivity lowers it.",
        "benign_factors_hi": "नियमित व्यायाम से यह बढ़ता है; निष्क्रिय रहने से घटता है।",
        "questions_en": [
            "How can I safely raise my HDL level through cardio exercise and diet?",
            "Does my overall cholesterol-to-HDL ratio look reassuring?"
        ],
        "questions_hi": [
            "व्यायाम और स्वस्थ वसा (नट्स/अलसी) से HDL कैसे बढ़ाया जा सकता है?",
            "क्या मेरा कुल कोलेस्ट्रॉल अनुपात सुरक्षित है?"
        ]
    },
    "LDL": {
        "canonical_name": "LDL Cholesterol (Bad)",
        "full_name": "Low-Density Lipoprotein",
        "loinc_code": "2089-1",
        "aliases": ["ldl", "ldl cholesterol", "bad cholesterol"],
        "category": "Lipid Profile",
        "default_unit": "mg/dL",
        "description_en": "Referred to as 'bad' cholesterol because excessive amounts can gradually deposit in blood vessel walls.",
        "description_hi": "इसे 'खराब कोलेस्ट्रॉल' कहा जाता है क्योंकि बहुत अधिक मात्रा में होने पर यह रक्त धमनियों की दीवारों पर जम सकता है।",
        "benign_factors_en": "Saturated fats, trans fats, sedentary lifestyle.",
        "benign_factors_hi": "तले-भुने खाद्य पदार्थ, घी-मक्खन की अधिकता, वजन बढ़ना।",
        "questions_en": [
            "What is my personalized target LDL level based on family history?",
            "Do I need lifestyle intervention or lipid-lowering therapy?"
        ],
        "questions_hi": [
            "मेरी आयु और स्वास्थ्य के अनुसार मेरा आदर्श LDL लक्ष्य क्या है?",
            "क्या खान-पान और जीवनशैली बदलने से यह नियंत्रित हो जाएगा?"
        ]
    },
    "TSH": {
        "canonical_name": "TSH (Thyroid Stimulating Hormone)",
        "full_name": "Thyrotropin / Thyroid Stimulating Hormone",
        "loinc_code": "3016-3",
        "aliases": ["tsh", "thyroid stimulating hormone", "s. tsh", "serum tsh"],
        "category": "Thyroid Function",
        "default_unit": "uIU/mL",
        "description_en": "A chemical messenger produced by your brain's pituitary gland that gently tells your thyroid gland in your neck how much hormone to produce.",
        "description_hi": "यह मस्तिष्क की पिट्यूटरी ग्रंथि द्वारा बनाया जाने वाला हार्मोन है, जो गले में मौजूद थायरॉयड ग्रंथि को संकेत देता है कि उसे कितना हार्मोन बनाना है।",
        "benign_factors_en": "Time of day (TSH fluctuates naturally), recent illness, pregnancy, or high biotin (vitamin B7) supplement intake.",
        "benign_factors_hi": "दिन का समय (सुबह-शाम में बदलाव), हाल की बीमारी, गर्भावस्था, या बायोटिन सप्लीमेंट।",
        "questions_en": [
            "Should we also check Free T3 and Free T4 levels to complete the picture?",
            "Could my symptoms (fatigue or weight changes) be related to this reading?"
        ],
        "questions_hi": [
            "क्या पूरी स्थिति समझने के लिए Free T3 और Free T4 टेस्ट भी कराने चाहिए?",
            "क्या मेरी थकान या वजन में बदलाव इस रीडिंग से जुड़े हो सकते हैं?"
        ]
    },
    "VITAMIN_D": {
        "canonical_name": "Vitamin D (25-OH)",
        "full_name": "25-Hydroxyvitamin D Total",
        "loinc_code": "62292-8",
        "aliases": ["vitamin d", "vit d", "25-oh vitamin d", "vitamin d3", "25 hydroxy vitamin d"],
        "category": "Vitamins & Minerals",
        "default_unit": "ng/mL",
        "description_en": "A vital nutrient that helps your bones absorb calcium, supports immune defense, and keeps muscles functioning smoothly.",
        "description_hi": "यह हड्डियों को मजबूत रखने के लिए कैल्शियम सोखने, रोग प्रतिरोधक क्षमता बढ़ाने और मांसपेशियों को स्वस्थ रखने वाला जरूरी विटामिन है।",
        "benign_factors_en": "Limited outdoor sunlight exposure, sunscreen use, or indoor living.",
        "benign_factors_hi": "धूप में कम निकलना, घर के अंदर ज्यादा रहना या आहार में कमी।",
        "questions_en": [
            "Do I need a weekly or monthly Vitamin D supplement course?",
            "How much morning sun exposure is recommended for me?"
        ],
        "questions_hi": [
            "क्या मुझे विटामिन डी का कोई साप्ताहिक या मासिक सप्लीमेंट लेने की जरूरत है?",
            "मुझे रोज़ाना कितनी देर सुबह की धूप लेनी चाहिए?"
        ]
    },
    "VITAMIN_B12": {
        "canonical_name": "Vitamin B12",
        "full_name": "Serum Cyanocobalamin / Vitamin B12",
        "loinc_code": "2132-9",
        "aliases": ["vitamin b12", "vit b12", "b12", "cyanocobalamin"],
        "category": "Vitamins & Minerals",
        "default_unit": "pg/mL",
        "description_en": "Essential for nervous system health, brain function, and red blood cell formation. Predominantly found in dairy, eggs, and fortified foods.",
        "description_hi": "यह तंत्रिका तंत्र (नर्वस सिस्टम), दिमाग और लाल रक्त कोशिकाओं के निर्माण के लिए अत्यंत आवश्यक विटामिन है। शुद्ध शाकाहारी आहार में इसकी कमी अक्सर देखी जाती है।",
        "benign_factors_en": "Strict vegetarian/vegan diet without supplements, antacid medications reducing absorption.",
        "benign_factors_hi": "शुद्ध शाकाहारी भोजन, एंटासिड (गैस की दवाएं) अधिक लेना जिससे यह पच नहीं पाता।",
        "questions_en": [
            "Should I take an oral Vitamin B12 supplement?",
            "Could tingling in fingers or fatigue be connected to this level?"
        ],
        "questions_hi": [
            "क्या मुझे विटामिन बी12 का कोई सप्लीमेंट शुरू करना चाहिए?",
            "क्या हाथ-पैरों में झनझनाहट या सुस्ती इस कमी से जुड़ी हो सकती है?"
        ]
    },
    "ESR": {
        "canonical_name": "ESR (Erythrocyte Sedimentation Rate)",
        "full_name": "Westergren Sedimentation Rate",
        "loinc_code": "30341-2",
        "aliases": ["esr", "erythrocyte sedimentation rate"],
        "category": "Inflammation Marker",
        "default_unit": "mm/hr",
        "description_en": "Measures how quickly red blood cells settle at the bottom of a test tube. When there is inflammation, cells clump and settle faster.",
        "description_hi": "यह मापता है कि टेस्ट ट्यूब में लाल रक्त कोशिकाएं कितनी तेजी से नीचे बैठती हैं। शरीर में किसी भी सामान्य सूजन या संक्रमण में यह बढ़ जाता है।",
        "benign_factors_en": "Menstruation, pregnancy, minor joint soreness, mild dental or throat infection.",
        "benign_factors_hi": "मासिक धर्म, हल्का गले का संक्रमण या दांत का दर्द, जोड़ों की हल्की सूजन।",
        "questions_en": [
            "Is this ESR elevation linked to a recent minor infection or joint pain?",
            "Do you advise repeating it once I feel fully recovered?"
        ],
        "questions_hi": [
            "क्या यह हालिया सर्दी-जुकाम या जोड़ों के दर्द के कारण थोड़ा बढ़ा है?",
            "क्या ठीक होने के बाद इसे दोबारा देखना चाहिए?"
        ]
    }
}

def find_parameter_info(param_query: str) -> Optional[Dict[str, Any]]:
    """
    Finds curated medical dictionary information using standard name or LOINC aliases.
    e.g., 'ALT' or 'SGPT' -> matches SGPT entry.
    """
    if not param_query:
        return None
        
    query_clean = param_query.strip().lower()
    
    # Exact key match
    for key, data in PARAM_DICTIONARY.items():
        if key.lower() == query_clean:
            return data
            
    # Alias match
    for key, data in PARAM_DICTIONARY.items():
        for alias in data.get("aliases", []):
            if alias in query_clean or query_clean in alias:
                return data
                
    # Fallback generic parameter generator if test is uncatalogued
    # Still provides clean, reassuring explanations!
    clean_title = param_query.strip().title()
    return {
        "canonical_name": clean_title,
        "full_name": clean_title,
        "loinc_code": "Standard Lab Marker",
        "aliases": [clean_title.lower()],
        "category": "Diagnostic Investigation",
        "default_unit": "",
        "description_en": f"A diagnostic laboratory test measuring {clean_title}. The printed reference range indicates typical expected levels for healthy individuals.",
        "description_hi": f"यह {clean_title} की जांच है। रिपोर्ट पर दी गई संदर्भ सीमा (reference range) सामान्य स्वस्थ व्यक्ति के स्तर को दर्शाती है।",
        "benign_factors_en": "Everyday physiological variations, hydration levels, timing of meals, or physical activity.",
        "benign_factors_hi": "दिन का समय, पानी की मात्रा, भोजन और सामान्य शारीरिक गतिविधियां।",
        "questions_en": [
            f"What specific clinical insight does {clean_title} provide for my health?",
            "Could temporary lifestyle or dietary factors have influenced this number?"
        ],
        "questions_hi": [
            f"मेरे स्वास्थ्य के संदर्भ में {clean_title} की जांच का क्या महत्व है?",
            "क्या खान-पान या अस्थायी कारणों से इसमें कोई बदलाव आ सकता है?"
        ]
    }

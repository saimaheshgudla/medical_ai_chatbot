import re


def extract_values(text, required_features):

    extracted_data = {}

    patterns = {

        # ---------- ANEMIA ----------
        "Hemoglobin": [
            r"Hemoglobin\s*[:\|]?\s*(\d+\.?\d*)",
            r"Hb\s*[:\|]?\s*(\d+\.?\d*)"
        ],
        "MCV": [
            r"MCV\s*[:\|]?\s*(\d+\.?\d*)"
        ],
        "MCH": [
            r"MCH\b\s*[:\|]?\s*(\d+\.?\d*)"
        ],
        "MCHC": [
            r"MCHC\s*[:\|]?\s*(\d+\.?\d*)"
        ],

        # ---------- DIABETES ----------
        "Age": [
            r"(\d+)\s*Yrs\s*(?:Male|Female)?",
            r"Age[_]?\s*[:\|]?\s*(\d+)\s*(?:Yrs|Years|yr)?"
        ],
        "BMI": [
            r"(\d+\.\d+)\s*BMI",
            r"BMI\s*[:\|]?\s*(\d+\.?\d*)"
        ],
        "HbA1c": [
            r"HbAIc\s*[:\|]?\s*(\d+\.?\d*)",
            r"HbA1c\s*[:\|]?\s*(\d+\.?\d*)",
            r"Hb\s*A\s*[1I]\s*c\s*[:\|]?\s*(\d+\.?\d*)",
            r"glycated\s*h[ae]moglobin\s*[:\|]?\s*(\d+\.?\d*)"
        ],
        "Glucose": [
            r"Glucose\s*Fasting\s*[:\|]?\s*(\d+\.?\d*)",
            r"Fasting\s*(\d+)\s*mg",
            r"Fasting\s*Glucose\s*[:\|]?\s*(\d+\.?\d*)",
            r"Glucose\s*[:\|]?\s*(\d+\.?\d*)"
        ],
        "hypertension": [
            r"Hypertension\s+(Yes|No)",
            r"Hypertension\s*[:\|]?\s*(Yes|No|1|0)"
        ],
        "heart_disease": [
            r"Heart\s*Disease\s+(Yes|No)",
            r"Heart\s*Disease\s*[:\|]?\s*(Yes|No|1|0)"
        ]
    }

    yes_no_features = {"hypertension", "heart_disease"}

    for feature in required_features:

        pattern_list = patterns.get(feature, [])
        matched = False

        for pattern in pattern_list:

            match = re.search(
                pattern,
                text,
                re.IGNORECASE
            )

            if match:

                raw = match.group(1).strip()

                if feature in yes_no_features:
                    if raw.lower() == "yes":
                        extracted_data[feature] = 1.0
                    elif raw.lower() == "no":
                        extracted_data[feature] = 0.0
                    else:
                        extracted_data[feature] = float(raw)
                else:
                    extracted_data[feature] = float(raw)

                matched = True
                break

        if not matched:
            extracted_data[feature] = None

    return extracted_data


def check_missing_values(extracted_data):

    missing_features = []

    for feature, value in extracted_data.items():
        if value is None:
            missing_features.append(feature)

    return missing_features
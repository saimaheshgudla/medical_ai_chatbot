import re

def extract_values(text, required_features):
    extracted_data = {}
    patterns = {
        # ---------- ANEMIA ----------
        "Hemoglobin": r"Hemoglobin.*?(\d+\.?\d*)",
        "MCV": r"MCV.*?(\d+\.?\d*)",
        "MCH": r"MCH.*?(\d+\.?\d*)",
        "MCHC": r"MCHC.*?(\d+\.?\d*)",
        # ---------- DIABETES ----------
        "Age": r"Age.*?(\d+)",
        "BMI": r"BMI.*?(\d+\.?\d*)",
        "HbA1c": r"HbA1c.*?(\d+\.?\d*)",
        "Glucose": r"Glucose.*?(\d+\.?\d*)",
        "hypertension": r"hypertension.*?(\d+)",
        "heart_disease": r"heart_disease.*?(\d+)"
    }
    for feature in required_features:
        pattern = patterns.get(feature)
        if pattern:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                extracted_data[feature] = float(match.group(1))
            else:
                extracted_data[feature] = None
        else:
            extracted_data[feature] = None
    return extracted_data

def check_missing_values(extracted_data):
    missing_features = []
    for feature, value in extracted_data.items():
        if value is None:
            missing_features.append(feature)
    return missing_features
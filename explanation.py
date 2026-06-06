def explain_anemia(values, model_result):

    explanations = []
    precautions = []

    hb = values.get("Hemoglobin")
    mcv = values.get("MCV")
    mch = values.get("MCH")
    mchc = values.get("MCHC")

    if model_result == "No Anemia Detected":

        explanations.append("Based on your report, no anemia is detected.")
        explanations.append("Hemoglobin level appears normal.")
        explanations.append("MCV level appears normal.")
        explanations.append("MCH level appears normal.")
        explanations.append("MCHC level appears normal.")

        precautions.extend([
            "Maintain balanced nutrition.",
            "Stay hydrated.",
            "Monitor symptoms regularly."
        ])

        return explanations, precautions

    explanations.append("Based on your report, anemia is detected.")

    if hb is not None:
        if hb < 9:
            explanations.append("Hemoglobin level is critically low.")
            precautions.append("Please consult a doctor immediately.")
            precautions.append("Iron supplementation may be required.")
        elif hb < 12:
            explanations.append("Hemoglobin level is below normal.")
            precautions.append("Increase iron-rich foods.")
            precautions.append("Consume leafy vegetables and fruits.")
        else:
            explanations.append("Hemoglobin level appears normal.")

    if mcv is not None:
        if mcv < 80:
            explanations.append("MCV level is low, may indicate iron deficiency anemia.")
        elif mcv > 100:
            explanations.append("MCV level is high, may indicate B12 or folate deficiency.")
        else:
            explanations.append("MCV level appears normal.")

    if mch is not None:
        if mch < 27:
            explanations.append("MCH level is low, may indicate reduced hemoglobin in red blood cells.")
        else:
            explanations.append("MCH level appears normal.")

    if mchc is not None:
        if mchc < 32:
            explanations.append("MCHC level is below normal, may indicate hypochromic anemia.")
        else:
            explanations.append("MCHC level appears normal.")

    precautions.extend([
        "Maintain balanced nutrition.",
        "Avoid excessive junk food intake.",
        "Stay hydrated.",
        "Monitor symptoms regularly."
    ])

    seen = set()
    explanations = [x for x in explanations if not (x in seen or seen.add(x))]
    seen = set()
    precautions = [x for x in precautions if not (x in seen or seen.add(x))]

    return explanations, precautions


def explain_diabetes(values, model_result):

    explanations = []
    precautions = []

    hba1c = values.get("HbA1c")
    glucose = values.get("Glucose")
    bmi = values.get("BMI")
    hypertension = values.get("hypertension")
    heart_disease = values.get("heart_disease")

    if model_result == "No Diabetes Detected":

        explanations.append("Based on your report, no diabetes is detected.")
        explanations.append("HbA1c level appears normal.")
        explanations.append("Glucose level appears normal.")
        explanations.append("BMI appears normal.")

        precautions.extend([
            "Maintain healthy lifestyle.",
            "Avoid excessive sugar consumption.",
            "Drink sufficient water.",
            "Perform regular physical activity."
        ])

        return explanations, precautions

    explanations.append("Based on your report, diabetes is detected.")

    if hba1c is not None:
        if hba1c >= 8:
            explanations.append("HbA1c level is significantly high, indicating poorly controlled diabetes.")
            precautions.append("Please consult a doctor immediately.")
            precautions.append("Regular glucose monitoring is recommended.")
        elif hba1c >= 6.5:
            explanations.append("HbA1c level indicates diabetes.")
            precautions.append("Reduce sugar intake.")
            precautions.append("Exercise regularly.")
        elif hba1c >= 5.7:
            explanations.append("HbA1c level indicates prediabetes range.")
            precautions.append("Maintain healthy diet and exercise.")
        else:
            explanations.append("HbA1c level appears normal.")

    if glucose is not None:
        if glucose >= 200:
            explanations.append("Glucose level is very high.")
            precautions.append("Immediate medical consultation is recommended.")
        elif glucose >= 126:
            explanations.append("Glucose level is above normal.")
        elif glucose >= 100:
            explanations.append("Glucose level is slightly elevated.")
        else:
            explanations.append("Glucose level appears normal.")

    if bmi is not None:
        if bmi >= 30:
            explanations.append("BMI indicates obesity.")
            precautions.append("Weight management is strongly recommended.")
        elif bmi >= 25:
            explanations.append("BMI indicates overweight condition.")
        elif bmi < 18.5:
            explanations.append("BMI indicates underweight condition.")
        else:
            explanations.append("BMI appears normal.")

    if hypertension == 1:
        explanations.append("Patient history indicates hypertension.")
        precautions.append("Regular blood pressure monitoring is recommended.")

    if heart_disease == 1:
        explanations.append("Patient history indicates heart disease.")
        precautions.append("Regular cardiac evaluation is recommended.")

    precautions.extend([
        "Maintain healthy lifestyle.",
        "Avoid excessive sugar consumption.",
        "Drink sufficient water.",
        "Perform regular physical activity."
    ])

    seen = set()
    explanations = [x for x in explanations if not (x in seen or seen.add(x))]
    seen = set()
    precautions = [x for x in precautions if not (x in seen or seen.add(x))]

    return explanations, precautions
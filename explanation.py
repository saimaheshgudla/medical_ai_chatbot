# =====================================================
# ANEMIA EXPLANATION
# =====================================================

def explain_anemia(values):

    explanations = []

    precautions = []

    # =================================================
    # GET VALUES
    # =================================================

    hb = values.get("Hemoglobin")

    mcv = values.get("MCV")

    mch = values.get("MCH")

    mchc = values.get("MCHC")

    # =================================================
    # HEMOGLOBIN ANALYSIS
    # =================================================

    if hb is not None:

        if hb < 9:

            explanations.append(
                "Hemoglobin level is critically low."
            )

            explanations.append(
                "This may indicate severe anemia."
            )

            precautions.append(
                "Please consult a doctor immediately."
            )

            precautions.append(
                "Iron supplementation may be required."
            )

        elif hb < 12:

            explanations.append(
                "Hemoglobin level is below normal."
            )

            explanations.append(
                "This may indicate mild or moderate anemia."
            )

            precautions.append(
                "Increase iron-rich foods."
            )

            precautions.append(
                "Consume leafy vegetables and fruits."
            )

        else:

            explanations.append(
                "Hemoglobin level appears normal."
            )

    # =================================================
    # MCV ANALYSIS
    # =================================================

    if mcv is not None:

        if mcv < 80:

            explanations.append(
                "MCV level is low."
            )

            explanations.append(
                "This may indicate iron deficiency anemia."
            )

        elif mcv > 100:

            explanations.append(
                "MCV level is high."
            )

            explanations.append(
                "This may indicate vitamin B12 or folate deficiency."
            )

        else:

            explanations.append(
                "MCV level appears normal."
            )

    # =================================================
    # MCH ANALYSIS
    # =================================================

    if mch is not None:

        if mch < 27:

            explanations.append(
                "MCH level is slightly low."
            )

            explanations.append(
                "This may indicate reduced hemoglobin in red blood cells."
            )

        else:

            explanations.append(
                "MCH level appears normal."
            )

    # =================================================
    # MCHC ANALYSIS
    # =================================================

    if mchc is not None:

        if mchc < 32:

            explanations.append(
                "MCHC level is below normal."
            )

            explanations.append(
                "This may indicate hypochromic anemia."
            )

        else:

            explanations.append(
                "MCHC level appears normal."
            )

    # =================================================
    # GENERAL PRECAUTIONS
    # =================================================

    precautions.extend([

        "Maintain balanced nutrition.",

        "Avoid excessive junk food intake.",

        "Stay hydrated.",

        "Monitor symptoms regularly."
    ])

    # REMOVE DUPLICATES
    precautions = list(set(precautions))

    explanations = list(set(explanations))

    return explanations, precautions


# =====================================================
# DIABETES EXPLANATION
# =====================================================

def explain_diabetes(values):

    explanations = []

    precautions = []

    # =================================================
    # GET VALUES
    # =================================================

    hba1c = values.get("HbA1c")

    glucose = values.get("Glucose")

    bmi = values.get("BMI")

    hypertension = values.get("hypertension")

    heart_disease = values.get("heart_disease")

    # =================================================
    # HBA1C ANALYSIS
    # =================================================

    if hba1c is not None:

        if hba1c >= 8:

            explanations.append(
                "HbA1c level is significantly high."
            )

            explanations.append(
                "This may indicate poorly controlled diabetes."
            )

            precautions.append(
                "Please consult a doctor immediately."
            )

            precautions.append(
                "Regular glucose monitoring is recommended."
            )

        elif hba1c >= 6.5:

            explanations.append(
                "HbA1c level indicates diabetes."
            )

            precautions.append(
                "Reduce sugar intake."
            )

            precautions.append(
                "Exercise regularly."
            )

        elif hba1c >= 5.7:

            explanations.append(
                "HbA1c level indicates prediabetes."
            )

            precautions.append(
                "Maintain healthy diet and exercise."
            )

        else:

            explanations.append(
                "HbA1c level appears normal."
            )

    # =================================================
    # GLUCOSE ANALYSIS
    # =================================================

    if glucose is not None:

        if glucose >= 200:

            explanations.append(
                "Glucose level is very high."
            )

            precautions.append(
                "Immediate medical consultation is recommended."
            )

        elif glucose >= 140:

            explanations.append(
                "Glucose level is above normal."
            )

        else:

            explanations.append(
                "Glucose level appears normal."
            )

    # =================================================
    # BMI ANALYSIS
    # =================================================

    if bmi is not None:

        if bmi >= 30:

            explanations.append(
                "BMI indicates obesity."
            )

            precautions.append(
                "Weight management is strongly recommended."
            )

        elif bmi >= 25:

            explanations.append(
                "BMI indicates overweight condition."
            )

        elif bmi < 18.5:

            explanations.append(
                "BMI indicates underweight condition."
            )

        else:

            explanations.append(
                "BMI appears normal."
            )

    # =================================================
    # HYPERTENSION ANALYSIS
    # =================================================

    if hypertension == 1:

        explanations.append(
            "Patient history indicates hypertension."
        )

        precautions.append(
            "Regular blood pressure monitoring is recommended."
        )

    # =================================================
    # HEART DISEASE ANALYSIS
    # =================================================

    if heart_disease == 1:

        explanations.append(
            "Patient history indicates heart disease."
        )

        precautions.append(
            "Regular cardiac evaluation is recommended."
        )

    # =================================================
    # GENERAL PRECAUTIONS
    # =================================================

    precautions.extend([

        "Maintain healthy lifestyle.",

        "Avoid excessive sugar consumption.",

        "Drink sufficient water.",

        "Perform regular physical activity."
    ])

    # REMOVE DUPLICATES
    precautions = list(set(precautions))

    explanations = list(set(explanations))

    return explanations, precautions
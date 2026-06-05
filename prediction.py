import joblib
import numpy as np


# =====================================================
# LOAD MODELS
# =====================================================

anemia_model = joblib.load(
    "models/anemia_model.pkl"
)

diabetes_model = joblib.load(
    "models/diabetes_model.pkl"
)


# =====================================================
# LOAD SCALERS
# =====================================================

anemia_scaler = joblib.load(
    "models/anemia_scaler.pkl"
)

diabetes_scaler = joblib.load(
    "models/diabetes_scaler.pkl"
)


# =====================================================
# ANEMIA PREDICTION
# =====================================================

def predict_anemia(values):

    # Prepare input
    input_data = [[
        values["Hemoglobin"],
        values["MCV"],
        values["MCH"],
        values["MCHC"]
    ]]

    # Scale input
    scaled_data = anemia_scaler.transform(
        input_data
    )

    # Predict
    prediction = anemia_model.predict(
        scaled_data
    )

    # Result
    if prediction[0] == 1:

        return "Anemia Detected"

    else:

        return "No Anemia Detected"


# =====================================================
# DIABETES PREDICTION
# =====================================================

def predict_diabetes(values):

    # Prepare input
    input_data = [[
        values["Age"],
        values["BMI"],
        values["HbA1c"],
        values["Glucose"],
        values["hypertension"],
        values["heart_disease"]
    ]]

    # Scale input
    scaled_data = diabetes_scaler.transform(
        input_data
    )

    # Predict
    prediction = diabetes_model.predict(
        scaled_data
    )

    # Result
    if prediction[0] == 1:

        return "Diabetes Detected"

    else:

        return "No Diabetes Detected"
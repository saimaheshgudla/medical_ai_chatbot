import joblib
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

anemia_model = joblib.load(
    os.path.join(BASE_DIR, "models/anemia_model.pkl")
)

diabetes_model = joblib.load(
    os.path.join(BASE_DIR, "models/diabetes_model.pkl")
)

anemia_scaler = joblib.load(
    os.path.join(BASE_DIR, "models/anemia_scaler.pkl")
)

diabetes_scaler = joblib.load(
    os.path.join(BASE_DIR, "models/diabetes_scaler.pkl")
)


def predict_anemia(values):

    hb = values.get("Hemoglobin")

    if hb is not None:
        if hb >= 12:
            return "No Anemia Detected"
        if hb < 9:
            return "Anemia Detected"

    input_data = [[
        values["Hemoglobin"],
        values["MCV"],
        values["MCH"],
        values["MCHC"]
    ]]

    scaled_data = anemia_scaler.transform(input_data)
    prediction = anemia_model.predict(scaled_data)

    if prediction[0] == 1:
        return "Anemia Detected"
    else:
        return "No Anemia Detected"


def predict_diabetes(values):

    hba1c = values.get("HbA1c")
    glucose = values.get("Glucose")

    if hba1c is not None and glucose is not None:
        if hba1c >= 6.5 or glucose >= 126:
            return "Diabetes Detected"
        if hba1c < 5.7 and glucose < 100:
            return "No Diabetes Detected"

    input_data = [[
        values["Age"],
        values["BMI"],
        values["HbA1c"],
        values["Glucose"],
        values["hypertension"],
        values["heart_disease"]
    ]]

    scaled_data = diabetes_scaler.transform(input_data)
    prediction = diabetes_model.predict(scaled_data)

    if prediction[0] == 1:
        return "Diabetes Detected"
    else:
        return "No Diabetes Detected"
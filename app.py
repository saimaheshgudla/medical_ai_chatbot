from flask import Flask, render_template, request
import os
import sys

sys.path.insert(
    0,
    os.path.dirname(os.path.abspath(__file__))
)

from ocr_extractor import extract_text
from value_extractor import extract_values, check_missing_values
from prediction import predict_anemia, predict_diabetes
from explanation import explain_anemia, explain_diabetes

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    chatbot_message = None
    explanations = []
    precautions = []
    missing_values = []
    disease_type = ""

    extracted_values = {
        "Age": None,
        "BMI": None,
        "HbA1c": None,
        "Glucose": None,
        "Hemoglobin": None,
        "MCV": None,
        "MCH": None,
        "MCHC": None,
        "hypertension": None,
        "heart_disease": None
    }

    if request.method == "POST":

        disease_type = request.form.get("disease_type")

        if disease_type == "anemia":
            required_features = [
                "Hemoglobin", "MCV", "MCH", "MCHC"
            ]
        else:
            required_features = [
                "Age", "BMI", "HbA1c", "Glucose",
                "hypertension", "heart_disease"
            ]

        file = request.files.get("report")

        if file and file.filename != "":

            filepath = os.path.join(
                app.config["UPLOAD_FOLDER"],
                file.filename
            )

            file.save(filepath)
            text = extract_text(filepath)
            ocr_values = extract_values(text, required_features)

            for key, value in ocr_values.items():
                if value is not None:
                    extracted_values[key] = value

        for feature in extracted_values.keys():

            user_value = request.form.get(feature)

            if user_value is not None and user_value.strip() != "":
                extracted_values[feature] = float(user_value)

        filtered_values = {
            key: extracted_values[key]
            for key in required_features
        }

        missing_values = check_missing_values(filtered_values)

        if len(missing_values) == 0:

            if disease_type == "anemia":

                result = predict_anemia(filtered_values)

                explanations, precautions = explain_anemia(
                    filtered_values, result
                )

            else:

                result = predict_diabetes(filtered_values)

                explanations, precautions = explain_diabetes(
                    filtered_values, result
                )

            if result in ("Diabetes Detected", "Anemia Detected"):

                chatbot_message = (
                    f"The uploaded medical values show patterns "
                    f"associated with {disease_type}. "
                    f"This is not a final diagnosis. "
                    f"Please consult a healthcare professional "
                    f"for proper medical evaluation."
                )

            else:

                chatbot_message = (
                    "The uploaded report values appear "
                    "mostly within normal ranges."
                )

    return render_template(
        "index.html",
        result=result,
        chatbot_message=chatbot_message,
        explanations=explanations,
        precautions=precautions,
        missing_values=missing_values,
        extracted_values=extracted_values,
        disease_type=disease_type
    )


if __name__ == "__main__":
    app.run(debug=True)
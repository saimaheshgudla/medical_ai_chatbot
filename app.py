from flask import Flask, render_template, request
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# =====================================================
# IMPORT OCR
# =====================================================
from ocr_extractor import extract_text

# =====================================================
# IMPORT VALUE EXTRACTION
# =====================================================
from value_extractor import extract_values, check_missing_values

# =====================================================
# IMPORT PREDICTOR
# =====================================================
from prediction import predict_anemia, predict_diabetes

# =====================================================
# IMPORT EXPLANATIONS
# =====================================================
from explanation import explain_anemia, explain_diabetes

# =====================================================
# FLASK APP
# =====================================================
app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# =====================================================
# HOME ROUTE
# =====================================================
@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    explanations = []
    precautions = []
    extracted_values = {}
    disease_type = None
    missing_values = []

    if request.method == "POST":

        disease_type = request.form.get("disease_type")
        file = request.files.get("report")

        if file:

            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)

            text = extract_text(filepath)

            if disease_type == "anemia":
                required_features = ["Hemoglobin", "MCV", "MCH", "MCHC"]
            else:
                required_features = ["Age", "BMI", "HbA1c", "Glucose", "hypertension", "heart_disease"]

            extracted_values = extract_values(text, required_features)
            missing_values = check_missing_values(extracted_values)

            for feature in missing_values:
                user_value = request.form.get(feature)
                if user_value:
                    extracted_values[feature] = float(user_value)

            if disease_type == "anemia":
                result = predict_anemia(extracted_values)
                explanations, precautions = explain_anemia(extracted_values)
            else:
                result = predict_diabetes(extracted_values)
                explanations, precautions = explain_diabetes(extracted_values)

    return render_template(
        "index.html",
        result=result,
        explanations=explanations,
        precautions=precautions,
        extracted_values=extracted_values,
        missing_values=missing_values,
        disease_type=disease_type
    )

# =====================================================
# RUN APP
# =====================================================
if __name__ == "__main__":
    app.run(debug=True)
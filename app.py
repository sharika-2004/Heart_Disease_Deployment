from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    features = np.array([
        data["age"],
        data["sex"],
        data["cp"],
        data["trestbps"],
        data["chol"],
        data["fbs"],
        data["restecg"],
        data["thalach"],
        data["exang"],
        data["oldpeak"],
        data["slope"],
        data["ca"],
        data["thal"]
    ]).reshape(1, -1)

    prediction = model.predict(features)[0]

    result = "Heart Disease Detected" if prediction == 1 else "No Heart Disease"

    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(debug=True)
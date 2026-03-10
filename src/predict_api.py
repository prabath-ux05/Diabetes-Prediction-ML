from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("model/diabetes_model.pkl", "rb"))

@app.route('/predict', methods=['POST'])
def predict():

    data = request.json

    features = [[
        data['Pregnancies'],
        data['Glucose'],
        data['BloodPressure'],
        data['SkinThickness'],
        data['Insulin'],
        data['BMI'],
        data['DiabetesPedigreeFunction'],
        data['Age']
    ]]

    prediction = model.predict(features)[0]

    result = "Diabetes Risk" if prediction==1 else "No Diabetes Risk"

    return jsonify({
        "prediction": int(prediction),
        "result": result
    })

if __name__ == "__main__":
    app.run(port=5000)
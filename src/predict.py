import joblib
import numpy as np

def predict_failure(temp, vib, curr):
    model = joblib.load("models/model.pkl")

    data = np.array([[temp, vib, curr]])
    prediction = model.predict(data)

    if prediction[0] == 1:
        return "Failure"
    else:
        return "Normal"
import joblib
import pandas as pd

# --------------------------
# Load Model
# --------------------------

model = joblib.load("models/fraud_model.pkl")
encoders = joblib.load("models/encoders.pkl")


# --------------------------
# Get dropdown values
# --------------------------

def get_dropdown_data():

    dropdowns = {}

    for column, encoder in encoders.items():

        dropdowns[column] = sorted(encoder.classes_.tolist())

    return dropdowns


# --------------------------
# Prediction
# --------------------------

def predict_transaction(data):

    sample = pd.DataFrame([data])

    for column, encoder in encoders.items():

        sample[column] = sample[column].astype(str)

        sample[column] = sample[column].apply(

            lambda x: x if x in encoder.classes_

            else encoder.classes_[0]

        )

        sample[column] = encoder.transform(sample[column])

    prediction = model.predict(sample)[0]

    probability = model.predict_proba(sample)[0]

    confidence = round(max(probability) * 100, 2)

    if prediction == 1:

        result = "Fraud"

    else:

        result = "Genuine"

    return result, confidence
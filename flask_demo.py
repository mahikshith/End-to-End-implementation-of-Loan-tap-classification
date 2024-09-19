import streamlit as st
import pandas as pd
import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)

# flask --app flask_demo.py run

# Load the model
model = pickle.load(open("classifier.pkl", "rb"))

# Encoding dictionary
encode_dict = {
    "gender": {"Male": 0, "Female": 1},
    "married": {"Married": 1, "Unmarried": 0},
    "credit_history": {"Cleared Debts": 1, "Uncleared Debts": 0}
}

# Flask API endpoint
@app.route('/predict', methods=['POST', 'GET'])
def predict_loan_eligibility():
    if request.method == 'POST':
        data = request.json
        gender = data.get('gender')
        married = data.get('married')
        applicant_income = data.get('applicant_income')
        loan_amount = data.get('loan_amount')
        credit_history = data.get('credit_history')

        # Encode categorical features
        gender = encode_dict["gender"][gender]
        married = encode_dict["married"][married]
        credit_history = encode_dict["credit_history"][credit_history]

        # Prepare data as a DataFrame
        new_data = pd.DataFrame({
            "Gender": [gender],
            "Married": [married],
            "ApplicantIncome": [applicant_income],
            "LoanAmount": [loan_amount],
            "Credit_History": [credit_history]
        })

        # Make prediction
        prediction = model.predict(new_data)[0]

        # Return prediction as JSON response
        return jsonify({'prediction': prediction})

    else:
        return "Please use POST method to send data."

if __name__ == '__main__':
    app.run(debug=True)
import streamlit as st
import pandas as pd
import pickle 
import sklearn

# Title and User Inputs
st.title("Loan Eligibility Classification App")

st.text("This is a demo to showcase the poc whether the model works or not.")

gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Marital Status", ["Married", "Unmarried"])
applicant_income = st.number_input("Applicant Income", min_value=0)
loan_amount = st.number_input("Loan Amount", min_value=0)
credit_history = st.selectbox("Credit History", ["Cleared Debts", "Uncleared Debts"])

# Load Model
model = pickle.load(open("classifier.pkl", "rb"))

# Encoding Dictionary
encode_dict = {
    "gender": {"Male": 0, "Female": 1},
    "married": {"Married": 1, "Unmarried": 0},
    "credit_history": {"Cleared Debts": 1, "Uncleared Debts": 0}
}

# Model Prediction Function
def predict_loan_eligibility(gender, married, applicant_income, loan_amount, credit_history):
    # Encode categorical features
    gender = encode_dict["gender"][gender]
    married = encode_dict["married"][married]
    credit_history = encode_dict["credit_history"][credit_history]

    # Prepare data as a DataFrame
    data = pd.DataFrame({
        "Gender": [gender],
        "Married": [married],
        "ApplicantIncome": [applicant_income],
        "LoanAmount": [loan_amount],
        "Credit_History": [credit_history]
    })

    # Make prediction
    prediction = model.predict(data)[0]

    # Display result based on prediction
    if prediction == 1:
        st.success("Congratulations! You are eligible for a loan.")
    else:
        st.error("Unfortunately, you are not eligible for a loan at this time.")

# Button and Prediction
if st.button("Predict Eligibility"):
    predict_loan_eligibility(gender, married, applicant_income, loan_amount, credit_history)
else:
    st.write("Fill in your details and click 'Predict Eligibility' to proceed.")
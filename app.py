
import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("loan_model.pkl")

st.title("🏦 Loan Risk Prediction System")

st.write("Enter Applicant Details")

# Numeric Inputs

person_age = st.number_input("Age", 18, 100, 25)

person_income = st.number_input("Annual Income", 1000, 1000000, 50000)

person_emp_exp = st.number_input("Employment Experience (Years)", 0, 50, 2)

loan_amnt = st.number_input("Loan Amount", 500, 100000, 10000)

loan_int_rate = st.number_input("Interest Rate (%)", 1.0, 30.0, 10.0)

cb_person_cred_hist_length = st.number_input(
    "Credit History Length",
    0,
    50,
    5
)

credit_score = st.number_input(
    "Credit Score",
    300,
    900,
    650
)

# Categorical Inputs

gender = st.selectbox(
    "Gender",
    ["female", "male"]
)

education = st.selectbox(
    "Education",
    [
        "Associate",
        "Bachelor",
        "Doctorate",
        "High School",
        "Master"
    ]
)

home = st.selectbox(
    "Home Ownership",
    [
        "MORTGAGE",
        "OWN",
        "RENT",
        "OTHER"
    ]
)

loan_intent = st.selectbox(
    "Loan Purpose",
    [
        "EDUCATION",
        "HOMEIMPROVEMENT",
        "MEDICAL",
        "PERSONAL",
        "VENTURE",
        "DEBTCONSOLIDATION"
    ]
)

default_history = st.selectbox(
    "Previous Loan Default",
    ["No", "Yes"]
)

# Feature Engineering

loan_percent_income = loan_amnt / person_income

loan_income_ratio = loan_amnt / person_income

income_per_credit = person_income / credit_score

# Predict Button

if st.button("Predict"):

    data = {
        'person_age':[person_age],
        'person_income':[person_income],
        'person_emp_exp':[person_emp_exp],
        'loan_amnt':[loan_amnt],
        'loan_int_rate':[loan_int_rate],
        'loan_percent_income':[loan_percent_income],
        'cb_person_cred_hist_length':[cb_person_cred_hist_length],
        'credit_score':[credit_score],
        'loan_income_ratio':[loan_income_ratio],
        'income_per_credit':[income_per_credit],

        'person_gender_male':[1 if gender=="male" else 0],

        'person_education_Bachelor':[1 if education=="Bachelor" else 0],
        'person_education_Doctorate':[1 if education=="Doctorate" else 0],
        'person_education_High School':[1 if education=="High School" else 0],
        'person_education_Master':[1 if education=="Master" else 0],

        'person_home_ownership_OTHER':[1 if home=="OTHER" else 0],
        'person_home_ownership_OWN':[1 if home=="OWN" else 0],
        'person_home_ownership_RENT':[1 if home=="RENT" else 0],

        'loan_intent_EDUCATION':[1 if loan_intent=="EDUCATION" else 0],
        'loan_intent_HOMEIMPROVEMENT':[1 if loan_intent=="HOMEIMPROVEMENT" else 0],
        'loan_intent_MEDICAL':[1 if loan_intent=="MEDICAL" else 0],
        'loan_intent_PERSONAL':[1 if loan_intent=="PERSONAL" else 0],
        'loan_intent_VENTURE':[1 if loan_intent=="VENTURE" else 0],

        'previous_loan_defaults_on_file_Yes':
        [1 if default_history=="Yes" else 0]
    }

    input_df = pd.DataFrame(data)

    prediction = model.predict(input_df)[0]

    if prediction == 1:
        st.error("⚠️ High Risk Applicant")
    else:
        st.success("✅ Low Risk Applicant")

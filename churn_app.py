import streamlit as st
import numpy as np
import joblib

# Load the trained model and scaler
model = joblib.load("churn_model.pkl")
scaler = joblib.load("scaler.pkl")

# Streamlit UI
st.title("Bank Customer Churn Prediction")
st.write("Enter customer details below to predict whether they will leave the bank.")

# Input Fields
credit_score = st.number_input("Credit Score",placeholder="enter a number btw 300 and 900")
gender = st.radio("Gender", ("Male", "Female"))
age = st.number_input("Age", min_value=18, max_value=100,step=1)
tenure = st.number_input("Tenure (Years at Bank)", min_value=0, max_value=10, step=1)
balance = st.number_input("Balance ($)", min_value=0.0,step=1000.0)
num_of_products = st.number_input("Number of Products", min_value=1, max_value=4,step=1)
has_cr_card = st.radio("Has Credit Card?", ("Yes", "No"))
is_active_member = st.radio("Is Active Member?", ("Yes", "No"))
estimated_salary = st.number_input("Estimated Salary ($)", min_value=0.0, step=1000.0)
geography = st.radio("Geography", ("France", "Germany", "Spain"))

# Convert Inputs
gender = 1 if gender == "Male" else 0
has_cr_card = 1 if has_cr_card == "Yes" else 0
is_active_member = 1 if is_active_member == "Yes" else 0
geo_germany = 1 if geography == "Germany" else 0
geo_spain = 1 if geography == "Spain" else 0

# Prepare Data for Prediction
new_customer = np.array([[credit_score, gender, age, tenure, balance, num_of_products,
                          has_cr_card, is_active_member, estimated_salary, geo_germany, geo_spain]])

new_customer_scaled = scaler.transform(new_customer)
prediction = model.predict(new_customer_scaled)

# Display Result
if st.button("Predict"):
    if prediction[0] == 1:
        st.error("The customer is likely to leave the bank.")
    else:
        st.success("The customer will stay with the bank.")

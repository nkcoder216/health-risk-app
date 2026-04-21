import streamlit as st
import pandas as pd

st.title("Health Risk Prediction App")

# Load Excel (use your correct sheet name)
df = pd.read_excel("health.xlsx", sheet_name="data")

# ---- USER INPUT ----
st.header("Enter Your Details")

age = st.number_input("Age", min_value=1)
weight = st.number_input("Weight (kg)", min_value=1.0)
height = st.number_input("Height (cm)", min_value=1.0)
sleep = st.number_input("Sleep Hours", min_value=0.0)

# ---- COEFFICIENTS (from your Excel regression) ----
intercept = 53.8217134
age_coef = -0.0033338
weight_coef = 0.34655456
height_coef = -0.3114916
sleep_coef = -0.0097981

# ---- PREDICTION ----
bmi = intercept + (age * age_coef) + (weight * weight_coef) + (height * height_coef) + (sleep * sleep_coef)

# ---- RISK LOGIC ----
if bmi < 18.5:
    risk = "Low"
elif bmi < 25:
    risk = "Medium"
else:
    risk = "High"

# ---- BUTTON ----
if st.button("Predict"):
    st.subheader("Result")
    st.success(f"Predicted BMI: {round(bmi, 2)}")
    st.success(f"Health Risk: {risk}")


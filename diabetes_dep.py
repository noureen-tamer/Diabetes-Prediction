
import pickle
import streamlit as st
import pandas as pd

# Load model
data = pickle.load(open(r"C:\Users\Basel\Documents\PROJECTS\Diabetes prediction and deployment\diabetes_model.sav", 'rb'))

# Set page config
st.set_page_config(page_title="Diabetes Prediction", layout="centered")

# Add custom background color and header style
st.markdown("""
    <style>
    .main {
        background-color: black;
        padding: 20px;
        border-radius: 10px;
    }
    .title {
        font-size: 40px;
        color: #4a4a4a;
        text-align: center;
        font-weight: bold;
    }
    .info-box {
        background-color: #dfe8f3;
        padding: 10px;
        border-radius: 8px;
        color: #333;
        margin-bottom: 20px;
    }
    </style>
    <div class="main">
        <div class="title">🩺 Diabetes Prediction</div>
        <div class="info-box">🔍 Easy Prediction for Diabetes Disease</div>
    </div>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.header("🛠️ Feature Selection")

# Input fields
Pregnancies = st.text_input("Pregnancies")
Glucose = st.text_input("Glucose")
BloodPressure = st.text_input("BloodPressure")
SkinThickness = st.text_input("SkinThickness")
BMI = st.text_input("BMI")
DiabetesPedigreeFunction = st.text_input("DiabetesPedigreeFunction")
Age = st.text_input("Age")

# Create DataFrame
newdata = pd.DataFrame({
    'Pregnancies': [Pregnancies],
    'Glucose': [Glucose],
    'BloodPressure': [BloodPressure],
    'SkinThickness': [SkinThickness],
    'BMI': [BMI],
    'DiabetesPedigreeFunction': [DiabetesPedigreeFunction],
    'Age': [Age]
}, index=[0])

# Predict button
butt = st.sidebar.button("🔮 Predict")
if butt:
    prediction = data.predict(newdata)
    if prediction == 0:
        st.success("✅ The patient is **Healthy**")
    else:
        st.error("⚠️ The patient is **Diabetic**")
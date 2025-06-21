import streamlit as st
import numpy as np
import joblib

# Load trained model
model = joblib.load("model.pkl")

st.title("🛌 Sleep Quality Predictor")
st.markdown("Enter your lifestyle habits to predict sleep quality score (1–10)")

screen_time = st.slider("Daily Screen Time (hours)", 0.0, 12.0, 6.0, 0.5)
meals = st.slider("Number of Meals per Day", 1, 5, 3)
bedtime = st.slider("Bedtime (24-hour format)", 0.0, 23.99, 22.5, 0.25)
wake_time = st.slider("Wake-up Time (24-hour format)", 0.0, 12.0, 7.0, 0.25)
activity = st.slider("Physical Activity Level", 1, 5, 3)
stress = st.slider("Stress Level", 1, 5, 2)

if st.button("Predict Sleep Quality"):
    input_data = np.array([[screen_time, meals, bedtime, wake_time, activity, stress]])
    prediction = model.predict(input_data)[0]
    st.success(f"🛏 Predicted Sleep Quality Score: *{round(prediction, 2)} / 10*")

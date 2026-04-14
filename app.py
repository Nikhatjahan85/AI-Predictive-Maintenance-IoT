import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt

# Load model
model = joblib.load("models/model.pkl")

# Title
st.title("AI Predictive Maintenance Dashboard")
st.write("Enter sensor values to predict machine failure")

# Sliders (Inputs)
temperature = st.slider("Temperature (°C)", 0, 120, 70)
vibration = st.slider("Vibration", 0, 10, 2)
current = st.slider("Current (A)", 0, 20, 4)

# Predict button
if st.button("Predict"):
    input_data = [[temperature, vibration, current]]
    result = model.predict(input_data)[0]

    if result == 1:
        st.error("Machine Failure Detected!")
        st.write("Prediction: Failure")
    else:
        st.success("Machine Running Normally")
        st.write("Prediction: Normal")

# -------------------------------
#  Graph Section
# -------------------------------

st.subheader("Data Visualizations")

# Load dataset
df = pd.read_csv("data/iot_sensor_data.csv")

# Graph 1: Temperature vs Failure
fig1, ax1 = plt.subplots()
ax1.scatter(df["temperature"], df["failure"])
ax1.set_xlabel("Temperature")
ax1.set_ylabel("Failure")
ax1.set_title("Failure vs Temperature")
st.pyplot(fig1)

# Graph 2: Vibration vs Failure
fig2, ax2 = plt.subplots()
ax2.scatter(df["vibration"], df["failure"])
ax2.set_xlabel("Vibration")
ax2.set_ylabel("Failure")
ax2.set_title("Failure vs Vibration")
st.pyplot(fig2)
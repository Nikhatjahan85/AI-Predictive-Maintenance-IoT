# AI Predictive Maintenance System (IoT + Machine Learning)

An end-to-end Machine Learning project that predicts industrial machine failures using IoT sensor data and provides real-time insights through an interactive dashboard.


## Problem Statement

Unexpected machine failures in industries lead to:
• Production downtime  
• High maintenance costs  
• Safety risks  

This project solves the problem using Predictive Maintenance, where failures are predicted before they occur using sensor data.


## Solution

This system uses IoT sensor data such as:
• Temperature  
• Vibration  
• Current  

A Random Forest Machine Learning model is trained to classify:
• Normal Operation  
• Potential Machine Failure  


## Key Features

• Data preprocessing and cleaning pipeline  
• Machine Learning model (Random Forest Classifier)  
• Performance evaluation (classification report)  
• Real-time prediction system  
• IoT data simulation (step-by-step sensor streaming)  
• Interactive dashboard using Streamlit  
• Data visualization (Temperature vs Failure, etc.)  
• Logging system for predictions  


## Tech Stack

• Python  
• Pandas, NumPy  
• Scikit-learn  
• Matplotlib  
• Joblib  
• Streamlit  


## Project Structure

The project follows a modular and scalable structure for better maintainability and readability.

AI-Predictive-Maintenance-IoT/
│
├── data/
├── models/
├── outputs/
├── images/
├── src/
│   ├── preprocess.py
│   ├── train.py
│   ├── predict.py
│   ├── visualize.py
│   ├── simulator.py
│
├── app.py
├── main.py
├── requirements.txt
└── README.md


## How It Works

1. Data is loaded and cleaned  
2. Model is trained using historical sensor data  
3. Model is saved using Joblib  
4. New sensor data is passed for prediction  
5. Dashboard displays results in real-time  

## How to Run

### 1. Clone repository
git clone https://github.com/Nikhatjahan85/AI-Predictive-Maintenance-IoT.git
cd AI-Predictive-Maintenance-IoT

### 2. Install dependencies
pip install -r requirements.txt

### 3. Train the model
python train.py

### 4. Run the dashboard
streamlit run app.py



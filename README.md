# AI-Driven-Predictive-Maintenance-Dashboard
This Streamlit app uses sensor data and machine learning to predict equipment failures in a manufacturing environment. Filter by date, machine ID, or operation mode, visualize sensor trends, and download maintenance alerts with severity levels. Built with real-time AI alert logic for smart decision-making.

# 🛠️ Predictive Maintenance Dashboard

This Streamlit dashboard uses sensor data and machine learning to predict potential equipment failures in a manufacturing environment. It supports data upload, real-time filtering, visualization, and AI-powered maintenance alerts.

## 📂 Features

- 📁 Upload your own CSV dataset
- 📅 Filter data by date range, operation mode, and machine ID
- 📊 Visualize sensor trends:
  - Temperature
  - Vibration
  - Power consumption
  - Network latency
  - Defect rate
- ⚠️ Get AI-powered alerts when machines show failure risk
- 🔽 Download predictions with severity levels

## 🧠 AI Logic

- Trained Random Forest classifier on sensor features
- Custom failure alert logic:
  - `Vibration > 3.5 Hz` and `Temperature > 75°C`
  - Maintenance score threshold > 0.7

## 📤 How to Use

1. Upload a CSV file containing your machine data
2. Use the filters to explore specific machines
3. View real-time failure alerts and download the results

## 📄 Sample Columns Expected

Make sure your CSV file includes at least:

- `Timestamp`, `Machine_ID`, `Operation_Mode`
- `Temperature_C`, `Vibration_Hz`, `Power_Consumption_kW`
- `Predictive_Maintenance_Score`, `Error_Rate_%`, etc.

---

## 📎 Author

Built by:**Praveen Shivaramu** 

LinkedIn: https://www.linkedin.com/in/praveen-shivaramu-a3a54b218/

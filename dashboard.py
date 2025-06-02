import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

st.title("Predictive Maintenance Dashboard")

uploaded_file = st.file_uploader("Upload your manufacturing dataset", type="csv", label_visibility="collapsed")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    threshold = 0.7
    df['Maintenance_Needed'] = (df['Predictive_Maintenance_Score'] > threshold).astype(int)

    features = [
        'Temperature_C', 'Vibration_Hz', 'Power_Consumption_kW', 'Network_Latency_ms',
        'Packet_Loss_%', 'Quality_Control_Defect_Rate_%', 'Production_Speed_units_per_hr',
        'Error_Rate_%'
    ]

    X = df[features]
    y = df['Maintenance_Needed']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    clf = RandomForestClassifier(n_estimators=50, random_state=42)
    clf.fit(X_train, y_train)

    df['Maintenance_Prediction'] = clf.predict(X)
    df['Prediction_Prob'] = clf.predict_proba(X)[:, 1]

    df['Alert'] = df['Maintenance_Prediction'].apply(lambda x: "⚠️" if x == 1 else "")
    df['Severity'] = df['Prediction_Prob'].apply(lambda x: "🔴 High" if x > 0.9 else ("🟠 Medium" if x > 0.75 else "🟢 Low"))

    # AI-style logic
    df['AI_Condition_Alert'] = df.apply(lambda row: "⚠️" if row['Vibration_Hz'] > 3.5 and row['Temperature_C'] > 75 else "", axis=1)

    # Filters
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    min_date = df['Timestamp'].min().date()
    max_date = df['Timestamp'].max().date()
    date_range = st.date_input("Filter by Date Range", [min_date, max_date])
    mode_filter = st.selectbox("Filter by Operation Mode", ['All'] + sorted(df['Operation_Mode'].unique()))

    df_filtered = df[(df['Timestamp'].dt.date >= date_range[0]) & (df['Timestamp'].dt.date <= date_range[1])]
    if mode_filter != 'All':
        df_filtered = df_filtered[df_filtered['Operation_Mode'] == mode_filter]

    machine_ids = df_filtered['Machine_ID'].unique()
    selected_id = st.selectbox("Select Machine ID", machine_ids)
    df_selected = df_filtered[df_filtered['Machine_ID'] == selected_id]

    if df['Maintenance_Prediction'].sum() > 0:
        st.warning("⚠️ ALERT: Potential machine failure(s) detected!", icon="⚠️")

    st.subheader("Sensor Trends")
    st.plotly_chart(px.line(df_selected, x='Timestamp', y='Temperature_C', title='Temperature Over Time'))
    st.plotly_chart(px.line(df_selected, x='Timestamp', y='Vibration_Hz', title='Vibration Over Time'))
    st.plotly_chart(px.line(df_selected, x='Timestamp', y='Power_Consumption_kW', title='Power Consumption Over Time'))
    st.plotly_chart(px.line(df_selected, x='Timestamp', y='Network_Latency_ms', title='Network Latency Over Time'))
    st.plotly_chart(px.line(df_selected, x='Timestamp', y='Quality_Control_Defect_Rate_%', title='Defect Rate Over Time'))

    st.subheader("Maintenance Alerts")
    alerts = df_filtered[df_filtered['Maintenance_Prediction'] == 1]
    st.write(f"⚠️ Machines Needing Maintenance: {alerts['Machine_ID'].nunique()}")
    st.dataframe(alerts[['Timestamp', 'Machine_ID', 'Temperature_C', 'Vibration_Hz', 'Severity', 'Alert', 'AI_Condition_Alert']])

    st.download_button("Download Predictions", df_filtered.to_csv(index=False), file_name="predictions.csv")

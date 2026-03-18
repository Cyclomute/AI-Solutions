import streamlit as st
import joblib
import numpy as np

# Load model and scaler
model = joblib.load("extra_trees_model.pkl")
scaler = joblib.load("scaler.pkl")

# Page config
st.set_page_config(page_title="5G Throughput Predictor", layout="wide")

# Title
st.title("📡 5G Throughput Predictor Dashboard")
st.markdown("Predict downlink throughput using key 5G NR radio features.")

# Sidebar inputs
st.sidebar.header("📥 Input 5G Parameters")

data_volume = st.sidebar.number_input("DL Data Volume (MB)", min_value=0.0, value=4172.0)

avg_cqi = st.sidebar.number_input("Average CQI (256QAM)", min_value=0.0, max_value=15.0, value=11.3)

excellent_cqi_rate = st.sidebar.slider("Excellent CQI Rate (%)", min_value=0.0, max_value=100.0, value=98.0)

cell_id = st.sidebar.number_input("NR Cell ID", min_value=0, value=101)

# Combine inputs into array
input_data = np.array([[data_volume, avg_cqi, excellent_cqi_rate, cell_id]])

# Scale input
input_scaled = scaler.transform(input_data)

# Prediction
if st.sidebar.button("🔍 Predict Throughput"):
    prediction = model.predict(input_scaled)

    st.subheader("📊 Prediction Result")
    st.success(f"Estimated Throughput: {prediction[0]:.2f} Mbps")

    # Additional insight
    if prediction[0] < 10:
        st.warning("⚠️ Low throughput detected. Possible poor radio conditions.")
    elif prediction[0] < 50:
        st.info("ℹ️ متوسط performance. Optimization may improve throughput.")
    else:
        st.success("✅ Good network performance detected.")

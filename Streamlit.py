import streamlit as st
import numpy as np
import pickle

# Load model and encoder
with open('naive_bayes_crop_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('label_encoder.pkl', 'rb') as encoder_file:
    label_encoder = pickle.load(encoder_file)

# Set page config
st.set_page_config(page_title="🌱 Crop Recommendation System", page_icon="🌾", layout="centered")

# Background banner
st.markdown(
    """
    <style>
    .banner {
        background-color: #e0f7fa;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        margin:25px;
        margin-top:0px;
    }
    .banner h1,.banner p {
        color: #00796b;
        font-size: 40px;
    }
    .banner p{
    font-size: 20px;
    }
    .input-section {
        background-color: blue;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 0 20px rgba(0,0,0,0.08);
    }
    </style>
    <div class="banner">
        <h1>🌱 Smart Crop Recommendation</h1>
        <p>💡 Get the best crop based on soil and climate conditions</p>
    </div>
    """, unsafe_allow_html=True
)

# Input form UI
with st.form("input_form"):
    st.subheader("🧪 Enter Soil & Climate Details:")
    
    col1, col2 = st.columns(2)
    with col1:
        N = st.number_input("🌿 Nitrogen (N)", min_value=0.0)
        P = st.number_input("🌿 Phosphorus (P)", min_value=0.0)
        K = st.number_input("🌿 Potassium (K)", min_value=0.0)
        temperature = st.number_input("🌡️ Temperature (°C)", min_value=-10.0)

    with col2:
        humidity = st.number_input("💧 Humidity (%)", min_value=0.0, max_value=100.0)
        ph = st.number_input("⚗️ pH value", min_value=0.0, max_value=14.0)
        rainfall = st.number_input("🌧️ Rainfall (mm)", min_value=0.0)
    
    submitted = st.form_submit_button("🚀 Recommend Crop")

# Predict and display
if submitted:
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(input_data)
    predicted_crop = label_encoder.inverse_transform(prediction)[0]

    st.markdown("---")
    st.subheader("✅ Result")
    st.success(
    f"🌾 Based on the input, the recommended crop is: **{predicted_crop.upper()}**\n\n"
    f"🌱 So we recommend you to cultivate **{predicted_crop.capitalize()}** in your field, "
    "as it is best suited for the current soil and climate conditions. Ensure optimal irrigation, "
    "fertilization, and care based on this crop's requirements for maximum yield! 🚜"
)


    crop_key = predicted_crop.lower()
    

# Footer
st.markdown("""
---
<div style='text-align: center; font-size: 13px; color: grey;'>
    Developed by <strong>Sandeep,SHK</strong> 🌾 | Contact: sandeepreddybheema@gmail.com
</div>
""", unsafe_allow_html=True)

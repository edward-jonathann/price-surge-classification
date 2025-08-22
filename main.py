import streamlit as st
import pandas as pd
import numpy as np
import random

from machine_learning_assets import load_model
from encoders import load_encoders

# ====== Distance Simulation ======
def calculate_distance(origin, destination):
    # Mock distance lookup (replace with real geo-calculation if needed)
    base_distances = {
        ("Airport", "City"): 5.2,
        ("Airport", "Outstation"): 12.5,
        ("City", "Business District"): 25.1,
        ("Outstation", "Residential Area"): 40.3,
        ("Airport", "Residential Area"): 60.7,
        ("City", "Outstation"): 85.2,
        ("Business District", "Residential Area"): 109.23
    }
    return base_distances.get((origin, destination), random.uniform(2, 109.23))

def assign_destination_type(distance):
    if distance <= 20:
        return "A"
    elif distance <= 40:
        return "B"
    elif distance <= 60:
        return "C"
    elif distance <= 85:
        return "D"
    else:
        return "E"

def surge_pricing_prediction():
    # ====== Load model and encoders ======
    model, feature_names = load_model()
    encoders = load_encoders()

    gender_encoder = encoders["gender_encoder"]
    lifestyle_encoder = encoders["Confidence_Life_Style_Index_encoder"]
    destination_encoder = encoders["Destination_Type_encoder"]
    cab_encoder = encoders["Type_of_Cab_encoder"]
    scaler = encoders["MinMaxScaler"]

    # ====== Cab type mapping ======
    cab_mapping = {
        "Mini": "A",
        "Sedan": "B",
        "SUV": "C",
        "Luxury": "D",
        "Premium": "E"
    }

    # ====== Form ======
    with st.form("prediction_form"):
        st.header("🚕 Surge Pricing Prediction")

        gender = st.selectbox("Gender", ["Male", "Female"])
        cab_type = st.selectbox("Type of Cab", ["Mini", "Sedan", "SUV", "Luxury", "Premium"])
        customer_since_months = st.number_input("Customer Since (Months)", min_value=1, max_value=120, value=12)

        origin = st.selectbox("Origin", ["Airport", "City", "Outstation", "Business District", "Residential Area"])
        destination = st.selectbox("Destination", ["Airport", "City", "Outstation", "Business District", "Residential Area"])

        submitted = st.form_submit_button("Predict Surge Pricing")

    # ====== Prediction Logic ======
    if submitted:
        try:
            # Distance + Destination Type
            trip_distance = calculate_distance(origin, destination)
            destination_type = assign_destination_type(trip_distance)

            # Prepare DataFrame
            input_df = pd.DataFrame([{
                "Gender": gender,
                "Type_of_Cab": cab_type,
                "Customer_Since_Months": customer_since_months,
                "Trip_Distance": trip_distance,
                "Destination_Type": destination_type,
                # Randomized features
                "Life_Style_Index": random.randint(1, 5),
                "Confidence_Life_Style_Index": random.choice(["A", "B", "C"]),
                "Customer_Rating": round(random.uniform(1, 5), 1),
                "Cancellation_Last_1Month": random.randint(0, 3),
                "Var1": random.randint(0, 171),
                "Var2": random.randint(0, 101),
                "Var3": random.randint(0, 206),
            }])

            # ====== Encode categorical features ======
            input_df["Gender"] = gender_encoder.transform([input_df["Gender"][0]])
            input_df["Confidence_Life_Style_Index"] = lifestyle_encoder.transform(
                [input_df["Confidence_Life_Style_Index"][0]]
            )
            input_df["Destination_Type"] = destination_encoder.transform([input_df["Destination_Type"][0]])

            # Map cab type → A–E and encode
            cab_type_mapped = cab_mapping[cab_type]
            input_df["Type_of_Cab"] = cab_encoder.transform([cab_type_mapped])

            # ====== Scale numeric features (using scaler’s training columns) ======
            numeric_features = scaler.feature_names_in_
            input_df[numeric_features] = scaler.transform(input_df[numeric_features])

            # ====== Ensure correct feature order ======
            input_df = input_df[feature_names]

            # ====== Predict surge pricing ======
            prediction = model.predict(input_df)[0]

            surge_labels = {1: "Low Surge", 2: "Medium Surge", 3: "High Surge"}
            st.success(f"🚦 Predicted Surge Pricing Type: **{surge_labels.get(prediction, prediction)}**")
            st.info(f"Trip Distance: {trip_distance:.2f} KM | Destination Type: {destination_type}")

        except Exception as e:
            st.error("❌ Prediction failed.")
            st.write("Exception:", str(e))


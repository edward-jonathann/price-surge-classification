import streamlit as st


def project_overview():
    st.title("🚕 Surge Pricing Prediction — Machine Learning Project")
    st.subheader("By Edward Jonathan")

    st.markdown("""
    ## 👋 Self Introduction
    Hi, I’m Edward — a professional transitioning from Project Management & Business Development into **Data Science**.  
    I’m passionate about turning raw, messy data into **insights that help people make smarter choices**.

    ---
    ## 📌 Project Overview
    For this project, I worked on predicting **surge pricing in ride-hailing services** using Machine Learning.  
    Why? Because surge pricing often feels unpredictable — and a reliable model can help companies **optimize pricing** while also **improving customer trust**.

    ### 🔍 What I Did
    - Processed and cleaned ride-hailing data from an Indian cab aggregator service.
    - Engineered key features such as **trip distance, customer history, cab type, and lifestyle indices** to capture demand–supply dynamics.
    - Explored the data to uncover patterns:
        - **Cab type** strongly correlates with surge (Premium cabs surge more often).
        - **Longer trips** tend to face higher surge multipliers.
        - **Customer loyalty & ratings** impact surge sensitivity.
    - Built and tested multiple ML models, where **Gradient Boosting & Random Forest** delivered the best results with high predictive accuracy.

    ### 💡 Why This Matters
    This approach goes beyond ride-hailing — it can be applied to **dynamic pricing problems** in other industries like:
    - ✅ Airline & hotel bookings  
    - ✅ E-commerce promotions  
    - ✅ Logistics & delivery pricing  

    My skills in **data cleaning, feature engineering, exploratory analysis, and predictive modeling** can help businesses:
    - ✅ Model Optimization
    - ✅ Cleaning Data and Encoding
    - ✅ Insightful Analysis and Business Implementation
    """)

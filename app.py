import streamlit as st
from joblib import load
import pandas as pd

model = load('real_estate_model.joblib')

st.title("🏠 Real Estate Price Prediction")

total_sqft = st.number_input("Total Sqft", min_value=0.0)
bath = st.number_input("Bathrooms", min_value=0)
balcony = st.number_input("Balcony", min_value=0)
bhk = st.number_input("BHK", min_value=1)

if st.button("Predict Price"):
    try:
        # basic input
        input_data = pd.DataFrame([[total_sqft, bath, balcony, bhk]],
                                  columns=['total_sqft', 'bath', 'balcony', 'bhk'])

        # match model columns
        input_data = input_data.reindex(columns=model.feature_names_in_, fill_value=0)

        prediction = model.predict(input_data)

        st.success(f"Estimated Price: {prediction[0]:.2f} Lakhs")

    except Exception as e:
        st.error(f"Error: {e}")
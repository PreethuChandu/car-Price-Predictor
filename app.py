import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open("LinearRegressionModel.pkl", "rb"))

car_data = pd.read_csv("Cleaned_Car_data.csv")

st.title("Car Price Predictor ")

company = st.selectbox("Select Company", sorted(car_data['company'].unique()))

all_models = sorted(car_data[car_data['company'] == company]['name'].unique())
name = st.selectbox("Search or Select Car Model", all_models, index=0)

year = st.number_input("Car Year", min_value=1995, max_value=2025, step=1, value=2015)
kms_driven = st.number_input("Kilometers Driven", min_value=0, max_value=500000, step=1000, value=30000)
fuel_type = st.radio("Fuel Type", car_data['fuel_type'].unique())

if st.button("Predict Price"):
    sample = pd.DataFrame([[name, company, year, kms_driven, fuel_type]],
                          columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'])
    
    prediction = int(model.predict(sample)[0])
    st.success(f"💰 Estimated Price: ₹ {prediction:,}")
import streamlit as st
import pandas as pd
import pickle

# Load the model from the disk
with open('car_pred_model', 'rb') as f:
    model = pickle.load(f)

# Load dataset for demonstration
cars_df = pd.read_csv("./cars24-car-price.csv")

st.title("Cars Resale Price Prediction")
st.write("This site helps you estimate your car's resale value using a Machine Learning Model.")
st.dataframe(cars_df.head())

st.header("Enter the details about your car:")

# User input columns
col1, col2 = st.columns(2)

# Inputs for car details
year_of_make = col1.slider("Select the year of make:", 1990, 2023, step=1, value=2012)
mileage = col1.number_input("Enter the mileage (in kilometers):", min_value=0, max_value=500000, value=120000, step=1000)
fuel_type = col2.selectbox("Select the fuel type:", ["Diesel", "Petrol", "CNG", "LPG", "Electric"])
engine = col2.slider("Set the engine power (CC):", 700, 5000, step=100, value=1500)
transmission_type = col1.selectbox("Select the transmission type:", ["Manual", "Automatic"])
seats = col2.selectbox("Enter the number of seats:", [4, 5, 7, 9, 11])

# Encoding categorical features
encode_dict = {
    "fuel_type": {'Diesel': 1, 'Petrol': 2, 'CNG': 3, 'LPG': 4, 'Electric': 5},
    "seller_type": {'Dealer': 1, 'Individual': 2, 'Trustmark_Dealer': 3},
    "transmission_type": {'Manual': 1, 'Automatic': 2}
}

if st.button("Get Price"):
    # Encode categorical inputs
    encoded_fuel_type = encode_dict['fuel_type'][fuel_type]
    encoded_transmission_type = encode_dict['transmission_type'][transmission_type]

    # Input data for the prediction model
    input_data = [
        year_of_make,  # Year of make
        2,             # Owner type (default value in this case)
        mileage,       # Mileage (input by user)
        encoded_fuel_type,
        encoded_transmission_type,
        19.7,          # Mileage in km/l (example default value)
        engine,
        46.3,          # Power (example default value)
        seats
    ]

    # Predict resale price
    pred = model.predict([input_data])[0]
    st.header(":rainbow[Your car's price-prediction below:]")
    st.header(f"₹ {round(pred, 2)} Lakhs")

# Disclaimer
st.markdown("---")
st.markdown("""
<div style="background-color: #eef6fc; border-left: 6px solid #2b83ba; padding: 15px; border-radius: 5px; font-family: Arial, sans-serif;">
    <strong>Disclaimer</strong><br><br>
    This web app is created as part of an academic project and provides resale value predictions based on a machine learning model. The predictions are intended for informational purposes only.<br><br>
    The developer is not liable for any decisions made based on the app’s output. For precise car resale valuations, users should consult professional services.
</div>
""", unsafe_allow_html=True)

import streamlit as st
import pandas as pd
import pickle

# Load the model from the disk
with open('car_pred_model', 'rb') as f:
    model = pickle.load(f)

cars_df = pd.read_csv("./cars24-car-price.csv")

st.title("Cars Resale Price Prediction.")
st.write("This site helps you estimate your car's resale value using a Machine Learning Model.")
st.dataframe(cars_df.head())
st.markdown("---")

st.header("Just enter the details about your car:")

# Initialize session state for all inputs if not already initialized
if 'fuel_type' not in st.session_state:
    st.session_state['fuel_type'] = "Diesel"
if 'engine' not in st.session_state:
    st.session_state['engine'] = 700
if 'transmission_type' not in st.session_state:
    st.session_state['transmission_type'] = "Manual"
if 'seats' not in st.session_state:
    st.session_state['seats'] = 4
if 'km_driven' not in st.session_state:
    st.session_state['km_driven'] = 100
if 'year' not in st.session_state:
    st.session_state['year'] = 2010
if 'mileage' not in st.session_state:
    st.session_state['mileage'] = 25

# Columns for inputs
col1, col2, col3 = st.columns(3)

# Input fields with default values managed by session state
fuel_type = col1.selectbox("Select the fuel type:", ["Diesel", "Petrol", "CNG", "LPG", "Electric"], index=["Diesel", "Petrol", "CNG", "LPG", "Electric"].index(st.session_state['fuel_type']))
engine = col2.slider("Set the engine power/Displacement (CC):", 700, 5000, step=100, value=st.session_state['engine'])
transmission_type = col3.selectbox("Select the transmission type:", ["Manual", "Automatic"], index=["Manual", "Automatic"].index(st.session_state['transmission_type']))
seats = col1.selectbox("Enter the number of seats:", [4, 5, 6, 7, 8, 9, 10], index=[4, 5, 6, 7, 8, 9, 10].index(st.session_state['seats']))
km_driven = col2.number_input("Select/type the KM driven:", 100, 3800000, step=1, value=st.session_state['km_driven'])
year = col3.selectbox("Select the year:", list(range(2010, 2022)), index=list(range(2010, 2022)).index(st.session_state['year']))
mileage = col2.slider("Select the mileage:", 25, 120, step=5, value=st.session_state['mileage'])

# Update session state on input change
st.session_state['fuel_type'] = fuel_type
st.session_state['engine'] = engine
st.session_state['transmission_type'] = transmission_type
st.session_state['seats'] = seats
st.session_state['km_driven'] = km_driven
st.session_state['year'] = year
st.session_state['mileage'] = mileage

# Encoding categorical features
encode_dict = {
    "fuel_type": {'Diesel': 1, 'Petrol': 2, 'CNG': 3, 'LPG': 4, 'Electric': 5},
    "transmission_type": {'Manual': 1, 'Automatic': 2}
}

if st.button("Get Price"):
    # Call the model.predict() function
    encoded_fuel_type = encode_dict['fuel_type'][fuel_type]
    encoded_transmission_type = encode_dict['transmission_type'][transmission_type]

    input_data = [year, 2, km_driven, encoded_fuel_type, encoded_transmission_type, mileage, engine, 46.3, seats]

    pred = model.predict([input_data])[0]
    st.header(":rainbow[Your car's price-prediction below:]")
    st.header(round(pred, 2))
    st.write("In Lakhs.")

# Reset button
if st.button("Reset"):
    st.session_state['fuel_type'] = "Diesel"
    st.session_state['engine'] = 700
    st.session_state['transmission_type'] = "Manual"
    st.session_state['seats'] = 4
    st.session_state['km_driven'] = 100
    st.session_state['year'] = 2010
    st.session_state['mileage'] = 25
    st.experimental_rerun()

# Disclaimer
st.markdown("---")
st.markdown("""
<div style="background-color: #eef6fc; border-left: 6px solid #2b83ba; padding: 15px; border-radius: 5px; font-family: Arial, sans-serif;">
    <strong>Disclaimer</strong><br><br>
    This web app is created as part of an academic project and provides resale value predictions based on a Machine Learning model (Regression based). The predictions are intended for informational purposes only.<br><br>
    The developer is not liable for any decisions made based on the app’s output. For precise car resale valuations, users should consult professional services.
</div>
""", unsafe_allow_html=True)

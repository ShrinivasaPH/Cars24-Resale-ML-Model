import streamlit as st
import pandas as pd
import pickle

#load the model from the disk
with open('car_pred_model', 'rb') as f:
    model = pickle.load(f)


cars_df = pd.read_csv("./cars24-car-price.csv")

st.title("Cars Resale Price Prediction.")
st.write("This site helps you estimate your car's resale value using a Machine Learning Model.")
st.dataframe(cars_df.head())

st.header("Just enter the details about your car:")


col1, col2 = st.columns(2)

#dropdowns
fuel_type = col1.selectbox("Select the fuel type:", ["Diesel", "Petrol", "CNG", "LPG", "Electric"])
engine = col1.slider("Set the engine power:", 700,5000, step=100)
transmission_type = col2.selectbox("Select the transmission type:", ["Manual", "Automatic"])
seats = col2.selectbox("Enter the number of seats:", [4,5,7,9,11])
model_year = col1.selectbox("Enter the make-Year:", 1980,2024, step=1)
mileage = col1.slider("Enter the mileage:")
seller_type = col2.number_input("Enter the seller Type:", [1,2,3])
km_driven = col2.slider("Enter the mileage:")
max_power = col1.slider("Enter the max power:")

#Encoding categorical features
encode_dict = {
    "fuel_type": {'Diesel':1, 'Petrol':2, 'CNG':3, 'LPG':4, 'Electric':5},
    "seller_type": {'Dealer':1, 'Individual':2, 'Trustmark_Dealer':3},
    "transmission_type": {'Manual':1, 'Automatic':2}
}

if st.button("Get Price"):
    #call the model.predict() function
    encoded_fuel_type = encode_dict['fuel_type'][fuel_type]
    encoded_transmission_type = encode_dict['transmission_type'][transmission_type]
    encoded_seller_type = encode_dict["seller_type"][seller_type]

    input_data = [model_year,encoded_seller_type,km_driven,encoded_fuel_type, encoded_transmission_type,encoded_seller_type,engine,max_power,seats]

    pred = model.predict([input_data])
    st.header(":rainbow[Your car's price-prediction below:]")
    st.header(round(pred,2))
    st.write("In Lakhs.")

st.markdown("---")
st.header("Disclaimer:")
st.caption("This web app is created as part of an academic project and provides resale value predictions based on a Machine Learning model (Regression based). The predictions are intended for informational purposes only.")
st.caption("The developer is not liable for any decisions made based on the app’s output. For precise car resale valuations, users should consult professional services.")

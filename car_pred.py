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

    input_data = [2012.0,2,120000,encoded_fuel_type, encoded_transmission_type,19.7,engine,46.3,seats]

    pred = model.predict([input_data])[0]
    st.header(":rainbow[Your car's price-prediction below:]")
    st.header(round(pred,2))
    st.write("In Lakhs")

st.header("Disclaimer:")
st.caption("This web app was developed as part of an academic project and is for informational purposes only. The predicted resale values are based on a machine learning model and may not accurately reflect real-world market conditions.")
st.caption("The developer is not liable for any decisions made based on the app’s output. Users should consult professionals for reliable car resale valuations.")
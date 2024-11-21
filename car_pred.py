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
st.markdown("---")

st.header("Just enter the details about your car:")


col1, col2, col3 = st.columns(3)

#dropdowns
fuel_type = col1.selectbox("Select the fuel type:", ["Diesel", "Petrol", "CNG", "LPG", "Electric"])
engine = col2.slider("Set the engine power/Displacement (CC):", 800,5000, step=100)
transmission_type = col3.selectbox("Select the transmission type:", ["Manual", "Automatic"])
seats = col1.selectbox("Enter the number of seats:", [4,5,6,7,8,9,10])
km_driven = col2.number_input("Select/type the KM driven:", 100,3800000,step=1)
year = col3.selectbox("Select the year:",list(range(2005, 2022)))
mileage =  col2.slider("Select the mileage:", 10,120, step=1)

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

    #           year, individual, km_driven, fuel_type, transmmission_type, mileaege, engine, max_power, seats

    input_data = [year, 2, km_driven, encoded_fuel_type, encoded_transmission_type, mileage, engine, 46.3, seats]

    pred = model.predict([input_data])[0]
    st.header(":rainbow[Your car's price-prediction below:]")
    st.header(round(pred,2))
    st.write("In Lakhs.")

#Disclaimer
st.markdown("---")
st.markdown("""
<div style="background-color: #eef6fc; border-left: 6px solid #2b83ba; padding: 15px; border-radius: 5px; font-family: Arial, sans-serif;">
    <strong>Disclaimer</strong><br><br>
    This web app is created as part of an academic project and provides resale value predictions based on a Machine Learning model (Regression based). The predictions are intended for informational purposes only.<br><br>
    The developer is not liable for any decisions made based on the app’s output. For precise car resale valuations, users should consult professional services.
</div>
""", unsafe_allow_html=True)
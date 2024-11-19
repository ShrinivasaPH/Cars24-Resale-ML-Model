import streamlit as st
st.title("My Calculator")

def square(x):
    return x*x

number = st.number_input("Enter number to get its square: ") 

if st.button("Get Square"):
    res = square(number)
    st.header(res)

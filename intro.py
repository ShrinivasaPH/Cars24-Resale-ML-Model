import streamlit as st
st.title("My web app")
st.header("My custom header")
st.write("Learning streamlit")

agree  =st.checkbox("I agree with Mohit")

if agree:
    st.write("Great!")

genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],index=None,
    captions=[
        "Laugh out loud.",
        "Get the popcorn.",
        "Never stop learning.",
    ],
)

if genre == ":rainbow[Comedy]":
    st.header(":rainbow[You selected comedy.]")
elif genre == "***Drama***":
    st.header("***Dramatist! Hahahaha...!!!***")
elif genre == "Documentary :movie_camera:":
    st.header("You are knowledge-hungry! :movie_camera:")
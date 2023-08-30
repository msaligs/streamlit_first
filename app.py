import streamlit as st

st.title("my first streamlit app")
user_input = st.text_input("enter your name")
num_input = st.color_picker("choose color")

st.write("Hello ",user_input, num_input)
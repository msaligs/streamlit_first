import streamlit as st

st.title("Simple Calculator")
user_name = st.text_input("Enter your name")

num_1 = st.number_input("Enter a number",step=1)
num_2 = st.number_input("Enter second number",step=1)

operation = st.selectbox("Select an operation",["Addition","Subtraction","Multiplication","Division"])
result = None

calculate_button = st.button("Calculate")
if calculate_button:
    
    if operation == "Addition":
        result = num_1 + num_2
    elif operation == "Subtraction":
        result = num_1 - num_2 
    elif operation == "Multiplication":
        result = num_1 * num_2 
    elif operation == "Division":
        if num_2 != 0:
            result = num_1 / num_2 

    if 'result' in locals():
        st.write(f"Hello {user_name}")
        st.write(f"Result of {num_1} {operation.lower()} {num_2} = {result}")
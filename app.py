import streamlit as st

# st.title("Simple Calculator")
# user_name = st.text_input("Enter your name")

# num_1 = st.number_input("Enter a number",step=1)
# num_2 = st.number_input("Enter second number",step=1)

# operation = st.selectbox("Select an operation",["Addition","Subtraction","Multiplication","Division"])
# result = None

# calculate_button = st.button("Calculate")
# if calculate_button:
    
#     if operation == "Addition":
#         result = num_1 + num_2
#     elif operation == "Subtraction":
#         result = num_1 - num_2 
#     elif operation == "Multiplication":
#         result = num_1 * num_2 
#     elif operation == "Division":
#         if num_2 != 0:
#             result = num_1 / num_2 

#     if 'result' in locals():
#         st.write(f"Hello {user_name}")
#         st.write(f"Result of {num_1} {operation.lower()} {num_2} = {result}")


# ====================assignment task =========================================

st.title("Finding the largest of 3 numbers")
num1 = st.number_input("enter first number",step=1)
num2 = st.number_input("enter second number",step=1)
num3 = st.number_input("enter third number",step=1)
find_button = st.button("Find")

if find_button:
    # m = max(num1,num2,num3)

    if num1 > num2:
        if num1 > num3:
            m = num1
        else:
            m = num3
    elif num2 > num3:
        m = num2
    else:
        m = num3

    st.write(f"Largest number among {num1}, {num2} and {num3} is {m}")
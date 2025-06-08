import streamlit as st
from factorial import fact

def main():
    #Set the title
    st.title("Calculator app")

    #Set the sub-title
    st.header("Calculate plus, minus, multiply, divide")

    #Set the description
    st.write("Help every one calculate basic operation")

    number1 = st.number_input("Enter the first number:", min_value=-(10**4), max_value=10**6, value=0, step=1)
    number2 = st.number_input("Enter the second number:", min_value=-(10**4), max_value=10**6, value=0, step=1)

    if st.button("Calculate"):
        result = fact(number1, number2)
        st.write(f"The multiplication of {number1} and {number2} is {result}")
        
if __name__ == "__main__":
    main()
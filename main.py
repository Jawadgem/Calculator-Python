import streamlit as st

def main():
    st.markdown("<h1 style='text-align: center; color: red;'>🧮 Simple Calculator</h1>", unsafe_allow_html=True)
    st.write("**Enter two numbers and choose an operation**")

    col1, col2 =st.columns(2)

    with col1:
        num1 = st.number_input("🔢 **Enter first number**", value=0)

    with col2:
        num2 = st.number_input("🔢 **Enter second number**", value=0)

    operation = st.selectbox("📌 **Choose an operation**", ["Addition ➕", "Subtraction ➖", "Multiplication ✖️", "Division ➗"])

    if st.button("✅ Calculate"):
        try:
            if operation == "Addition (+)":
                result = num1 + num2
                symbol = "+"
            elif operation == "Subtraction (-)":
                result = num1 - num2
                symbol = "-"
            elif operation == "Multiplication (x)":
                result = num1 * num2
                symbol = "x"
            else:
                if num2 == 0:
                    st.warning("⚠️ Oops! Division by Zero is not possible. Please enter a valid number.")
                    return
                result = num1 / num2
                symbol = "/"

            st.success(f"🎯 Result: **{num1} {symbol} {num2} = {result}**")
                
        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")

    st.markdown("<h3 style='text-align: center; color: grey;'>🚀 Built by Jawad Nasir</h3>", unsafe_allow_html=True)


# Run the main function if the script is executed
if __name__ == "__main__":
    main()
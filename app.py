import streamlit as st

def main():
    st.title("Welcome to test Streamlit app")
    name = st.text_input("First, enter your name (you can enter a fake name):")
    if st.button("Submit"):
        if name:
            st.success(f"Hello, {name}! Streamlit app works OK with LeWagon requirements.txt but doesn't work with out requirements.txt:(")
        else:
            st.warning("Please enter your name.")

if __name__ == "__main__":
    main()

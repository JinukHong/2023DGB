import streamlit as st

def main():
    st.title("Button Test")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Left Button"):
            st.write("Left Button Pressed")
    
    with col2:
        if st.button("Right Button"):
            st.write("Right Button Pressed")

if __name__ == "__main__":
    main()

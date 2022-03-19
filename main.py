import streamlit as st


st.write(
    """
         # Test
         """
)

st.write("web app to predict if the image needs an alarm")

file = st.file_uploader("Please upload an image file", type=["jpg", "png"])

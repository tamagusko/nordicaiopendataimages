import streamlit as st


st.write("""
         # Rock-Paper-Scissor Hand Sign Prediction
         """
         )st.write("This is a simple image classification web app to predict rock-paper-scissor hand sign")file = st.file_uploader("Please upload an image file", type=["jpg", "png"])

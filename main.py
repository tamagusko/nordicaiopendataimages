import numpy as np
import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps


def import_image(image):
    size = (75, 75)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)
    image = image.convert('RGB')
    image = np.asarray(image)
    image = (image.astype(np.float32) / 255.0)
    return image[np.newaxis, ...]


def predict(image):
    model_name = 'FI_C0151303_best_model.h5'
    model = tf.keras.models.load_model(model_name)
    return model.predict(import_image(image))


st.write("""
         # Nordic AI & Open Data Hackathon (18-19 of March 2022)
         ## Project: Intelligent system for analysis and early warning of vehicle accidents on highways
         """
         )

st.write("web app to predict if the image needs an alarm")

file = st.file_uploader("Please upload an image file", type=["jpg", "png"])

if file is None:
    st.text("You haven't uploaded an image file")
else:
    image = Image.open(file)
    filename = image.filename
    """ 
    st.image(image, use_column_width=True)
    prediction = predict(image)

    if np.argmax(prediction) == 0:
        st.write("Normal!")
    elif np.argmax(prediction) == 1:
        st.write("Alarm!")
    else:
        st.write("ERROR")
    st.write(prediction)
     """
    st.write(filename)

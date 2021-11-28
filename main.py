import streamlit as st
import os
from PIL import Image
from helper import *

st.title('Dogs vs Cats Classifier')


def save_uploaded_file(up_file):
    """This function saves the uploaded pics to the static/images folder. 

    Parameters:
    -----------
    up_file: Uploaded image file

    Returns:
    ---------
    1, file path if successful and 0 if failed"""
    try:
        with open(os.path.join('static\images', up_file.name), 'wb') as file:
            file.write(uploaded_file.getbuffer())
            #print('file written')
        return 1
    except:
        return 0

# Creating Upload button,
# display uploaded image on the app,
# and call the predictor function which we had just created.


uploaded_file = st.file_uploader("Upload Image Here")
#print(uploaded_file)
print(save_uploaded_file(uploaded_file))
if uploaded_file is not None:
    if save_uploaded_file(uploaded_file):
        display_image = Image.open(uploaded_file)
        st.image(display_image)
        prediction = get_prediction(os.path.join('static\images', uploaded_file.name))
        #print(prediction)
        # delete uploaded file after prediction
        os.remove(os.path.join('static\images', uploaded_file.name))
        if prediction:
            st.write('Dog Detected')
        else:
            st.write('Cat Detected')

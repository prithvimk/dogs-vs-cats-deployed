from tensorflow.keras.preprocessing.image import img_to_array, load_img
from tensorflow.keras.models import load_model
import numpy as np


def get_prediction(image_path):
    """Loads the image, applies image processing and passes it to the model to return the prediction

    Parameters:  
    -----------
    Image path  

    Returns: 
    ---------
    1 if dog and 0 if cat is detected in the image"""

    image = load_img(image_path, target_size=(224, 224))
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image.reshape(1, 224, 224, 3)
    # centering
    image = image - np.array([123.68, 116.779, 103.939], dtype='float32')
    # load model
    model = load_model(r'static\final_model.h5')
    result = model.predict(image)
    return result[0]


from tensorflow import keras
import pandas as pd
import keras
from tensorflow.python.keras.models import load_model
from keras.preprocessing import image
import numpy as np

model = keras.models.load_model('PATH')   #Change the location where the trained model is stored


# Load and preprocess the image
img_path = 'PATH'    #Specify path of the image
img = image.load_img(img_path, target_size=(150, 150, 3))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)  # Expand dimensions to make it a batch of size 1
img_array /= 255.0  # Normalize pixel values if needed

prediction = model.predict(img_array)[0][0]


if(prediction<0.1):
    print("The patient has been diagnosed with a brain Tumor.")
else:
    print("The patient does not exhibit any signs of brain tumor.")

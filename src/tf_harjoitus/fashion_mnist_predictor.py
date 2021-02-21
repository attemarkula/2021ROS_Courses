#!/usr/bin/python3
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '0' 

import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

model = tf.keras.models.load_model('saved_model/')
model.summary()

img = Image.open('jeans_small_gray.jpg')
np_image = np.array(img)
np_image_normalized = np_image / 255.0

np_image_inverted = 255 - np_image
np_image_inverted_normalized = np_image_inverted / 255.0


print("tulosta pitää tutkia luokkien avulla")

class_names = ['T-shirt/top', 'Trouser','Pullover', 'Dress', 'Coat',
			 'Sandals', 'Shirts', 'Sneaker', 'Bag', 'Angle boot']
print (class_names)

np.set_printoptions(precision=6) #best fit
np.set_printoptions(linewidth=200)
prediction_single = model.predict(np.expand_dims(np_image_inverted_normalized,0))
print(prediction_single)
print("non-inverted")
prediction_single = model.predict(np.expand_dims(np_image_normalized,0))
print(prediction_single)


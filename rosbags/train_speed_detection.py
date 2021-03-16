import tensorflow as tensorflow
import numpy as np 
import pandas as pd
from PIL import Image
import os
from tensorflow.keras import layers, models

train_dataset_path = '....topics_combined.csv'
images_path = 'rosbag/data'
model_save_path = 'saved_models'

raw_train_dataset = pd.read_csv(train_dataset_path)

print (raw_train_dataset.shape)
print (raw_train_dataset.head)
print (type(raw_train_dataset))

train_labels = raw_train_dataset.pop('sog')
print(train_labels.head)
print(train_labels.shape)
print(type(train_labels))
#päätettiin tehdä rakenne jossa on 10 kuvaa joista sevenssinä voidaan tutkia nopeus
train_images = raw_train_dataset.pop('filename')
images_array = np.zeros((1737, 10, 240, 240), dtype=np.uint8)
#images_array on 240x240 setti kuvia joka kuva on 'channel'. 
#jokaisen setin delta on yksi kuva. ja lopusta periaatteessa puuttuu kuvia

for index, current_image in train_images.iteritems():
    img = Image.open(os.path.join(images_path, current_image).resize(240,240))
    np_image = np.array(img)

    try:
        for channel in range(10):
            images_array[index+channel][channel] = img
    except Exception:
        print(str(index) + "index " + str (channel) + "channel ")

print(images_array.shape)
print(images_array)

# muotoillaan neuroverkolle sopivaksi
# axis vaihto numpy arrayssä. 1 = toinen axis alusta, -1 on toinen axis lopusta
images_array = np.moveaxis(images_array,1,-1)
model = models.Sequential()
model.add(layers.Conv2D(10,(3,3),activation='relu', input_shape=(240,240,10)))
model.add(layers.MaxPool2D((2,2)))
model.add(layers.Conv2D(10,(5,5),activation='relu'))

model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(1))

print (model.summary())

optimizer = tf.keras.optimizer.RMSprop(0.001)
model.optimizer(optimizer=optimizer, loss = 'mse', 
                metrics = ['mae','mse'])

history = model.fit(images_array, train_images, 
                    epoch=3, batch_size=10, 
                    validation_data=images_array, train_labels))

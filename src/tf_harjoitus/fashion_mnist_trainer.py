#!/usr/bin/python3

import tensorflow as tf
import matplotlib.pyplot as plt

#Dataset https://github.com/zalandoresearch/fashion-mnist
#haetaan dataset fashion_mnist avulla
fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
class_names = ['T-shirt/top', 'Trouser','Pullover', 'Dress', 'Coat',
			 'Sandals', 'Shirts', 'Sneaker', 'Bag', 'Angle boot']

print(train_images.shape)
#ensimmäinen osa
"""
plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)
plt.show()
"""

#toinen osa

"""
plt.figure(figsize=(10,10))
for i in  range(25):
	plt.subplot(5,5,i+1)
	plt.xticks([])
	plt.yticks([])
	plt.grid(False)
	plt.imshow(train_images[i], cmap=plt.cm.binary)
	plt.xlabel(class_names[train_labels[i]])
plt.show()

"""
#Normalisoidaan dataset nollan ja ykkösen väliin
train_images = train_images / 255.0
test_images = test_images / 255.0


#Luodaan neuroverkko model
model = tf.keras.Sequential([
	tf.keras.layers.Flatten(input_shape=(28,28)),
	tf.keras.layers.Dense(128,activation='relu'),
	tf.keras.layers.Dense(10)
])

model.compile(optimizer='adam',
	loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
	metrics=['accuracy'])

#neuroverkon treenaus train datalla
model.fit(train_images, train_labels, epochs=10)

#neuroverkon testaus testaus datalla
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)


print()
print("Test accuracy:", test_acc)
#tallennetaan neuroverkko myöhempää käyttöä varten.
model.save('saved_model')




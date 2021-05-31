#!/usr/bin/python3
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '0' 

import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

train_dataset_path = "robot1_positions.csv"
validation_dataset_path = "robot1_positions.csv" # FIXME
test_dataset_path = "robot1_positions.csv" # FIXME

column_names = ['us1_sub.range','us2_sub.range','us3_sub.range','us4_sub.range','us5_sub.range','us6_sub.range','ground_truth_x','ground_truth_y']
raw_train_database = pd.read_csv(train_dataset_path, names=column_names)

#print (raw_train_database.shape)
#print (raw_train_database.head)

train_dataset = raw_train_database.copy()
train_label_x = train_dataset.pop('ground_truth_x')
train_label_y = train_dataset.pop('ground_truth_y')

#print (train_dataset.shape)
#print (train_dataset.head)

train_labels = pd.concat([train_label_x, train_label_y], axis=1)
print (train_labels.head)

raw_validation_dataset = pd.read_csv(validation_dataset_path, names=column_names)
validation_dataset = raw_validation_dataset.copy()
validation_label_x = validation_dataset.pop('ground_truth_x')
validation_label_y = validation_dataset.pop('ground_truth_y')

validation_labels = pd.concat([validation_label_x, validation_label_y], axis=1)


raw_test_dataset = pd.read_csv(test_dataset_path, names=column_names)
test_dataset = raw_test_dataset.copy()
test_label_x = test_dataset.pop('ground_truth_x')
test_label_y = test_dataset.pop('ground_truth_y')

test_labels = pd.concat([test_label_x, test_label_y], axis=1)
#print (test_labels.head)

def build_model():
    model = keras.Sequential([
        layers.Dense(64,activation="relu", input_shape=[len(train_dataset.keys() )]),
        layers.Dense(64,activation="relu"),
        layers.Dense(2)
    ])
    optimizer = tf.keras.optimizers.RMSprop(0.001)
    model.compile(loss='mse', optimizer=optimizer, metrics=['mae', 'mse'])
    return model

model = build_model()
print(model.summary)

EPOCH = 10
mae = 0

for x in range(50):
    history = model.fit(
        train_dataset, train_labels, epochs = EPOCH, 
        validation_data=(validation_dataset, validation_labels), verbose=0)
    last_mae = mae
    loss, mae, mse = model.evaluate(test_dataset, test_labels, verbose=0)
    #FIXME print("Testing set Mean abs error: {:5,2f} position".format(mae))
    print("Testing set Mean abs error: {:5.2f} position".format(mae))
    
    print("Testing set Mean abs error as 1000* integer : ",(int(mae*1000)),"position")
    if mae < last_mae:
        print("saving model...")
        model_save_path = "saved_model/robot1_model" + str(x*10) + "epochs"
        model.save(model_save_path)

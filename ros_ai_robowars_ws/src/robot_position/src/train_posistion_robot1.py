#!/usr/bin/python3

import numby as nb
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

train_dataset_path = "robot1_positions.csv"
validation_dataset_path = "robot1_positions.csv" # FIXME
test_dataset_path = "robot1_positions.csv" # FIXME


column_names[] = ['yaw_radians','us1','us2','us3','us4','us5','us6','ground_truth_x','ground_truth_y']
raw_train_database = pd.read_csv(train_dataset_path, names=column_names)

print (raw_train_database.shape)
print (raw_train_database.head)
train_dataset = raw_train_database.copy()

train_label_x = train_dataset_copy.pop('ground_truth_x')
train_label_y = train_dataset_copy.pop('ground_truth_y')
print (train_dataset.shape)
print (train_dataset.head)

#!/usr/bin/python3
import rospy, cv2
from sensor_msgs import CompressedImage
from std_msgs.msg import Float64
import numpy as np
from tensorflow import keras
from pathlib import Path
from PIL import Image

class Speed_detector:
def __init__(self):
    self.predict_data = np.zeros((1,10,240,240))  # oltava saman kokoinen
    self.node = rospy.init_mode("speed_detector")
    self.predict_speed_publisher = rospy.Publisher('predicted_speed',Float64, queue_size=1)
    self.subscriber = rospy.Subscriber('/camera_crop/image_rect_color/compressed', CompressedImage, self.image_callback)

    self.model = keras.models.load_model('/home/rosp/rosbag/saved_models/model')

def image_callback(self, msg):
    #self.predict_data = np.zeros((1,10,240,240))
    self.predict_data = np.moveaxis(self.predict_data,-1,1)
    buf = np.ndarray(shape=(1,len(msg.data)), dtype=np.uint8, buffer=msg.data)
    cv_img = cv2.imdecode(buf, cv2.IMREAD_ANYCOLOR)
    cv_img_gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
    resize_cv_img_gray = cv2.resize(cv_img_gray, self.dim)
    np_img = np.asarray(resized_cv_img_gray)

    for channel in range(10:
        self.predict_data[0][channel] = self.predict_data[0][channel+1]
        self.predict_data[0][0] = np_img
"""
    self.predict_data
"""

    self.predict_data = np.moveaxis(self.predict_data, 1,-1)
    test_predictions = self.model.predict(self.predict_data)
    s_msg = Float64()
    s_msg.data = test_predictions[0][0]



from PIN import Image
import os

img_save_folder = '/home/rosp/rosbags/data'
img_load_folder = '/home/rosp/rosbags/subset_2019-06-23-20-22-22_extract/cameraimages'


for filename in os.list.dir(img_load_folder):
    if filename.endswith(".jpg"):
        img = Image.open(os.path.join(img_load_folder, filename)).convert('L')
        img.save(os.path.join(img_save_folder, filename))
    else:
        print('Thats no image that i know')

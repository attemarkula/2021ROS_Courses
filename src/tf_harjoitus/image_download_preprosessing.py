#!/usr/bin/python3
import urllib.request
from PIL import Image
import numpy as np

#urllib.request.urlretrieve('https://pixy.org/src/154/thumbs350/1547777.jpg', "jeans.jpg")


img = Image.open("jeans.jpg")

def grayscale(colors):
    red,green,blue=colors
    return (0.07*red+0.072*green+0.021*blue)

print("from: "+str(img.size),end="")
#nopeutetaan hieman
img=img.resize((150,150))
print(" -> "+str(img.size))

#img=Image.open('jeans.jpg')
np_image = np.array(img)


#allaoleva lataa ja konvertor ja pienentää kuvan(pienennys alussa nopeuttaa).
#np_image = np.array(Image.open('jeans.jpg').convert("L").resize((300,300)))
#print(np_image)
#img=Image.fromarray(np_image)
#img.save("1.jpg")

np_image_grayscale = np.apply_along_axis(grayscale,2,np_image)
#print(np_image_grayscale)

np_gray_image_int =  np_image_grayscale.astype(np.uint8)
#print(np_gray_image_int)

grey_image = Image.fromarray(np_image_grayscale)
#print(grey_image) #150x150 F -> 32bit

grey_image = Image.fromarray(np_gray_image_int)
#print(grey_image) #150x150 L -> 8bit

img_gray_small = grey_image.resize((28,28))
print(img_gray_small) #28x28 -> 8bit
img_gray_small.save('jeans_small_gray2.jpg')

print("\nprogram ends.")

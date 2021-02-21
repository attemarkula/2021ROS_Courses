#!/usr/bin/python3
import urllib.request

from PIL import Image, ImageOps

import numpy as np

try:
	img = Image.open("jeans.jpg")
except Exception as e:
	print("fetching file from internet")
	urllib.request.urlretrieve('https://pixy.org/src/154/thumbs350/1547777.jpg', "jeans.jpg")
	img = Image.open("jeans.jpg")
else:
	print("found local file, using it")

def grayscale(colors):
    red,green,blue=colors
    return (0.07*red+0.72*green+0.21*blue)

#print("resize: "+str(img.size),end="")
#nopeutetaan hieman ja esi-pienennetään iso
#img=img.resize((150,150))
#print(" -> "+str(img.size))

#img=Image.open('jeans.jpg')
np_image = np.array(img)


#allaoleva lataa ja konvertor ja pienentää kuvan(pienennys alussa nopeuttaa).
#np_image = np.array(Image.open('jeans.jpg').convert("L").resize((300,300)))

#img=Image.fromarray(np_image)
#img.save("1.jpg")

#toinen tapa PIL.ImageOps funktiolla
#imgbw=ImageOps.grayscale(img)
#img.resize((28,28)).save("1bw.jpg")

np_image_grayscale = np.apply_along_axis(grayscale,2,np_image)
#print(np_image_grayscale)

np_gray_image_int =  np_image_grayscale.astype(np.uint8)
#print(np_gray_image_int)

np_gray_image = Image.fromarray(np_gray_image_int)
#print(np_gray_image) #150x150 L -> 8bit

np_image_gray_small = np_gray_image.resize((28,28))
#print(np_image_gray_small) #28x28 -> 8bit
np_image_gray_small.save('jeans_small_gray.jpg')

print("\nprogram ends.")


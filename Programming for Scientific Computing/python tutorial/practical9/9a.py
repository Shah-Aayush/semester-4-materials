#!/usr/bin/env python3

# first install 'skimage' using this command in terminal :
# pip install scikit-image

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from skimage import io
import os
import scipy
from scipy import ndimage
from skimage.filters import sobel
from skimage.color import rgb2gray

camera = io.imread('./images/cameraman.tiff')

# Number of pixel
print("Image size :",camera.shape) 

# 2 dimentional
print("Dimension :",camera.ndim)

# Numpy array
print("Type of Object :",type(camera))

# Integer value range from 0 to 255 (0 for black and 255 for white)
print("Object data type :", camera.dtype)

plt.imshow(camera, cmap=plt.cm.gray)
print(camera)

print(camera.ravel())
ax = plt.hist(camera.ravel(), bins = 256)
plt.xlabel('Intensity Value')
plt.ylabel('Count')
plt.show()

image_of_lena = io.imread('./images/lena_gray.gif')
lena_img = image_of_lena.astype(float)
blurred_lena_img = ndimage.gaussian_filter(lena_img, 3)
plt.figure(figsize=(12,4))
plt.subplot(121)
plt.imshow(lena_img, cmap=plt.cm.gray)
plt.axis('off')
plt.subplot(122)
plt.imshow(blurred_lena_img, cmap=plt.cm.gray)
plt.axis('off')
plt.tight_layout()
plt.show()

image_edge = io.imread('./images/lena_gray.gif')
edge_sobel = sobel(image_edge)
plt.figure(figsize=(12,4))
plt.subplot(121)
plt.axis('off')
plt.imshow(image_edge, cmap=plt.cm.gray)
plt.subplot(122)
plt.axis('off')
plt.imshow(edge_sobel, cmap=plt.cm.gray)
plt.tight_layout()
plt.show()

color_img = io.imread('./images/lena_color.gif')
gray_img = rgb2gray(color_img)
plt.figure(figsize=(12,4))
plt.subplot(121)
plt.imshow(color_img,cmap=plt.cm.gray)
plt.subplot(122)
plt.imshow(gray_img, cmap=plt.cm.gray)
plt.tight_layout()
plt.show()
#Refer - https://www.geeksforgeeks.org/opencv-python-tutorial/

# Arithmetic Operation on Images
# Pixel values are directly added / subtarcted for 2 images
# make sure that the 2 images are of same size

import cv2 
import numpy as np 
     
image1 = cv2.imread('star.jpeg') 
image2 = cv2.imread('dot.jpeg')
  
# 0.5 and 0.4 are weights to be multiplied for each pixel, 0 is gamma_value (measurement of light)
weightedSum = cv2.addWeighted(image1, 0.5, image2, 0.4, 0)
  
cv2.imshow('Weighted Image', weightedSum)

cv2.waitKey(0) 
cv2.destroyAllWindows() 

##### Subtraction of images

import cv2 

image1 = cv2.imread('star.jpeg') 
image2 = cv2.imread('dot.jpeg')
  
sub = cv2.subtract(image1, image2)
  
cv2.imshow('Subtracted Image', sub)
  
cv2.waitKey(0)
cv2.destroyAllWindows()

##### Image Resizing
# Explain the various situtions where image resizing is needed

import cv2

img = cv2.imread("pika.png",1)
cv2.imshow("Original Image", img)

# The order of dimensions is (WIDTH, HEIGHT)
resized = cv2.resize(img, (500, 250))
cv2.imshow("reducedImage", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()

##### Erosion of an image, corners are trimmed in erosion
#refer - https://docs.opencv.org/3.4/d9/d61/tutorial_py_morphological_ops.html
import cv2
import numpy as np
  
image = cv2.imread("pika.png", 1) 
  
# kernel is used for erosion as an input
kernel = np.ones((5, 5), np.uint8)

image = cv2.erode(image, kernel) 
cv2.imshow("Eroded Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

##### Bluring of an image
# Explain the situations where blurring is needed
# Advantages of blurring to be discussed here

import cv2

image = cv2.imread("pika.png")

cv2.imshow('Original Image', image)
cv2.waitKey(0)


#refer -https://docs.opencv.org/3.4/d4/d13/tutorial_py_filtering.html
# Gaussian Blur - used mostly in machine learning preprocessing steps
Gaussian = cv2.GaussianBlur(image, (7, 7), 0,0)
cv2.imshow('Gaussian Blurring', Gaussian)
cv2.waitKey(0)

# Median Blur - used in digital processing preserves edges but removes noise
median = cv2.medianBlur(image, 5)
cv2.imshow('Median Blurring', median)
cv2.waitKey(0)


# Bilateral Blur - only sharp edges are preserved here
bilateral = cv2.bilateralFilter(image, 9, 75, 75)
cv2.imshow('Bilateral Blurring', bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()


##### Bordering an image
#cv2.copyMakeBorder(image, top, bottom, left, right, borderType, colorValue)
# SOLID Border around an image
import cv2

img = cv2.imread("pika.png")
borderedImage = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value = 1)

cv2.imshow("Bordered Image", borderedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Reflective Border around an image
import cv2

img = cv2.imread("pika.png")
borderedImage = cv2.copyMakeBorder(img, 20, 20, 20, 20, cv2.BORDER_REFLECT, value = 2)

cv2.imshow("Bordered Image", borderedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()


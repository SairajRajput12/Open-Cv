import cv2 
import numpy as np 

print('This is tutorial for image smoothing and image blurring')
# Image Smoothing/Blurring:
# it's very common to blur and smooth image in the vision applications. this reduces the noise in the images. 
# The noise can be present due to various factors like maybe the sensor by which you took the picture was corrupted or it malfunctioned, or environmental factors like the lightning was poor, etc.
# Now there are different types of blurring to deal with different types of noises and I have discussed each method in detail and even done a comparison between them inside our Computer Vision Course but for now, we will briefly look at just one method, the Gaussian Blurring method. This is the most common image smoothing technique used. It gets rid of Gaussian Noise. In simple words, this will work most of the time. 

# Smoothed_image  = cv2.GaussianBlur(source-image, ksize, sigmaX)

# Params:

# source-image:  Our input image
# ksize: Gaussian kernel size. kernel width and height can differ but they both must be positive and odd. 
# sigmaX: Gaussian kernel standard deviation in X direction.

# One thing you need to learn is that by controlling the kernel size you control the level of smoothing done. There is also a SigmaX and a SigmaY parameter that you can control

img = cv2.imread('naruto.jpg',1) 
blurred = cv2.GaussianBlur(img,(9,9), 50)
cv2.imshow('This is blurred image',blurred) 
cv2.waitKey(0)
cv2.destroyAllWindows()




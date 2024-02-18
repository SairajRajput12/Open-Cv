import cv2 
import numpy as np

print('edge detection using python')

# In OpenCV there are edge detectors such as Sobel filters and laplacian filters but the most effective is the Canny Edge detector. In our Computer Vision Course I go into detail of exactly how this detector works but for now let’s take a look at its implementation in OpenCV.
# edges = cv2.Canny( image, threshold1, threshold2)

# Params:

# image: This is our input image.
# edges: output edge map; single channels 8-bit image, which has the same size as image .
# threshold1: First threshold for the hysteresis procedure.
# threshold2: Second threshold for the hysteresis procedure.

img = cv2.imread('Sairaj Rajput IT VIIT.png',1) 
edges = cv2.Canny(img,30,150) 
cv2.imshow('The image after edges',edges) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 




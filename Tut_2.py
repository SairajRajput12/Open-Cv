import cv2 
import numpy as np


# Accessing and modifying image pixels 
img = cv2.imread('naruto.jpg',0) 
print('The data type of the Image is: {}'.format(img.dtype))
print('The dimensions of the Image is: {}'.format(img.ndim))

# colored image is 3 dimensional 
# gray colored image in 2 dimensional

# First 2 are the width and the height and the 3rd are the image channels. Now these are B (blue), G (green), & R (red) channels. 
# In OpenCV due to historical reasons, colored images are stored in BGR instead of the common RGB format.
# print(img [300, 300])
# We are setting all pixels in x range 100-150 and in y range 80-120 equal to 0 (meaning black).
# Img_copy = img.copy() 
# Img_copy[100:150,80:120]  =  0
# cv2.imshow("Fixed Resizing",Img_copy)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Here i have changed the one of the pixels from image copy

# Image resizing
resized = cv2.resize(img, (500,500))   

# # Display image
cv2.imshow("Fixed Resizing", resized);
cv2.waitKey(0)
cv2.destroyAllWindows()









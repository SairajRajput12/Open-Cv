import cv2 
import numpy as np 

print('This is tutorial for thresolding image') 
# Image used in this tutorial is: ThresoldingSampleImage.jpg 
# thresholding does is that it checks each pixel in the image against a threshold value and If the pixel value is smaller than the threshold value, it is set to 0, otherwise, it is set to the maximum value, (this maximum value is usually 255 so white color).

# Syntax: ret, thresholded_image = cv2.threshold(source_image, thresh, max_value, type)
# Params:

# Source_image: This is your input image.
# thresh: Threshold value. (If you use THRESH_BINARY then all values above this are set to max_value.)
# max_value: Maximum value, normally this is set to be 255.
# type: Thresholding type. The most common types are THRESH_BINARY  & THRESH_BINARY_INV
# ret: Boolean variable which tells us if thresholding was successful or not.

# 1. first convert the image into the grayscale image. for this purpose we will use cv2.cvtColor function
img = cv2.imread('ThresoldingSampleImage.jpg',1) 
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
# cv2.imshow("Grayscale Image", gray_img);

# Now that we have a grayscale image, we can apply our threshold.
# Apply the threshold
# _ , thresholded_image = cv2.threshold(gray_img, 220, 255, cv2.THRESH_BINARY)

#  We are applying a threshold such that all pixels having an intensity above 220 are converted to 255 and all pixels below 220 become 0.
# Display Thresholded image

# Now Let’s see the result of the inverted threshold, which just reverses the results above. For this you just need to pass in cv2.THRESH_BINARY_INV instead of cv2.THRESH_BINARY.
_ , thresholded_image = cv2.threshold(gray_img, 220, 255, cv2.THRESH_BINARY_INV)


cv2.imshow("Thresholded Image",thresholded_image);
cv2.waitKey(0)
cv2.destroyAllWindows()








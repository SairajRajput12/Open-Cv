import cv2 
import numpy as np 

print('Contour Detection:') 
# Contours can be defined simply as a curve joining all the continuous points (along the boundary), having the same color or intensity
# In simple terms think of contours as white blobs on black background for e.g. in the output of threshold function or the edge detection 
# function, each shape can be considered as an individual contour. So you can segment each shape, localize them or even recognize them.
# The contours are a useful tool for shape analysis, object detection, and recognition, take a look at this detection and recognition  
# application I’ve built using contour detection.

# contours, hierarchy = cv2.findContours(image, mode, method[, offset])

# Params:

# image Source: This is your input image in binary format, this is either a black & white image obtained from a thresholding or a similar function or the output of a canny edge detector.
# mode: Contour retrieval mode, for example  cv2.RETR_EXTERNAL mode lets you extract only external contours meaning if there is a contour inside a contour then that child contour will be ignored. You can see other RetrievalModes here
# method: Contour approximation method, for most cases cv2.CHAIN_APPROX_NONE works just fine.

# After you detect contours you can draw them on the image by using this function.

# cv2.drawContours( image, contours, contourIdx, color, [thickness] )

# Params:

# image: original input image.
# contours: This is a list of contours, each contour is stored as a vector.
# contourIdx: Parameter indicating which contour to draw. If it is -1 then all the contours are drawn.
# color: Color of the contours.

# Code 

img = cv2.imread('naruto.jpg',1) 
image_copy = img.copy() 
# Alternatively you can also pass in the edges output to the contours function.
# Threshold image, Remember the target object is white and background black.
gray_image = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY) 
_ , thresholded_image = cv2.threshold(gray_image, 220, 255, cv2.THRESH_BINARY_INV)
contours, _ = cv2.findContours(thresholded_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# Draw the detected contours, -1 means draw all detected contours
cv2.drawContours(image_copy , contours, -1 , (0,255,0), 3)
print('Total Shapes present in image are: {}'.format(len(contours)))
# Display image
cv2.imshow("Contour Detection", image_copy);
cv2.waitKey(0)
cv2.destroyAllWindows()






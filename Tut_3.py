import cv2 
import numpy as np

# Resizing While Keeping the Aspect Ratio Constant:

img = cv2.imread('naruto.jpg', 1)

# Get the width and height of the image
height, width = img.shape[:-1]
# We are extracting the shape of the image, [:-1] indicates that I don’t want channels returned, just height and width. 
# This ensures your code works for both color and grayscale images.



# Compute ratio for the new height taking into account the 300 px width of image
r = 300.0 / width

# Get the new height
new_height = int(height * r)

# Resize the image with 300 width and the new height.
resized = cv2.resize(img, (300, new_height))

# Display Resized Image
cv2.imshow("Aspect Ratio Resize", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

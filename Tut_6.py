import cv2 
import numpy as np 

print('this is tutorial for cropping an image') 

# Cropping the images: 
# Now let’s say we wanted to crop naruto’s face then we would need four values namely X1 (lower bound on the x-axis),  X2 (Upper bound on y-axis), Y1 (lower bound on the y-axis) and Y2 (Upper bound on the y-axis). 
# Syntax: 
# face_roi = img [Start X : End X, Start Y: End Y]

img = cv2.imread('naruto.jpg',1) 
face_roi = img[100:270,200:450] 
cv2.imshow(
    'I am Batman',
    face_roi
)
cv2.waitKey(0)
cv2.destroyAllWindows()




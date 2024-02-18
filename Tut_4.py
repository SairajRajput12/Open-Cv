import cv2 
import numpy as np  
# Applying the geometric transformation to the image 

# transformed_ image = cv2.warpAffine(src, M, dsize[, dst[, flags[, borderMode[, borderValue]]]])
# Params:
# src: input image.
# M: 2×3 transformation matrix.
# dsize: size of the output image.
# flags: combination of interpolation methods
# borderMode: pixel extrapolation method (see BorderTypes) by default its constant border.
# borderValue: value used in case of a constant border; by default, it is 0, which means replaced values will be black.


# Translation: 
# Translation is the shifting of an object’s location, meaning the movement of image in x, y-direction. Suppose you want the image to move tx amount of pixels  
# in the x-direction and ty amount of pixels in y-direction then you will construct below transformation matrix accordingly and pass it into the warpAffine function

# img = cv2.imread('naruto.jpg',1) 

# rows, cols, channels = img.shape

# Consturct the translation matrix 
# M = np.float32([
#     [1,0, 120], 
#     [0,1, -40]
# ])


# Apply the wrapAffline function
# translated = cv2.warpAffine(img, M, (cols,rows))

# Display image
# cv2.imshow("Translated Image",translated);
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# Explanation of this code: 
# We’re constructing the translation matrix so we move 120 px in x-direction and 40 px in the negative y-direction.
# M = cv2.getRotationMatrix2D( center, angle, scale )

# Params:

# center: This is the center of the rotation in the source image.
# Angle: The Rotation angle in degrees. Positive values mean counter-clockwise rotation (the coordinate origin is assumed to be the – top-left corner).
# Scale: scaling factor.


img = cv2.imread('naruto.jpg',1) 

rows, cols, channels = img.shape

# Set angle to 45 degrees.
angle = 45

# Rotate image from center of image with an angle of 45 degrees at the same scale.
rotation_matrix = cv2.getRotationMatrix2D((cols/2,rows/2), angle, 1)

# Apply the transformation
rotated = cv2.warpAffine(img, rotation_matrix, (cols,rows))

# Display image
cv2.imshow("Rotated Image",rotated);
cv2.waitKey(0)
cv2.destroyAllWindows()
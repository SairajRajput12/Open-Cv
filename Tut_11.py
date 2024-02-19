import cv2 
import numpy as np 

print('this tutorial is for morphological operations')
# This is one of the most used preprocessing techniques to get rid of noise in binary (black & white) masks
# it needs 2 input one is source image and another is the kernel which decides the nature of the operations. 
# there are 2 common morphological operations which are the erosion and dilation. 

# 1. Ersion:
# -> means erode or eats away the boundaries of the forground object. 
# -> in this process the kernel is slided and if in original image if it contains 1 then we will consider that pixel in an original image. 
# -> otherwise it get erroded. 
# Erosion decreases the thickness or size of the foreground object or you can simply say the white region of image decreases. It is useful for removing small white noises.
# eroded_image = cv2.erode(source_image, kernel, [iterations] ) 
# Params:

# source_image: Input image.
# kernel: Structuring element or filter used for erosion if None is passed then, a 3x3 rectangular structuring element is used. The bigger kernel you create the stronger the impact of erosion on the image.
# iterations: Number of times erosion is applied, the larger the number, greater the effect. 
 
# we will remove the noises from the sample.png image 
# img = cv2.imread('sample.png',1) 
# # Make a 7x7 kernel of ones
# kernel = np.ones((7,7),np.uint8) # Making a 7x7 kernel, bigger the kernel the stronger the effect.


# eroded = cv2.erode(img,kernel,iterations=2) # Applying erosion with 2 iterations, the values for kernel and iterations should be tuned according to your own images.

# cv2.imshow("Eroded Image", eroded);
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#As you can see the white noise is gone but there is a small problem, our object (person) has become thinner.  
# We can easily fix this by applying dilation which is the opposite of erosion.

# 2. Dilation:
# It is just the opposite of erosion. It increases the white region in the image or size of the foreground object increases. So essentially dilation expands the boundary of Objects.  
# Normally, in cases like noise removal, erosion is followed by dilation. Because, erosion removes white noises, but it also shrinks our object like we have seen in our example. 
# So now we dilate it. Since noise is gone, they won’t come back, but our object area increases.
# Dilation is also useful for removing black noise or in other words black holes in our object. So it helps in joining broken parts of an object.

# dilated_image  = cv2.dilate( source_image, kernel, [iterations])

# The parameters are the same as erosion.

# now we will attempt to fill the holes in that image 
# Read the image
img = cv2.imread('blacknoise.png',0)

# Make a 7x7 kernel of ones
kernel = np.ones((7,7),np.uint8)

# Apply dilation with an iteration of 3
dilated_image = cv2.dilate(img, kernel,iterations = 3)

# Display Image
cv2.imshow("Eroded Image", dilated_image);
cv2.waitKey(0)
cv2.destroyAllWindows()

print('Next tutorial will be based on the video working')








import cv2 
import matplotlib.pyplot as plt 
import numpy as np 
print('this is tutorial number 12') 

img = cv2.imread('Mor.jpg',0) 
binr = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1] 
# define the kernel 
kernel = np.ones((5, 5), np.uint8) 

invert = cv2.bitwise_not(binr) 
erosion = cv2.erode(invert, kernel, iterations=1) 
plt.imshow(erosion, cmap='gray') 
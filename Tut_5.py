import cv2 
import numpy as np 

print("Tutorial number 5: Drawing on image") 

# This tutorial focus on drawing the circle and rectangle on the image 
# This tutorial also disscuss to put the text on the image 
# Most of the drawing functions have below parameters in common.

# img : Your Input Image
# color : Color of the shape for a BGR image, pass it as a tuple i.e. (255,0,0), for Grayscale image just pass a single scalar value from 0-255.
# thickness : Thickness of the line or circle etc. If -1 is passed for closed figures like circles, it will fill the shape. default thickness = 1
# lineType : Type of line, popular choice is cv2.LINE_AA .


# 1. Drawing a line on the image 
# We can draw a line in OpenCV by using the function cv2.line(). 
# cv2.line(img, pt1, pt2, color, [thickness])

# Params:
# pt1: First point of the line, this is a tuple of (x1,y1) point.
# pt2: Second point of the line, this is a tuple of (x2,y2) point.


# img = cv2.imread('naruto.jpg',1) 
# copy = img.copy() 

# cv2.line(copy,(300,100),(300,30), (255,255,0), 5)
# cv2.imshow("Draw Line", copy);
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 2. Drawing the circle on the image 
# We can draw a Circle in OpenCV by using the function cv2.Circle(). For drawing a circle we just need a center point and a radius.
# cv2.circle(img, Center, radius, color, [thickness])
# Params:
# center: Center of the circle.
# radius: Radius of the circle.


# img = cv2.imread('naruto.jpg',1) 
# copy = img.copy() 
# cv2.circle(copy, (360,200),100,(255,255,0),5) 
# cv2.imshow("Draw Line",copy) 
# cv2.waitKey(0) 
# cv2.destroyAllWindows()


# 3. Drawing a Rectangle
# We can also draw a rectangle in OpenCV by using the function cv2.rectangle(). You just have to pass two corners of a rectangle to draw it. It’s similar to the cv2.line function.
# cv2.rectangle(img, pt1, pt2, color, [thickness])
# Params:
# pt1: Top left corner of the rectangle.
# pt2: bottom right corner of the rectangle.


# img = cv2.imread('naruto.jpg',1) 
# copy = img.copy() 
# # drawing the rectangle on the image 
# cv2.rectangle(copy, (250,100), (450,300), (0,255,0),3)

# # Display image
# cv2.imshow("Draw Rectangle", copy);
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# 3. putting the text on the image 
# cv2.putText(img, text, origin, fontFace, fontScale, color, [thickness])

# Params:

# text: Text string to be drawn.
# origin: Top-left corner of the text (x,y) origin position.
# fontFace: Font type, we will use cv2.FONT_HERSHEY_SIMPLEX.
# fontScale: Font scale, how large your text will be.


img = cv2.imread('naruto.jpg',1) 
copy = img.copy() 

cv2.putText(copy,'sample text',(0,250),cv2.FONT_HERSHEY_SIMPLEX, 1.7, (255,255,0), 4)
# Display image
cv2.imshow("Write Text",copy);
cv2.waitKey(0)
cv2.destroyAllWindows()



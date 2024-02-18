import cv2 
import numpy as np

print('the libraries has been imported succesfully!!')

# 1.    Reading and displaying the images 
    # For displaying the image we use: 
    #         image = cv2.imread(filename, [flag]) method where: 
    #         herer: the filename is the path to the image 
    #         if 0 is passed the image is read in Grayscale (Black & white) and if -1 is used to read transparent images which we will learn in the next chapter, If no parameter is passed the image will be read in Color.
    

# img = cv2.imread('Sairaj Rajput IT VIIT.png',0)
# print(img)
# print('the shape of an image is ',img.shape)  

# The values returned are in rows, columns or you can call it height, width, or x,y. If we were dealing with a color image then img.shape would have returned height, width, channels

# 2. To display the image: 
    # For displaying the image you can use the imshow() methood 
    # cv2.imshow(Window_Name, img)
        # Params:
        # Window_Name: Any custom name you  assign to your window
        # img: Your image either be in uint8 datatype or float datatype having range 0-1
    #  Also with cv2.imshow() you will have to use the cv2.waitKey() function. This function is a keyboard binding function. Its argument is the time in milliseconds. The function waits for specified milliseconds. If you press any key in that time frame, the program continues. 
    # If 0 is passed, it waits indefinitely for a keystroke. This function returns the ASCII value of the keyboard key pressed, for e.g. if you press ESC key then it will return 27 which is the ASCII value for the ESC key. For now, we won’t be using this returned value.
    # cv2.waitKey(delay=0)
    # Note: The default delay is 0 which means wait forever until the user presses a key.

    # The last step is to destroy the window we created so the program can end, now this is not required to view the image but if you don’t destroy the window then you can’t proceed to end the program and it can crash, so to destroy the windows you will do:

    # cv2.destroyAllWindows()

    # This will destroy all present image windows, there is also a function to destroy a specific window.
    # Now let’s see the full code in action.


    # Example: 
# img = cv2.resize(img, (0,0), fx=10, fy=10)
# cv2.imshow("Image",img)

# # Wait for the user to press any key
# cv2.waitKey(0)

# # Destroy all windows
# cv2.destroyAllWindows()


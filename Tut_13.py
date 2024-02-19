import cv2
import numpy as np 

print('working with the videos')

# cap = cv2.VideoCapture(arg)
# Now there are 4 ways we can use the videoCapture Object depending what you pass in as arg:

# 1. Using Live camera feed: You pass in an integer number i.e. 0,1,2 etc e.g. cap = cv2.VideoCapture(0), now you will be able to use your webcam live stream.

# 2. Playing a saved Video on Disk: You pass in the path to the video file e.g. cap = cv2.VideoCapture(Path_To_video).

# 3. Live Streaming from URL using Ip camera or similar: You can stream from a URL e.g. cap = cv2.VideoCapture(protocol://host:port/script_name?script_params|auth) Note, that each video stream or IP camera feed has its own URL scheme.

# 4. Read a sequence of Images: You can also read sequences of images but this is not used much.

# The next step After Initializing is read from video frame by frame, we do this by using cap.read().

# ret, frame = cap.read()
# 1. ret is the boolean value.  boolean variable which either returns True if the frame was successfully read otherwise False if it fails to read the next frame. 
# 2. This will be a frame/image of our video. Now everytime we run cap.read() it will give us a new frame so we will put cap.read() in a loop and show all the frames sequentially , it will look like we are playing a video but actually we are just displaying frame by frame.
# After exiting the loop there is one last thing you must do, you must release the cap object you created by doing cap.release() otherwise your camera will stay on even after the program ends. You may also want to destroy any remaining windows after the loop.

# Initialize Video capture Object.
cap = cv2.VideoCapture('sample_video.mp4')
while(True):
    ret,frame = cap.read() 
    
    if not ret: 
        break 
    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # Show the frame we just read
    cv2.imshow('frame',gray)
        
    # Wait for the 1 millisecond, before showing the next frame.
    #  If the user presses the `q` key then exit the loop.
    if cv2.waitKey(50)  ==  ord('q'):
        break
# Release the camera
cap.release()

# Destroy the windows you created
cv2.destroyAllWindows()

    










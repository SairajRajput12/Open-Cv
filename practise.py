import cv2 
import numpy as np 

cap = cv2.VideoCapture('sample_video1.mp4')
# You can set a custom kernel size if you want
kernel = None

# Initialize background subtractor object
foog = cv2.createBackgroundSubtractorMOG2(detectShadows=True, varThreshold=50, history=2800)

# Noise filter threshold
thresh = 1100

while True:
    ret, frame = cap.read()
    if not ret:
        break
        
    # Apply background subtraction
    fgmask = foog.apply(frame)
    
    # Get rid of the shadows
    ret, fgmask = cv2.threshold(fgmask, 250, 255, cv2.THRESH_BINARY)
    
    # Apply some morphological operations to ensure a good mask
    fgmask = cv2.dilate(fgmask, kernel, iterations=1)
    
    # Detect contours in the frame
    contours, hierarchy = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        # Get the maximum contour
        cnt = max(contours, key=cv2.contourArea)

        # Make sure the contour area is somewhat higher than a threshold to ensure it's a person and not noise.
        if cv2.contourArea(cnt) > thresh:
            # Draw a bounding box around the person and label it as person detected
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
            cv2.putText(frame, 'Person Detected', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 255, 0), 1, cv2.LINE_AA)
 
    # Stack both frames and show the image
    fgmask_3 = cv2.cvtColor(fgmask, cv2.COLOR_GRAY2BGR)
    stacked = np.hstack((fgmask_3, frame))
    # Adjust window size
    cv2.imshow('Combined', cv2.resize(stacked, (800, 600)))

    k = cv2.waitKey(40) & 0xff
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

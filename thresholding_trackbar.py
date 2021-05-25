import cv2
import numpy as np

# Create a window
cv2.namedWindow('image',cv2.WINDOW_AUTOSIZE)
def nothing(x):
    pass
# Create trackbars for color change
# Hue is from 0-179 for Opencv
cv2.createTrackbar('YMin', 'image', 0, 255, nothing)
cv2.createTrackbar('UMin', 'image', 0, 255, nothing)
cv2.createTrackbar('VMin', 'image', 0, 255, nothing)
cv2.createTrackbar('YMax', 'image', 0, 255, nothing)
cv2.createTrackbar('UMax', 'image', 0, 255, nothing)
cv2.createTrackbar('VMax', 'image', 0, 255, nothing)

# Set default value for Max YUV trackbars
cv2.setTrackbarPos('YMax', 'image', 255)
cv2.setTrackbarPos('UMax', 'image', 255)
cv2.setTrackbarPos('VMax', 'image', 255)

# Initialize YUV min/max values
yMin = uMin = vMin = 0
yMax = uMax = vMax = 255

#cam_capture = cv2.VideoCapture(0)

while (1):
    image_frame = cv2.resize(cv2.imread("cloak.jpg"),(500,500))
    #_, image_frame = cam_capture.read()
    image_frame = cv2.cvtColor(image_frame,cv2.COLOR_BGR2YUV)
    yMin = cv2.getTrackbarPos('YMin', 'image')
    uMin = cv2.getTrackbarPos('UMin', 'image')
    vMin = cv2.getTrackbarPos('VMin', 'image')
    yMax = cv2.getTrackbarPos('YMax', 'image')
    uMax = cv2.getTrackbarPos('UMax', 'image')
    vMax = cv2.getTrackbarPos('VMax', 'image')

    lower = np.array([yMin,uMin,vMin])
    upper = np.array([yMax,uMax,vMax])

    mask = cv2.inRange(image_frame,lower,upper)
    cv2.imshow("mask",mask)
    if cv2.waitKey(1) and 0xFF==ord("q"):
        break

cam_capture.release()
cv2.destroyAllWindows()
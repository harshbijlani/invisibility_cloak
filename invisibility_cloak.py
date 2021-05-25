import cv2
import numpy as np

cam_capture = cv2.VideoCapture(0)
cv2.destroyAllWindows()

lower = np.array([45,108,150])
upper = np.array([117,255,255])
background = cv2.resize(cv2.imread("background.jpg"),(500,500))
out = cv2.VideoWriter("demo2.mp4", cv2.VideoWriter_fourcc(*'MP4V'), 30, (500,500))
while(cam_capture.isOpened()):
    _,image_frame = cam_capture.read()
    image_frame = cv2.resize(image_frame,(500,500))
    cv2.imshow("webcam", image_frame)
    yuv_img = cv2.cvtColor(image_frame,cv2.COLOR_BGR2YUV)
    mask = cv2.inRange(yuv_img,lower,upper)
    mask = cv2.resize(mask,(500,500))
    #cv2.imshow("mask", mask)
    background_mask = cv2.bitwise_and(background,background,mask=mask)
    inverse_background = cv2.bitwise_not(mask)
    #print("image: ",image_frame.shape)
    #print("mask: ",inverse_background.shape)
    im = cv2.bitwise_and(image_frame,image_frame,mask = inverse_background)
    final = im + background_mask
    cv2.imshow("final",final)
    #cv2.imshow("background mask", background_mask)
    cv2.imshow("inverse background mask", inverse_background)
    if cv2.waitKey(1) and 0xFF==ord("q"):
        break
    out.write(final)

out.release()
cam_capture.release()
cv2.destroyAllWindows()

import pip
!pip install opencv-python
Requirement already satisfied: opencv-python in c:\users\saurabh singh\appdata\local\programs\python\python37-32\lib\site-packages (4.1.0.25)
Requirement already satisfied: numpy>=1.14.5 in c:\users\saurabh singh\appdata\local\programs\python\python37-32\lib\site-packages (from opencv-python) (1.17.0)

You are using pip version 19.0.3, however version 19.2.1 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' commad.
import cv2
import numpy as np
cam = cv2.VideoCapture(0)
cv2.namedWindow("test")
img_counter = 0
while True:
    ret, frame = cam.read()
    cv2.imshow("test",frame)
    if not ret:
        break
    K= cv2.waitKey(1)
    if K%256 == 27:
        # ESC pressed
        print("Escape hit,closing...")
        break
    elif K%256 == 32:
        #SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
    img_counter += 1
cam.release()
cv2.destroyAllWindows()
Escape hit,closing...

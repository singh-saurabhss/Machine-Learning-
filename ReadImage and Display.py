import pip
!pip install opencv-python
Requirement already satisfied: opencv-python in c:\users\saurabh singh\appdata\local\programs\python\python37-32\lib\site-packages (4.1.0.25)
Requirement already satisfied: numpy>=1.14.5 in c:\users\saurabh singh\appdata\local\programs\python\python37-32\lib\site-packages (from opencv-python) (1.17.0)

import cv2
import numpy as np
img=cv2.imread('C:\\Users\\Saurabh singh\\Pictures\\Saved Pictures\\image.jpg')
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows(0)

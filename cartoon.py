#install opencv using the command (pip install opencv-python)
import cv2

#install opencv numpy using the command (pip install numpy)
import numpy as np

#imread function to load the image
img = cv2.imread("me.jpg")

#resize function to resize the image
img = cv2.resize(img,(450,450), fx= 0.15, fy = 0.14)

#gray conversion
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#blur background
gray = cv2.medianBlur(gray,5)

#function to mark the edges
edges= cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,9,9)

#To colourised the cartoon image
color = cv2.bilateralFilter(img,9,350,350)

#finally cartooning
cartoon = cv2.bitwise_and(color, color, mask=edges)

#To show the cartoon image
cv2.imshow("Cartoon", cartoon)

cv2.waitKey(0)

#Destroy the image by pressing any key
cv2.destroyAllWindows()

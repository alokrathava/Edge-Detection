import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 360)  # Width
cap.set(4, 480)  # Height
cap.set(10, 100)  # Brightness

while True:
    success, img = cap.read()
    imgCanny = cv2.Canny(img, 100, 100)  # Edge Detection using Canny
    cv2.imshow("Read Video", imgCanny)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

import cv2 

cap = cv2.VideoCapture(1)
cap.set(3, 1280)
cap.set(4, 720)

imgBackGround = cv2.imread('Resources/background.png')

while True:
    success, image = cap.read()

    cv2.imshow("Webcam", img)
    cv2.imshow("Face Attendance", imgBackGround)
    cv2.waitKey(1)
    
import cv2
import mediapipe as mp

Capture = cv2.VideoCapture(0)
mphands = mp.solutions.hands
hands = mphands.Hands()

while True:

    captured, vid = Capture.read()
    rotated = cv2.flip(vid, 1)
    cv2.imshow("Catured", rotated)
    cv2.waitKey(1)




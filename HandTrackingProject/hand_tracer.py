import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTIME = 0
cTIME = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)

    # detection
    if results.multi_hand_landmarks:
        for handLM in results.multi_hand_landmarks:
            for id, lm in enumerate(handLM.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy)
                # if id == 4:
                #     cv2.circle(img, (cx, cy), 10, (113, 48, 218), cv2.FILLED)
                    # print(id, cx, cy)

            mpDraw.draw_landmarks(img, handLM, mpHands.HAND_CONNECTIONS)

    # print(results.multi_hand_landmarks)
    # frame rate
    cTIME = time.time()
    fps = 1/(cTIME-pTIME)
    pTIME = cTIME

    # cv2.putText(img, str(int(fps)), (5, 70), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 0, 255))

    #video flipped
    rotated = cv2.flip(img, 1)
    resize = cv2.resize(rotated, (800, 500))
    # cv2.rotate(cv2.putText(img, str(int(fps)), (5, 70), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 0, 255)))
    cv2.imshow("Image", resize)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break



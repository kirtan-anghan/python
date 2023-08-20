import cv2
import mediapipe as mp
import math
import osascript
import time


mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands


# wCam, hCam = 640, 480
cap = cv2.VideoCapture(0)
# cap.set(3,wCam)
# cap.set(4,hCam)

pTime = 0
cTime = 0
mphand = mp.solutions.hands
hand = mphand.Hands()
draw = mp.solutions.drawing_utils

with mp_hands.Hands(
        model_complexity=0,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:
 while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hand.process(imgRGB)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            for index, lm in enumerate(hand_landmarks.landmark):
                height, width, channel = img.shape
                cx, cy = int(lm.x * width), int(lm.y * height)
            for hand_landmarks in result.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    img,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style()
                )



                # cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
                # draw.draw_landmarks(img, hand_landmarks, mphand.HAND_CONNECTIONS,mp_drawing_styles.get_default_hand_landmarks_style(),
                #      mp_drawing_styles.get_default_hand_connections_style())
                # cv2.rectangle(imgRGB, (50, 150), (85, 400), (0, 0, 0), 3)
                # print(osascript.getMasterVolume())

    lmList = []
    if result.multi_hand_landmarks:
              myHand = result.multi_hand_landmarks[0]
              for id, lm in enumerate(myHand.landmark):
                        h, w, c = imgRGB.shape
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        lmList.append([id, cx, cy])



    if len(lmList) != 0:
                    x1, y1 = lmList[4][1], lmList[4][2]
                    x2, y2 = lmList[8][1], lmList[8][2]

                    # Marking Thumb and Index finger
                    cv2.circle(imgRGB, (x1, y1), 15, (255, 0, 255))
                    cv2.circle(imgRGB, (x2, y2), 15, (255, 0, 255))
                    cv2.line(imgRGB, (x1, y1), (x2, y2), (0, 255, 0), 3)
                    length = math.hypot(x2 - x1, y2 - y1)

                    # draw.draw_landmarks(
                    i = ((length * 100) / 600 ) - 20;
                    print(length , i)
                    osascript.setMasterVolume(i)



                    cv2.line(imgRGB, (x1, y1), (x2, y2), (0, 0, 255), 3)

                    cv2.rectangle(imgRGB, (50, 150), (85, 400), (0, 0, 0), 3)
                    cv2.rectangle(imgRGB, (50, 150), (85, 400), (0, 0, 0), 3)


    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)


    cv2.imshow("Image", img)
    cv2.waitKey(1)
import numpy as np
import cv2
import mediapipe as mp

# Initialize the mediapipe hands detector
mpHands = mp.solutions.hands
hands = mpHands.Hands()

# Initialize the soundflower volume controller
vol = soundflower.Soundflower(0)
volMin, volMax = vol.get_volume_range()

# Start the webcam
cap = cv2.VideoCapture(0)

while True:
    # Get a frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to RGB
    rgbFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect the hands in the frame
    results = hands.process(rgbFrame)

    # Check if hands were detected
    if results.hands.count > 0:
        # Get the hand landmarks
        hand = results.hands[0]
        landmarkList = hand.landmark

        # Find the distance between the thumb and index finger
        length = np.hypot(landmarkList[4].x - landmarkList[8].x, landmarkList[4].y - landmarkList[8].y)

        # Adjust the volume based on the distance
        volLevel = int(volMin + (volMax - volMin) * length / 200)
        vol.set_volume(volLevel)

    # Display the frame
    cv2.imshow('Frame', frame)

    # Press `q` to quit
    if cv2.waitKey(1) == ord('q'):
        break

# Release the webcam
cap.release()
cv2.destroyAllWindows()


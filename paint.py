import cv2 
import mediapipe as mp
import numpy as np 
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

folderpath = 'Hand Tracking Project/Header'
myList = os.listdir(folderpath)
overlaylist = []

for imPath in myList:
    image = cv2.imread(f'{folderpath}/{imagePath}')
    overlaylist.append(image)

with mp_hands.Hands(min_detection_confidence=0.85, min_tracking_confidence=0.5,max_num_hands=1) as hands:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            break

            image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = hands.process(image)
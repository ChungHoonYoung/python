import cv2
import mediapipe as mp

mp_pose = mp.solutions.pose

for lndmk in mp_pose.PoseLandmark:
    print(lndmk)
    print(lndmk.value)
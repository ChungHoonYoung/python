import cv2
import mediapipe as mp
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

mp_pose = mp.solutions.pose
# pose = mp_pose.Pose()

with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, image = cap.read()
        image_h, image_w, _ = image.shape

        results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        if results.pose_landmarks :
            # print(results.pose_landmarks)

            left_shoulder = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER]
            left_elbow = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW]
            left_wrist = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST]

            shoulder_pos = (int(left_shoulder.x * image_w), int(left_shoulder.y * image_h))
            elbow_pos = (int(left_elbow.x * image_w), int(left_elbow.y * image_h))
            wrist_pos = (int(left_wrist.x * image_w), int(left_wrist.y * image_h))

            print("shoulder_pos :", shoulder_pos)
            print("elbow_pos :", elbow_pos)
            print("wrist_pos :", wrist_pos)

            cv2.circle(image, shoulder_pos, 20, (255, 0, 0), -1)
            cv2.circle(image, elbow_pos, 20, (255, 0, 0), -1)
            cv2.circle(image, wrist_pos, 20, (255, 0, 0), -1)

            cv2.imshow("My cam", image)

            key = cv2.waitKey(10)
            if (key == ord('q') or key == 27):
                break

    cap.release()
    cv2.destroyAllWindows()
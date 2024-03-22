import cv2
import mediapipe as mp
import numpy as np

def calculate_angle(a,b,c) :
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])

    angle = np.abs(radians*180.0/np.pi)

    if angle > 180.0 :
        angle = 360-angle
    
    return angle

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

        try :
            if results.pose_landmarks :
                # print(results.pose_landmarks)

                landmarks = results.pose_landmarks.landmark

                left_shoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER]
                left_elbow = landmarks[mp_pose.PoseLandmark.LEFT_ELBOW]
                left_wrist = landmarks[mp_pose.PoseLandmark.LEFT_WRIST]

                shoulder_pos = (int(left_shoulder.x * image_w), int(left_shoulder.y * image_h))
                elbow_pos = (int(left_elbow.x * image_w), int(left_elbow.y * image_h))
                wrist_pos = (int(left_wrist.x * image_w), int(left_wrist.y * image_h))

                # print("shoulder_pos :", shoulder_pos)
                # print("elbow_pos :", elbow_pos)
                # print("wrist_pos :", wrist_pos)

                cv2.circle(image, shoulder_pos, 20, (255, 0, 0), -1)
                cv2.circle(image, elbow_pos, 20, (0, 255, 0), -1)
                cv2.circle(image, wrist_pos, 20, (0, 0, 255), -1)

                cv2.line(image, shoulder_pos, elbow_pos, (255, 255, 0), 3)
                cv2.line(image, elbow_pos, wrist_pos, (0, 255, 255), 3)

                angle = calculate_angle(left_shoulder, left_elbow, left_wrist)

                cv2.putText(image, F'Angle: {round(angle, 2)}', (elbow_pos[0], elbow_pos[1], cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2, cv2.LINE_AA))


                cv2.imshow("My cam", image)

                key = cv2.waitKey(10)
                if (key == ord('q') or key == 27):
                    break

        except Exception as e :
            print(e)
            pass

    cap.release()
    cv2.destroyAllWindows()
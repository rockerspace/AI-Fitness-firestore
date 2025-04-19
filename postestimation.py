import cv2
import mediapipe as mp

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_draw = mp.solutions.drawing_utils

def get_landmarks(image):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    result = pose.process(image_rgb)
    if result.pose_landmarks:
        mp_draw.draw_landmarks(image, result.pose_landmarks, mp_pose.POSE_CONNECTIONS)
    return result.pose_landmarks

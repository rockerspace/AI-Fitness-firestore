# streamlit_app.py

import streamlit as st
import cv2
import numpy as np
import sys
import os

st.set_page_config(page_title="AI Fitness Pose Estimator", layout="wide")

st.title("🏋️‍♀️ AI Fitness Pose Estimation")

run = st.toggle("Start Webcam", value=False)
frame_window = st.image([])

if run:
    cap = cv2.VideoCapture(0)

    st.markdown("✅ Webcam started. Close this tab to stop.")
    while run and cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        frame = detect_pose(frame)

        # Convert to RGB for Streamlit
        frame_window.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    cap.release()
else:
    st.warning("⏹️ Toggle the switch to start webcam.")

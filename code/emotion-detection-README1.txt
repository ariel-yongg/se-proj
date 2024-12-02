OVERVIEW
This program captures real-time video from the webcam, detects faces, and analyzes emotions using the DeepFace 
library. The program displays the detected emotion on the screen and saves images of detected faces with their 
labeled emotion.

SETUP AND REQUIREMENTS
Python Libraries: Make sure you have the following Python packages installed:
    pip install opencv-contrib-python deepface matplotlib tf-keras
Download Haar Cascade XML File:
    This program requires the haarcascade_frontalface_default.xml file for face detection.
    Place this XML file in the same directory as the code file or in a known directory.

RUNNING THE CODE
To run the code:
    python realtime-emotion-detection.py
Press 'q' to end the program.

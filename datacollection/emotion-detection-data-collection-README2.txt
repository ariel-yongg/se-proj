OVERVIEW
The data collection script is integrated with the main program to save images of detected faces along with their 
dominant emotions. This enables collecting a dataset of labeled emotions, useful for training or further testing.

SETUP AND REQUIREMENTS
Python Libraries: Make sure you have the following Python packages installed:
    pip install opencv-contrib-python deepface matplotlib tf-keras
Download Haar Cascade XML File:
    This program requires the haarcascade_frontalface_default.xml file for face detection.
    Place this XML file in the same directory as the code file or in a known directory.
Directory Setup: 
The program automatically creates a directory called collected_data to store collected images.

RUNNING THE CODE
To run the code:
    python emotion-detection-data-collection.py

Each time a face is detected, the script analyzes the emotion, overlays it on the screen, and saves the face as 
an image in the collected_data folder.

The images are saved in the format:
collected_data/[emotion]_[timestamp]_[frame_count].jpg
where [emotion] is the detected emotion, [timestamp] is the date and time, and [frame_count] is a unique frame 
identifier.

Data Collection Directory:
All collected images will be saved to the collected_data directory created automatically in the script.

Press 'q' to end the program.

TEST CASES AND OUTCOMES
Emotion Detection: Each detected face should show an emotion label.
Image Saving: Each frame with a detected face should save a cropped face image in collected_data.

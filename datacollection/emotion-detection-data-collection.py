# libraries
import cv2
from deepface import DeepFace
import os
from datetime import datetime

# draw rectangle over face
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# video capture
capture = cv2.VideoCapture(0)

# Directory to save collected images
output_dir = "collected_data"
os.makedirs(output_dir, exist_ok=True)

# check if camera opened 
if not capture.isOpened():
    raise IOError("Error opening webcam")

# frame counter to save images
frame_count = 0

# face analysis and data collection loop
while True:
    ret, frame = capture.read()
    
    # convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.1, 4)

    # analyze and display detected emotions
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        
        try:
            # analyze face for emotion
            face_roi = frame[y:y+h, x:x+w]
            result = DeepFace.analyze(face_roi, actions=['emotion'], enforce_detection=False)
            
            # get emotion
            dominant_emotion = result[0]['dominant_emotion'] if isinstance(result, list) else result['dominant_emotion']

            
            # text to show determined emotion
            cv2.putText(frame,
                        dominant_emotion,
                        (x, y-10),
                        font,
                        0.8,
                        (0, 0, 255),
                        2)
            
            # data collection
            # save the face with the emotion label
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(output_dir, f"{dominant_emotion}_{timestamp}_{frame_count}.jpg")
            cv2.imwrite(filename, face_roi)
            print(f"Saved: {filename}")
            frame_count += 1

        except Exception as e:
            print("error", e)
            continue

    # open camera window
    cv2.imshow('Emotion Detection - Press "q" to quit', frame)
    
    # press 'q' to exit
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break

# release resources
capture.release()
cv2.destroyAllWindows()

# libraries
import cv2 as cv2
from deepface import DeepFace
import matplotlib as plt

# draw rectangle over face
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# video capture
capture = cv2.VideoCapture(0)

# check if camera opened 
if not capture.isOpened():
    capture =  cv2.VideoCapture(0)
if not capture.isOpened():
    raise IOError("error opening webcam")

# face analysis
while True:
    ret, frame =  capture.read()
    result = DeepFace.analyze(frame, actions = ['emotion'], enforce_detection=False)
    
    # convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.1, 4)
    
    # draw rectangle over face
    for(x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        font = cv2.FONT_HERSHEY_SIMPLEX
    
        try:
            
            # analyze face
            face_roi = frame[y:y+h, x:x+w]
            result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
            
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
        
        except Exception as e:
            print("error", e)
            continue
    
    # open camera window
    cv2.imshow('original video', frame)
    
    # press 'q' to exit
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break

# end
capture.release()
cv2.destroyAllWindows()
import sys
import io
import cv2
import time
from keras.models import model_from_json
import numpy as np
from functools import reduce

# Set the default encoding to utf-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Use raw strings for file paths to avoid escape character issues
json_file_path = r"emotiondetector.json"
weights_file_path = r"emotiondetector.h5"

# Load the model
try:
    with open(json_file_path, "r") as json_file:
        model_json = json_file.read()
    model = model_from_json(model_json)
    model.load_weights(weights_file_path)
except FileNotFoundError as e:
    print(f"Error loading model files: {e}")
    exit()

# Load Haar Cascade for face detection
haar_file = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(haar_file)

def extract_features(image):
    """Extracts features from the image."""
    feature = np.array(image)
    feature = feature.reshape(1, 48, 48, 1)
    return feature / 255.0

# Start webcam
webcam = cv2.VideoCapture(0)
if not webcam.isOpened():
    print("Error: Could not open webcam.")
    exit()

labels = {0: 'angry', 1: 'disgust', 2: 'fear', 3: 'happy', 4: 'neutral', 5: 'sad', 6: 'surprise'}

# Store detected emotions in a list
detected_emotions = []
start_time = time.time()  # Start the timer

while True:
    current_time = time.time()
    elapsed_time = current_time - start_time

    if elapsed_time > 30:  # Stop after 30 seconds
        break

    ret, im = webcam.read()
    if not ret:
        print("Failed to capture image")
        break

    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        face_image = gray[y:y+h, x:x+w]
        cv2.rectangle(im, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        face_image = cv2.resize(face_image, (48, 48))
        img = extract_features(face_image)
        
        try:
            pred = model.predict(img)
            prediction_label = labels[np.argmax(pred)]
            detected_emotions.append(prediction_label)  # Append detected emotion
            cv2.putText(im, prediction_label, (x, y-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2)
        except Exception as e:
            print(f"Error during prediction/display: {e}")

    cv2.imshow("Output", im)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
webcam.release()
cv2.destroyAllWindows()


emo_score_1 = {'angry': 0.8, 'disgust': 0.6, 'fear': 0.9, 'happy': 0.1, 'neutral': 0.3, 'sad': 0.7, 'surprise': 0.6}

emo_score_2 = {'angry': 0.8, 'disgust': 0.6, 'fear': 0.9, 'happy': 0.1, 'neutral': 0.0, 'sad': 0.7, 'surprise': 0.6}

emo_count = {'angry': 0, 'disgust': 0, 'fear': 0, 'happy': 0, 'neutral': 0, 'sad': 0, 'surprise': 0}

total_score=reduce(lambda x,y:x+emo_score_1[y],detected_emotions,0)
print(f"Detected emotions over 30 seconds: {detected_emotions}")
print(f"No. of emotions: {len(detected_emotions)}")
print(f"total emotion score: {total_score:.3f}")
print(f"total average score: {(total_score/len(detected_emotions)):.3f}")

detected_emotions_without_neutral=[ i for i in detected_emotions if  i!='neutral']
total_score_without_neutral=reduce(lambda x,y:x+emo_score_1[y],detected_emotions_without_neutral,0)
print(f"Detected emotions over 30 seconds without neutral: {detected_emotions_without_neutral}")
print(f"No. of emotions without neutral: {len(detected_emotions_without_neutral)}")
print(f"total emotion score: {total_score_without_neutral:.3f}")
print(f"total average score without neutral: {(total_score_without_neutral/len(detected_emotions_without_neutral)):.3f}")


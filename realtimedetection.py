import sys
import io
import cv2
from keras.models import model_from_json
import numpy as np

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

while True:
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

import cv2
import threading
import time
import firebase_admin
import os
from firebase_admin import credentials, db
from google.cloud import vision
from flask import Flask, render_template, Response
from dotenv import load_dotenv

load_dotenv()

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {'databaseURL': os.getenv('DATABASE_URL')})
vision_client = vision.ImageAnnotatorClient.from_service_account_json("serviceAccountKey.json")

app = Flask(__name__)
camera = cv2.VideoCapture(0)

def cloud_compute_worker():
    while True:
        success, frame = camera.read()
        if success:
            _, encoded_image = cv2.imencode('.jpg', frame)
            image = vision.Image(content=encoded_image.tobytes())
            
            # Compute: Label Detection
            response = vision_client.label_detection(image=image)
            if response.label_annotations:
                label = response.label_annotations[0].description
                # Push to Firebase
                db.reference('live_status').set({
                    'object': label,
                    'timestamp': time.strftime("%H:%M:%S")
                })
        elif (not success):
            DatabaseNotAvaiable()
            
        time.sleep(5) 

threading.Thread(target=cloud_compute_worker, daemon=True).start() # for clarification: this thread runs in the background for camera sync to the Google Cloud API

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    def gen():
        while True:
            _, frame = camera.read()
            _, buffer = cv2.imencode('.jpg', frame)
            yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
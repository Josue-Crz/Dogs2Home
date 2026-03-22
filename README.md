# Dogs2Home
### "Leave no surprises, correct behavior one detection at a time."
Dog2Home is a full-stack Internet of Things (IoT) application built in under 24 hours. Inspired by the Ring home monitoring system, this project focuses on high-stakes pet monitoring. By leveraging Google Cloud Vision, Dog2Home identifies when your dog is causing damage to furniture and provides instantaneous alerts, ensuring you can intervene before the stuffing hits the floor.
#
### Key Features
Real-Time Detection: Utilizes Google Cloud Vision API to analyze video frames for specific destructive behaviors or damaged objects.

Instant Alerts: Sends immediate notifications when a "furniture destruction" event is triggered.

Live Telemetry Dashboard: A web-based interface that displays real-time data from the home environment.

Integrated Database: Uses a real-time database to log history, timestamps, and detection confidence levels.
#
### Tech Stack
Frontend: Flask (for the real-time monitoring dashboard & MVP demonstration)

Backend: Python

Cloud AI: Google Cloud Vision API

Database(DB): Firebase Realtime DB

Hardware: WIP

#
### Installation & Setup

### Prerequisites:
Create a .env file in the root directory and add the following credential variable(s) once you've created your Firebase DB alongside Google Cloud API: 

DATABASE_URL="https://myweblink.firebaseio.com/"

#
### Clone the repository
running: "git clone https://github.com/Josue-Crz/Dogs2Home.git"

### Navigate to the directory
running: "cd Dog2Me"

#

### Locally install Flask onto your local machine via pip & running the app:

running: "pip install Flask && python3 app.py"



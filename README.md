# 🚗 Traffic Detection & Vehicle Counting Web App

A real-time traffic detection and vehicle counting **web application** built using **FastAPI**, OpenCV, and deep learning. It detects and counts vehicles in uploaded or live-streamed videos to assist in traffic monitoring and smart city planning.

## 📌 Features

- 🌐 FastAPI-based backend
- 🔍 Real-time vehicle detection using YOLOv4/SSD
- 🚗 Vehicle counting by category (cars, bikes, trucks, etc.)
- 📤 Upload video files or use webcam
- 🎥 Output video with bounding boxes and counters
- 📁 Clean and modular structure

## 🧰 Tech Stack

- Python
- FastAPI
- Uvicorn
- OpenCV
- NumPy
- Pandas (optional)
- Jinja2 (via `templates/` folder for HTML)

## Requirements
- fastapi==0.110.1
- uvicorn==0.29.0
- python-multipart==0.0.9
- opencv-python==4.9.0.80
- numpy==1.26.4
- ultralytics==8.0.226  # for YOLOv5
  
## 📂 Folder Structure

traffic-detection-counter/
├── data/ # Uploaded or test videos
├── static/ # Output/result videos with detections
├── templates/ # HTML templates for the frontend (Jinja2)
├── main.py # FastAPI app entry point
├── detect_vehicle.py # Vehicle detection and counting logic
├── requirements.txt # Project dependencies
└── README.md # Project documentation


## ▶️ Running the App

- Start the FastAPI server using Uvicorn:  uvicorn main:app --reload
- The app will be available at: http://127.0.0.1:8000

- Visit /docs for the interactive Swagger API documentation

- Upload a video via the frontend form or API endpoint to process it

  ## UI (images)
  ![Screenshot (240)](https://github.com/user-attachments/assets/42b657d2-499a-4867-a153-b1af8d6f7d07)
  ![Screenshot (242)](https://github.com/user-attachments/assets/e72c9590-6ef5-4484-a6b0-bcc0460fbae7)



## 🖥️ API Endpoints

| Method | Endpoint          | Description                                                 |
|--------|-------------------|-------------------------------------------------------------|
| GET    | `/`               | Renders the home page with a video upload form              |
| POST   | `/upload-video`   | Accepts video file uploads and processes them for detection |
| GET    | `/result/{file}`  | Returns the processed output video from the `static/` folder|
| GET    | `/docs`           | Opens the interactive Swagger UI for API testing            |
| GET    | `/redoc`          | Opens the ReDoc API documentation                           |

  
## 🏗️ Future Enhancements
- Vehicle speed estimation

- ANPR (license plate recognition)

- User authentication for saved history

- Deploy on cloud (Heroku, Render, AWS, etc.)

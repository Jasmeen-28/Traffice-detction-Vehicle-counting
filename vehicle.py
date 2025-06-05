import cv2
from ultralytics import YOLO
import time

uploaded_video_path = "output(compress-video-online.com).mp4"
processed_video_path = "processed_output.mp4"

model = YOLO("yolov8n.pt")
vehicle_classes = ['car', 'truck', 'bus', 'motorcycle']

def detect_and_stream(video_path):
    cap = cv2.VideoCapture(video_path)
    count_line = 600
    offset = 8
    detect = []
    counter = 0

    interval = 10
    interval_counter = 0
    status = 'Analyzing...'
    color = (0, 0, 255)
    last_check_time = time.time()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)[0]
        for result in results.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = result
            class_name = model.names[int(class_id)]

            if class_name in vehicle_classes:
                x1, y1, x2, y2 = map(int, [x1, y1, x2, y2])
                center = ((x1 + x2) // 2, (y1 + y2) // 2)
                detect.append(center)
                
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, class_name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 0), 2)

        for cx, cy in detect[:]:
            if (count_line - offset) < cy < (count_line + offset):
                counter += 1
                interval_counter += 1
                detect.remove((cx, cy))

        current_time = time.time()
        if current_time - last_check_time >= interval:
            if interval_counter < 10:
                status = 'Smooth Traffic'
                color = (0, 255, 0)
            else:
                status = 'Congested Traffic'
                color = (255, 0, 0)
            interval_counter = 0
            last_check_time = current_time

        cv2.putText(frame, f"Traffic: {status}", (50, 120), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)
        cv2.putText(frame, f"Vehicles: {counter}", (450, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()

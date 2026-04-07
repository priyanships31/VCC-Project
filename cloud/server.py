from flask import Flask, request, jsonify
from ultralytics import YOLO
import numpy as np
import cv2

# Initialize Flask app
app = Flask(__name__)

# Load YOLO model
model = YOLO("yolov8n.pt")

@app.route('/')
def home():
    return "Edge-Cloud AI Server is Running!"

@app.route('/detect', methods=['POST'])
def detect():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files['image']
    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)

    results = model(img)
    labels = results[0].names

    detections = []

    for box in results[0].boxes:
        cls_id = int(box.cls.item())   # FIXED
        label = labels[cls_id]

        x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())  # FIXED

        detections.append({
            "label": label,
            "box": [x1, y1, x2, y2]
        })

    return jsonify({"detections": detections})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

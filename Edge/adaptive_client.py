import cv2
import requests
import time
import csv
from ultralytics import YOLO

CLOUD_URL = "http://35.222.188.129:5000/detect"

edge_model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)

# 🔥 CSV setup
csv_file = open("results.csv", mode="w", newline="")
csv_writer = csv.writer(csv_file)

# Header
csv_writer.writerow(["Frame", "Mode", "Latency(s)", "Num_Objects"])

frame_id = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_id += 1
    start = time.time()

    # -------------------------------
    # EDGE INFERENCE
    # -------------------------------
    edge_results = edge_model(frame)
    annotated_frame = edge_results[0].plot()
    num_objects = len(edge_results[0].boxes)

    latency = time.time() - start

    # -------------------------------
    # DECISION LOGIC
    # -------------------------------
    if num_objects > 3 or latency > 0.3:
        use_cloud = True
    else:
        use_cloud = False

    # -------------------------------
    # PROCESSING
    # -------------------------------
    if use_cloud:
        mode = "CLOUD"
        print("☁️ Using CLOUD")

        try:
            _, img_encoded = cv2.imencode('.jpg', frame)

            response = requests.post(
                CLOUD_URL,
                files={"image": img_encoded.tobytes()},
                timeout=2
            )

            data = response.json()
            detections = data.get("detections", [])

            for det in detections:
                label = det["label"]
                x1, y1, x2, y2 = det["box"]

                cv2.rectangle(annotated_frame, (x1, y1), (x2, y2),
                              (0, 0, 255), 2)

                cv2.putText(annotated_frame, label,
                            (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6,
                            (0, 0, 255),
                            2)

        except Exception as e:
            print("⚠️ Cloud failed, fallback to EDGE")
            print("Error:", e)
            mode = "EDGE"

    else:
        mode = "EDGE"
        print("💻 Using EDGE")

    # -------------------------------
    # 🔥 SAVE DATA TO CSV
    # -------------------------------
    csv_writer.writerow([frame_id, mode, latency, num_objects])

    # -------------------------------
    # DISPLAY INFO
    # -------------------------------
    cv2.putText(annotated_frame, mode,
                (10, 400),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 0, 0),
                2)

    cv2.putText(annotated_frame, f"Latency: {latency:.2f}s",
                (10, 430),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255, 255, 0),
                2)

    cv2.imshow("Adaptive Edge-Cloud System", annotated_frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
csv_file.close()
cv2.destroyAllWindows()
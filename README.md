# 🎥 Adaptive Edge-Cloud Object Detection System

This project implements an **adaptive object detection pipeline** using a combination of **edge (local) inference** and **cloud-based inference**. It dynamically switches between local YOLO processing and remote server detection based on performance.

---

## 🚀 Features

* 📷 Real-time video capture using OpenCV
* 🧠 Local object detection with YOLOv8 (edge model)
* ☁️ Cloud-based detection via API
* ⚡ Adaptive switching between edge and cloud modes
* 📊 Latency and detection logging to CSV

---

## 🛠️ Tech Stack

* Python 3.x
* OpenCV (`cv2`)
* Ultralytics YOLOv8
* Flask
* Requests (for API calls)
* CSV logging

---

## 📁 Project Structure

project/
│
├── Edge/
│   ├── adaptive_client.py   # Adaptive edge-cloud switching logic
│   ├── client.py            # Sends image to cloud API
│   ├── edge-test.py         # Local YOLO testing script
│   ├── yolov8n.pt           # YOLOv8 model (edge)
│   ├── results.csv          # Logged performance results
│   └── test.png             # Sample test image
│
├── Cloud/
│   ├── server.py            # Flask server with YOLO inference
│   ├── test.py              # Cloud-side testing script
│   └── yolov8n.pt           # YOLOv8 model (cloud)
│
└── README.md                # Project documentation
---

## ⚙️ Installation

```bash
git clone <repo-url>
cd project
python3 -m venv venv
pip install -r requirements.txt
```

If needed:

```bash
pip install opencv-python
```

---

## ▶️ Usage
run in cloud 

```bash
cd cloud
python3 server.py

```
run in local
```bash
cd edge
python3 adaptive_client.py
```


---

## 🌐 Cloud Configuration

```python
CLOUD_URL = "http://<your-server-ip>:5000/detect"
```

---

## 📊 CSV Output (results.csv)

The system logs performance and detection data into `results.csv`.

### 🧾 CSV Columns

| Column Name | Description                |
| ----------- | -------------------------- |
| Frame       | Frame number               |
| Mode        | `Edge` or `Cloud`          |
| Latency (s) | Time taken for detection   |
| Num_Objects | Number of detected objects |

---

### 📄 Example Output

```
Frame,Mode,Latency(s),Num_Objects
0,Edge,0.045,3
1,Edge,0.052,2
2,Cloud,0.210,4
3,Edge,0.048,1
```

### 📊 Comparison and Analysis

| Metric      | Edge Only      | Cloud Only | Proposed System     |
| ----------- | -------------- | ---------- | ------------------- |
| Latency     | ✅ Low (~0.03s) | ❌ High     | ✅ Optimized         |
| Accuracy    | ⚠️ Medium      | ✅ High     | ✅ High              |
| Cost        | ✅ Low          | ❌ High     | ✅ Balanced          |
| Scalability | ❌ Limited      | ✅ High     | ✅ Adaptive          |
| Flexibility | ❌ Static       | ❌ Static   | ✅ Dynamic Switching |


### 🏗️ Architecture Diagram

        +------------------+
        |   Webcam Input   |
        +--------+---------+
                 |
                 v
        +------------------------------+
        |         Edge Device          |
        |  YOLOv8 (Local Inference)    |
        |  OpenCV + Python Client      |
        +--------+---------------------+
                 |
     Measure Latency & Object Count
                 |
        +--------+---------+
        | Decision Engine  |
        +--------+---------+
                 |
     +-----------+-----------+
     |                       |
     v                       v
+----------------+   +------------------------------+
| Edge Result    |   |        Cloud Server          |
| (YOLO Output)  |   | Flask API + YOLOv8 Model     |
+----------------+   +-------------+----------------+
                                      |
                                      v
                           +------------------------+
                           | Cloud YOLO Inference   |
                           | (via Flask API)        |
                           +----------+-------------+
                                      |
                                      v
                           +------------------------+
                           |   Final Output Display |
                           +------------------------+

## 🧠 How It Works

1. Capture frame from webcam
2. Run YOLO locally
3. Measure latency
4. If latency exceeds threshold → switch to cloud
5. Log results into CSV


---

## 📌 Future Improvements

* Intelligent switching (ML-based decision)
* GPU acceleration
* Real-time dashboard for CSV visualization
* Edge model optimization


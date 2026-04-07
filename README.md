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
* Requests (for API calls)
* CSV logging

---

## 📁 Project Structure

```
Edge/
│── adaptive_client.py
│── edge-test.py
│── client.py
│── yolov8n.pt
│── requirements.txt
│── results.csv        # Generated output file
│── test.png
```

---

## ⚙️ Installation

```bash
git clone <your-repo-url>
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


# 🎥 Adaptive Edge-Cloud Object Detection System

This project uses a combination of edge and cloud computing to balance speed and computational power.

⚡ Edge (Local Processing)

*Handles simple frames quickly with low latency, enabling real-time performance without network delay.

☁️ Cloud (Remote Processing)

*Handles complex frames that require more computation, such as scenes with many objects or higher processing time.

🔄 Adaptive Switching

The system intelligently switches between edge and cloud based on:

*Number of detected objects
*Processing latency

👉 Benefits
*Fast response for simple tasks (edge)
*Accurate and efficient processing for complex tasks (cloud)

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

 <img width="1341" height="1173" alt="image" src="https://github.com/user-attachments/assets/2c560dda-8fed-4419-82dd-8619a17d7c70" />

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


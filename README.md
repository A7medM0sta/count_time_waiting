Here’s a revised version of the instructions focused solely on video processing, with outputs directed to a specific output folder, and made more readable:

---

# Video Time Analysis

## 👋 Introduction

This project demonstrates the use of computer vision techniques to analyze wait times and monitor the duration that objects or individuals spend in predefined zones within video frames. It's ideal for applications like retail analytics or traffic management.


## Sample Outputs
##### Analysis For Customer Waiting Time 
![Checkout](/assets/market.png)

##### Analysis For Cars Waiting  Time 
![Checkout](/assets/traffic.png)


## 💻 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/A7medM0sta/time_analysis.git  
cd time_analysis
```

### Step 2: Set Up the Python Environment (Optional)

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Required Dependencies

```bash
pip install -r requirements.txt
```

## 🛠 Video Processing Scripts

### `download_from_youtube`

This script downloads videos from YouTube.

- **`--url`**: The full URL of the YouTube video to download.
- **`--output_path`**: Directory to save the downloaded video (default: `output` folder).
- **`--file_name`**: Name of the saved video file.

Example Usage:

```bash
python scripts/download_from_youtube.py \
--url "https://www.youtube.com/watch?v=-8zyEwAa50Q" \
--output_path "output/checkout" \
--file_name "video.mp4"
```

```bash
python scripts/download_from_youtube.py \
--url "https://www.youtube.com/watch?v=MNn9qKG2UFI" \
--output_path "output/traffic" \
--file_name "video.mp4"
```

### `draw_zones`

Use this script to design custom zones on your video. The zones are saved as a JSON file.

- **`--source_path`**: Path to the video file.
- **`--zone_configuration_path`**: Path to save the polygon annotations (as a JSON file).

**Key Controls**:
- `Enter`: Finish drawing the current polygon.
- `Escape`: Cancel drawing the current polygon.
- `Q`: Quit the drawing window.
- `S`: Save zone configuration to a JSON file.

Example Usage:

```bash
python scripts/draw_zones.py \
--source_path "output/checkout/video.mp4" \
--zone_configuration_path "output/checkout/config.json"
```

```bash
python scripts/draw_zones.py \
--source_path "output/traffic/video.mp4" \
--zone_configuration_path "output/traffic/config.json"
```

### `inference_file_example`

Run object detection on a video file using the Roboflow Inference model.

- **`--zone_configuration_path`**: Path to the zone configuration JSON file.
- **`--source_video_path`**: Path to the video file.
- **`--model_id`**: Roboflow model ID.
- **`--classes`**: List of class IDs to track (optional).
- **`--confidence_threshold`**: Confidence level for detections (default: `0.3`).
- **`--iou_threshold`**: IOU threshold for non-max suppression (default: `0.7`).

Example Usage:

```bash
python inference_file_example.py \
--zone_configuration_path "output/checkout/config.json" \
--source_video_path "output/checkout/video.mp4" \
--model_id "yolov8x-640" \
--classes 0 \
--confidence_threshold 0.3 \
--iou_threshold 0.7
```
```bash
python inference_file_example.py \
--zone_configuration_path "output/traffic/config.json" \
--source_video_path "output/traffic/video.mp4" \
--model_id "yolov8x-640" \
--classes 2 5 6 7 \
--confidence_threshold 0.3 \
--iou_threshold 0.7
```

# Background Removal With OpenCV

A small Python script that removes the background from a live webcam feed in real time. It uses OpenCV to capture and display frames and the cvzone `SelfiSegmentation` module (built on MediaPipe selfie segmentation) to separate the person from the background.

## Features

- Captures video from the default webcam at 640x480
- Segments the person in each frame and replaces the background with a solid magenta colour
- Shows the original feed and the result in two separate windows
- Press `q` to quit

## Tech Stack

- Python
- OpenCV (`opencv-python`)
- cvzone
- MediaPipe

## Project Structure

```
.
├── main.py            # webcam capture and background removal loop
├── requirements.txt
└── README.md
```

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/Hamza-Tahirr/Background-Removal-With-OpenCV.git
   cd Background-Removal-With-OpenCV
   ```

2. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS / Linux
   source venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Make sure a webcam is connected, then run:

```bash
python main.py
```

Two windows open: `Image` shows the raw camera feed and `Image Out` shows the frame with the background removed. Press `q` in one of the windows to stop.

Recent versions of cvzone download the MediaPipe selfie segmentation model (`selfie_segmenter.tflite`) into the current folder the first time the script runs, so an internet connection is needed on the first run.

## Customising

- To use a different camera, change the index in `cv2.VideoCapture(0)`.
- To change the background colour, edit the BGR tuple passed to `segmentor.removeBG(img, (255, 0, 255))`. You can also pass an image of the same size as the frame instead of a colour.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

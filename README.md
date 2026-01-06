## Human Emotion Recognition using OpenCV

A real-time human emotion recognition system that detects and classifies facial emotions using a webcam and OpenCV.

---

### About the Project

This project implements a real-time emotion recognition system using computer vision and a pre-trained facial emotion recognition model.  
It captures live video from a webcam, detects facial expressions, and classifies human emotions such as happy, sad, angry, surprised, and neutral in real time.

---

### Features

- Real-time emotion detection using webcam  
- Facial emotion classification on live video feed  
- Bounding box and emotion label visualization  
- Lightweight and easy-to-run implementation  
- CPU-based execution (no GPU required)  

---

### Technologies Used

- Python  
- OpenCV  
- facial-emotion-recognition library  
- NumPy  

---

### How to Run

1. Install required dependencies:
   ```bash
   pip install opencv-python facial-emotion-recognition numpy

2. Run the emotion recognition script:
    ```bash
   python main.py

3. Press ESC to exit the application.

---

### Project Folder Structure

human-emotion-recognition-opencv/
│
├── main.py                 # Emotion recognition script
├── README.md               # Project documentation
├── requirements.txt        # Required libraries
└── assets/                 # Sample outputs (optional)

---

## Working Principle

- Capture video frames using a webcam  
- Detect faces from the live video feed  
- Analyze facial expressions using a pre-trained model  
- Classify emotions for each detected face  
- Display emotion labels on the video stream in real time  

---

## Applications

- Human–computer interaction  
- Emotion-aware systems  
- Behavioral analysis  
- Mental health research (educational use)  
- Learning computer vision and AI concepts  

---

## Output

- Real-time webcam feed with detected emotions  
- Emotion labels displayed on detected faces  

---

### License

This project is intended for educational purposes.

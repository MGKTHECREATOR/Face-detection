👁️ Face Detection using OpenCV

This is a simple **real-time face detection project** built using **Python** and **OpenCV**.
The program captures video from your **webcam** and detects faces using **Haar Cascade Classifier**.

🚀 Features

* ✅ Detects faces in real-time using webcam
* ✅ Draws bounding boxes around detected faces
* ✅ Displays number of faces on screen
* ✅ Labels each face with "Face"
* ✅ Press **S** to take a snapshot
* ✅ Press **ESC** to exit

📂 Project Structure

📁 Face-Detection
 ┣ 📜 face_detect.py     # Main code
 ┣ 📜 README.md          # Project documentation


🛠️ Requirements

* Python 3.x
* OpenCV library

Install dependencies:

bash
pip install opencv-python


▶️ How to Run

1. Clone this repository:

   bash
   git clone https://github.com/yourusername/face-detection.git
   cd face-detection
   
2. Run the script:

   bash
   python face_detect.py
   
3. A window will open with your webcam feed:

   * Green boxes = Detected faces
   * "Faces: N" = Number of faces detected
   * Press **S** → Save a snapshot
   * Press **ESC** → Exit

🔮 Future Improvements

* Add **face blur mode** for privacy
* Detect **eyes, smile, or full body**
* Integrate with **Deep Learning (DNN/YOLO)** for higher accuracy

📜 License

This project is open-source under the [MIT License](LICENSE).

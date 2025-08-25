import cv2

face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
webcam = cv2.VideoCapture(0)

while True:
    _, img = webcam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face.detectMultiScale(gray, 1.5, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
        cv2.putText(img, "Face", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.9, (0, 255, 0), 2)

    # Show number of faces
    cv2.putText(img, f"Faces: {len(faces)}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    cv2.imshow("find face", img)

    key = cv2.waitKey(10)
    if key == 27:   # ESC to exit
        break
    if key == ord('s'):  # 's' to save snapshot
        cv2.imwrite("snapshot.jpg", img)
        print("Snapshot saved!")

webcam.release()
cv2.destroyAllWindows()

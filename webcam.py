import cv2

webcam = cv2.VideoCapture(0)
while True:
    status, frame = webcam.read()
    if not status:
        print("Camera not working")
        break
    cv2.imshow("Webcam", frame)
# press esc to exit
    
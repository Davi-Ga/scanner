import cv2 as cv 

cam = cv.VideoCapture()
capturing = True
ip = "https"


cam.open(ip)

while capturing:

    status, frame = cam.read()

    if not status:
        print("Failed to read frame from camera. Please check your camera.")
        capturing = False
        continue

    if cv.waitKey(1) & 0xff == ord('q'):
        capturing = False

    cv.imshow("Camera", frame)
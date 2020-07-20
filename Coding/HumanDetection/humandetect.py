import cv2
from random import randrange

trained_body_data = cv2.CascadeClassifier("haarcascade_fullbody.xml")

webcam = cv2.VideoCapture(0)

while True:
    # current frame
    success, frame = webcam.read()

    # covert to grayscale
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect the faces
    face_coordinates = trained_body_data.detectMultiScale(grayscaled_img)

    # draws the rectangles
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (randrange(256), randrange(256), randrange(256)), 1)

    cv2.imshow("box", frame)
    key = cv2.waitKey(1)

    if key==81 or key==113:
        break

webcam.release()

print("Code Completed")

import cv2
from random import randrange


trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#img = cv2.imread('download.jpg')

# Get capture from webcam
webcam = cv2.VideoCapture(0)

while True:
    # current frame
    success, frame = webcam.read()

    # covert to grayscale
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("box", grayscaled_img)
    cv2.waitKey(1)

"""
# detect the faces
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

# draws the rectangles
cv2.rectangle(img, face_coordinates,(randrange(256), randrange(256), randrange(256)), 1)

# shows the color image with boxes
"""

print("Code Completed")

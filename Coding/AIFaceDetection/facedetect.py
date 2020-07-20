import cv2
from random import randrange


trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('download.jpg')

grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

cv2.rectangle(img, face_coordinates,(randrange(256), randrange(256), randrange(256)), 1)

cv2.imshow("box", img)

cv2.waitKey()

print("Code Completed")

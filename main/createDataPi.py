#creating database
import cv2, sys, numpy, os, picamera
from time import sleep
haar_file = 'haarcascade_frontalface_default.xml'
datasets = 'datasets'  #All the faces data will be present this folder
sub_data = raw_input("Enter Name: ")     #These are sub data sets of folder, for my faces I've used my name

path = os.path.join(datasets, sub_data)
if not os.path.isdir(path):
    os.mkdir(path)
(width, height) = (130, 100)    # defining the size of images 


face_cascade = cv2.CascadeClassifier(haar_file)
# initialize the camera and grab a reference to the raw camera capture#'0' is use for my webcam, if you've any other camera attached use '1' like this
camera = picamera.PiCamera(resolution=(480, 320))
camera.vflip = True

# The program loops until it has 30 images of the face.
count = 1
while count < 10:
    camera.capture('face.jpg')
    im = cv2.imread('face.jpg')
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
    for (x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (width, height))
        cv2.imwrite('%s/%s.png' % (path,count), face_resize)
    count += 1

    key = cv2.waitKey(10)
    if key == 27:
        break

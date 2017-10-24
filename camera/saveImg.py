#Dummy Code snippet to save image
import picamera
import time
import cv2
 
# initialize the camera and grab a reference to the raw camera capture
camera = picamera.PiCamera()
camera.vflip = True
camera.capture('test.jpg')


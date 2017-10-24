from SimpleCV import *
from time import sleep

#cam = Camera()
#sleep(2)
'''
print 'capturing'
image = cam.getImage().scale(320, 240)
print 'captured'
image.save("password.jpg")
'''
template = Image('password.jpg')
img = Image('password.jpg')
match = img.findKeypointMatch(template)

if match:
	print 'Match Found'
else:
	print 'No Matches Found'

#img.show()


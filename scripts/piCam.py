import picamera
from imageUpload import uploadImage
from time import sleep
import os
import sys

def main():
        imgDest = sys.argv[1]
	counter = 0
	camera = picamera.PiCamera()
        while counter < 100:
		imgName = 'TestImg' + str(counter) + '.jpg'
		camera.capture(imgName)
		uploadImage(imgDest, imgName)
		os.remove(imgName)
		counter += 1
		sleep(5)

if __name__ == '__main__':
	main()

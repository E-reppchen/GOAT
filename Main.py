import numpy
import picamera
import time

if __name__ == "__main__":
	main()

def main():	
	#camera used referenced as camera
	camera = PiCamera()
	#resolution of camera
	camera.resolution = (320, 240)
	#frame rate
	camera.framerate = 2
	#dimensionality of input frames
	arrayFormat = PiRGBArray(camera, size=(320, 240))
	time.sleep(2)
	for i, image in enumerate(camera.capture_continuous(arrayFormat, format = 'bgr', use_video_port = True)):
		#numpy version of the image
		inputArray = image.array

import numpy as np
import picamera
import time

if __name__ == "__main__":
	main()

def timeMatrix(currentArray, previousArray):
	#time matrix is the current matrix - the previous matrix
	timeMatrix = currentArray - previousArray
	#make current matrix the next previous matrix
	previousArray = currentArray
	return (timeMatrix, previousArray)

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
		#dimension of the array
		dimensions = inputArray.shape
		#we make an empty array of the same dimensions to start off with
		if i == 0:
			previousArray = np.zeros(dimensions)
		#we might have to declare timeArray beforehand (timeArray = np.zeros(dimensions))
		timeArray, previousArray = timeMatrix(currentArray, previousArray)

import numpy as np

def timeMatrix(currentArray, previousArray):
	timeMatrix = currentArray - previousArray
	print(previousArray)
	previousArray = currentArray
	print(timeMatrix)
	return previousArray

def main():
	#previous array would be declared in an if statement in main method at beginning of program
	#if timeStep==0:
	#	previousArray = np.zeros(currentArray.shape)
	currentArray = np.array([[1,2], [3,4]])
	previousArray = np.zeros(currentArray.shape)
	previousArray = timeMatrix(currentArray, previousArray)
	currentArray = np.array([[2,3], [4,5]])
	previousArray = timeMatrix(currentArray, previousArray)

if __name__ == "__main__":
    main()

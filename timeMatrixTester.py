import numpy as np

def timeMatrix(currentArray, previousArray):
	#time matrix is the current matrix - the previous matrix
	timeMatrix = currentArray - previousArray
	#note that the print statements are just to see the changes
	#they will not be in the actual program
	print(previousArray)
	#make current matrix the next previous matrix
	previousArray = currentArray
	print(timeMatrix)
	return previousArray

def main():
	#previous array would be declared in an if statement at the beginning of the main program 
	#if timeStep==0:
	#	previousArray = np.zeros(currentArray.shape)
	#***
	#so to test it we first make a custom 2 by 2 array
	currentArray = np.array([[1,2], [3,4]])
	#we make an empty array of the same dimensions to start off
	previousArray = np.zeros(currentArray.shape)
	#we input that into the timeMatrix method and make the new previousMatrix the return of that method
	#in the actual code it will return two things - the previous array and the time matrix
	previousArray = timeMatrix(currentArray, previousArray)
	#new current array
	currentArray = np.array([[2,3], [4,5]])
	previousArray = timeMatrix(currentArray, previousArray)

if __name__ == "__main__":
	#run the program    
	main()

import numpy

def timeMatrix(currentArray, timeStep):
  if timeStep == 0:
    previousArray = np.zeros(currentArray.shape)
  timeMatrix = currentArray - previousArray
  previousArray = currentArray
  return timeMatrix

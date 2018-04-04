import numpy as np

def differenceMatrix(dimensions, inputArray, n):
  x, y, z = dimensions
  n = n-1
  point = [n, n, n]
  point2 = [n, n, n]
  diffArray = np.zeros(dimensions)
  timeUsedArray = np.zeros(dimensions)
  localAv = 0
  for i in range(point[2], z):
    point2[1] = n
    point2[0] = n
    for i in range(point[1], y):
      point2[0] = n
      for i in range(point[0], x):
        for j in range(point2[2] - n, point[2]+1): 
          for k in range(point2[1] - n, point[1]+1):
            for l in range(point2[0] - n, point[0]+1):
              localAv += inputArray[l][k][j]
        localAv = localAv/(n*n*n)
        for j in range(point2[2] - n, point2[2]+1):
          for k in range(point2[1] - n, point2[1]+1):
            for l in range(point2[0] - n, point2[0]+1):
              percentDiff = (abs(inputArray[l][k][j] - localAv))/localAv*100.00        
              diffArray[l][k][j] += percentDiff
              timeUsedArray[l][k][j] += 1
        point2[0] += 1
        localAv = 0
      point2[1] += 1 
    point2[2] += 1
    
  for i in range(z):
    for j in range(y):
      for k in range(x):
        diffArray[k][j][i] = diffArray[k][j][i]/timeUsedArray[k][j][i]
  
  return diffArray

if __name__ == "__main__":
  inputArray = np.random.rand(64, 324, 3)
  dimensions = inputArray.shape
  diffArray = differenceMatrix(dimensions, inputArray, 3)
  print(diffArray)

import numpy as np

def differenceMatrix(dimensions, inputArray, n):
  x, y, z = dimensions
  n = n-1
  point = [n, n, n]
  diffArray = np.zeros(dimensions)
  timeUsedArray = np.zeros(dimensions)
  localAv = 0
  for c in range(point[2], z):
    for b in range(point[1], y):
      for a in range(point[0], x):
        for j in range(c - n, c+1): 
          for k in range(b - n, b+1):
            for l in range(a - n, a+1):
              localAv += inputArray[l][k][j]
        localAv = localAv/(n*n*n)
        for j in range(c - n, c+1):
          for k in range(b - n, b+1):
            for l in range(a - n, a+1):
              percentDiff = (abs(inputArray[l][k][j] - localAv))/localAv*100.00        
              diffArray[l][k][j] += percentDiff
              timeUsedArray[l][k][j] += 1
        localAv = 0
    
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

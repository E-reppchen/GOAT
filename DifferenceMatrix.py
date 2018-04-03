from itertools import product

def differenceMatrix(dimensions, inputArray, n):
  x, y, z = dimensions
  n = n-1
  point = [n, n, n]
  diffArray = np.zeros(dimensions)
  timeUsedArray = np.zeros(dimensions)
  for i in range(point[2], z+1):
    for i in range(point[1], y+1):
      for i in range(point[0], x+1):
        for j in range(point[2] - n, point[2]+1): 
          for j in range(point[1] - n, point[1]+1):
            for j in range(point[0] - n, point[0]+1):
              localAv += inputArray[point[0]][point[1]][point[2]]
        localAv = localAv/(n*n*n)
        for j in range(point[2] - n, point[2]+1):
          for j in range(point[1] - n, point[1]+1):
            for j in range(point[0] - n, point[0]+1):
              percentDiff = (abs(inputArray[point[0]][point[1]][point[2]] - localAv))/localAv*100
              diffArray[point[0]][point[1]][point[2]] += percentDiff
              timeUsedArray[point[0]][point[1]][point[2]] += 1
        localAv = 0
    
  for i, j, k in product(xrange(x), xrange(y), xrange(z)):
    diffArray[i][j][k] = diffArray[i][j][k]/timeUsedArray[i][j][k]
  
  return diffArray

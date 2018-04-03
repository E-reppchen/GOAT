def differenceMatrix(dimensions, inputArray, n):
  x, y, z = dimensions
  n = n-1
  point = [n, n, n]
  point2 = [n, n, n]
  diffArray = np.zeros(dimensions)
  timeUsedArray = np.zeros(dimensions)
  for i in range(point[2], z+1):
    point2[1] = n
    for i in range(point[1], y+1):
      point2[0] = n
      for i in range(point[0], x+1):
        for j in range(point2[2] - n, point[2]+1): 
          for k in range(point2[1] - n, point[1]+1):
            for l in range(point2[0] - n, point[0]+1):
              localAv += inputArray[l][k][j]
        localAv = localAv/(n*n*n)
        for j in range(point2[2] - n, point2[2]+1):
          for k in range(point2[1] - n, point2[1]+1):
            for l in range(point2[0] - n, point2[0]+1):
              percentDiff = (abs(inputArray[l][k][j] - localAv))/localAv*100
              diffArray[l][k][j] += percentDiff
              timeUsedArray[l][k][j] += 1
        point2[0] += 1
        localAv = 0
      point2[1] += 1 
    point2[2] += 1
    
  for i in range(z):
    for j in range(y):
      for k in range(x):
        diffArray[i][j][k] = diffArray[i][j][k]/timeUsedArray[i][j][k]
  
  return diffArray

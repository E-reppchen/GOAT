def differenceMatrix(dimensions, inputArray):
  x, y, z = dimensions
  point = [2, 2, 2]
  diffArray = np.zeros(dimensions)
  for i in range(point[2], z+1):
    

class Board:

  def __init__(self):
    self.matrix = [["." for x in range(10)] for y in range(10)]
  
  def __str__(self):
    string = "  0 1 2 3 4 5 6 7 8 9\n"
    for i in range(0,10):
      string += rowLabel[i]
      string += " "
      for j in range(0,10):
        string += self.matrix[i][j]
        string += " "
      string += "\n"
    return string   
    
  def get(self, row, column):
    return self.matrix[row][column]

  def set(self, row, column, value):
    self.matrix[row][column] = value

  def placeShip(self, row, column, isHorz, shipType):
    error = False
    #Check out of bounds
    if isHorz:
      if column + shipType.size > 10:
        return True
    else:
      if row + shipType.size > 10:
        return True

    #Check for overlap  
    for i in range(shipType.size):
      if isHorz:
        if self.matrix[row][column+i] != '.':
          error = True
          break
      else:
        if self.matrix[row+i][column] != '.':
          error = True
          break

    #Add ships
    if not error:
      for i in range(shipType.size):    
        if isHorz:
          self.matrix[row][column+i] = shipType.char 
        else:
          self.matrix[row+i][column] = shipType.char
    return error

  def contains(self, char):
    intermediateList = [False for x in range(10)] 
    for x in range(10):
      intermediateList[x] = char in self.matrix[x]
    return True in intermediateList


import random

rowDict = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9}
rowLable = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

class Board:

  def __init__(self):
    self.matrix = [["." for x in range(10)] for y in range(10)]
  
  def __str__(self):
    string = "  0 1 2 3 4 5 6 7 8 9\n"
    for i in range(0,10):
      string += rowLable[i]
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

  def placeShip(self, row, column, isHorz, size):
    error = False
    #Check out of bounds
    if isHorz:
      if column + size > 10:
        return True
    else:
      if row + size > 10:
        return True

    #Check for overlap  
    for i in range(size):
      if isHorz:
        if self.matrix[row][column+i] == 'x':
          error = True
          break
      else:
        if self.matrix[row+i][column] == 'x':
          error = True
          break

    #Add ships
    if not error:
      for i in range(size):    
        if isHorz:
          self.matrix[row][column+i] = 'x' 
        else:
          self.matrix[row+i][column] = 'x' 
    return error


# SETUP GAME

playerShipBoard = Board()

def PlacementPrompt(name, size):
  PlacementError = True
  while PlacementError:
    print "Place your size", size, name
    PromptRow = int(rowDict[raw_input("  Uppermost row letter: ").upper()])
    PromptCol = int(input("  Leftmost column number: "))
    Orientation = bool(input("  Vertical (0) or Horizontal (1): "))
    PlacementError = playerShipBoard.placeShip(PromptRow, PromptCol, \
                                               Orientation, size)
    if PlacementError:
      print
      print "   ### PLACEMENT ERROR!  Try again. ###"
      print
    else:
      print
      print playerShipBoard
      print
      
PlacementPrompt("Aircraft Carrier", 5)
PlacementPrompt("Battleship", 4)
PlacementPrompt("Destroyer", 3)
PlacementPrompt("Submarine", 3)
PlacementPrompt("PT Boat", 2)


oppShipBoard=Board()

Horz = [True, False]

PlacementError = True
while PlacementError:
  PlacementError = oppShipBoard.placeShip(random.randint(0,9),\
                                      random.randint(0,9),\
                                      random.choice(Horz),5)

PlacementError = True
while PlacementError:
  PlacementError = oppShipBoard.placeShip(random.randint(0,9),\
                                      random.randint(0,9),\
                                      random.choice(Horz),4)

PlacementError = True
while PlacementError:
  PlacementError = oppShipBoard.placeShip(random.randint(0,9),\
                                      random.randint(0,9),\
                                      random.choice(Horz),3)

PlacementError = True
while PlacementError:
  PlacementError = oppShipBoard.placeShip(random.randint(0,9),\
                                      random.randint(0,9),\
                                      random.choice(Horz),3)

PlacementError = True
while PlacementError:
  PlacementError = oppShipBoard.placeShip(random.randint(0,9),\
                                      random.randint(0,9),\
                                      random.choice(Horz),2)


playerViewBoard = Board()
oppViewBoard = Board()


# PLAY GAME

print
print "   Starting game, fire at will!"
print

numberOfShots = 0
numberOfHits = 0

while numberOfHits < 17:
  print
  print playerViewBoard

  targetRow = int(rowDict[raw_input("Row target letter: ").upper()])
  targetCol = int(input("Column target number: "))

  if playerViewBoard.get(targetRow, targetCol) != '.':
    print "Coordinates", rowLable[targetRow], targetCol, "already targeted."
  elif oppShipBoard.get(targetRow, targetCol) == 'x':
    numberOfShots += 1
    numberOfHits += 1
    playerViewBoard.set(targetRow, targetCol, 'x')    
  else:
    numberOfShots += 1
    playerViewBoard.set(targetRow, targetCol, 'o')    

print
print playerViewBoard
print "You took", numberOfShots, "shots."


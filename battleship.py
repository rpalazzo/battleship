import random

rowDict = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9}
rowLable = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

class Ship:
  def __init__(self, shipType):
    self.name = shipType
    self.sunk = False
    if shipType == "Aircraft Carrier":
      self.size = 5
      self.char = 'a'
    elif shipType == "Battleship":
      self.size = 4
      self.char = 'b'
    elif shipType == "Destroyer":
      self.size = 3
      self.char = 'd'
    elif shipType == "Submarine":
      self.size = 3
      self.char = 's'
    elif shipType == "PT Boat":
      self.size = 2
      self.char = 'p'
    else:
      self.size = 0
      self.char = '.'

  def isSunk(self):
    return self.sunk

  def sink(self):
    self.sunk = True
    
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


# SETUP GAME

# Player placement

playerShipBoard = Board()
print playerShipBoard

def PlacementPrompt(ship):
  PlacementError = True
  while PlacementError:
    print "Place your size", ship.size, ship.name
    PromptRow = int(rowDict[raw_input("  Uppermost row letter: ").upper()])
    PromptCol = int(input("  Leftmost column number: "))
    Orientation = bool(input("  Vertical (0) or Horizontal (1): "))
    PlacementError = playerShipBoard.placeShip(PromptRow, PromptCol, \
                                               Orientation, ship)
    if PlacementError:
      print
      print "   ### PLACEMENT ERROR!  Try again. ###"
      print
    else:
      print
      print playerShipBoard
      print

playerAircraftCarrier = Ship("Aircraft Carrier")
playerBattleship = Ship("Battleship")
playerDestroyer = Ship("Destroyer")
playerSubmarine = Ship("Submarine")
playerPtBoat = Ship("PT Boat")

#PlacementPrompt(playerAircraftCarrier)
#PlacementPrompt(playerBattleship)
#PlacementPrompt(playerDestroyer)
#PlacementPrompt(playerSubmarine)
#PlacementPrompt(playerPtBoat)

# Computer placement

oppShipBoard = Board()

Horz = [True, False]

def oppPlacement(ship):
  PlacementError = True
  while PlacementError:
    PlacementError = oppShipBoard.placeShip(random.randint(0,9),\
                                        random.randint(0,9),\
                                        random.choice(Horz),ship)

oppAircraftCarrier = Ship("Aircraft Carrier")
oppBattleship = Ship("Battleship")
oppDestroyer = Ship("Destroyer")
oppSubmarine = Ship("Submarine")
oppPtBoat = Ship("PT Boat")

oppPlacement(oppAircraftCarrier)
oppPlacement(oppBattleship)
oppPlacement(oppDestroyer)
oppPlacement(oppSubmarine)
oppPlacement(oppPtBoat)

#print oppShipBoard


playerViewBoard = Board()
oppViewBoard = Board()


# PLAY GAME

print
print "   Starting game, fire at will!"
print

numberOfShots = 0
numberOfHits = 0

def printYouSankMy(ship):
    print ""
    print "**********************************"
    print "* You sank my", ship.name, "!"
    print "**********************************"
    print ""  

def announceSinking():
  if not(oppShipBoard.contains('a')) and not(oppAircraftCarrier.isSunk()):
    oppAircraftCarrier.sink()
    printYouSankMy(oppAircraftCarrier)
  if not(oppShipBoard.contains('b')) and not(oppBattleship.isSunk()):
    oppBattleship.sink()
    printYouSankMy(oppBattleship)
  if not(oppShipBoard.contains('d')) and not(oppDestroyer.isSunk()):
    oppDestroyer.sink()
    printYouSankMy(oppDestroyer)
  if not(oppShipBoard.contains('s')) and not(oppSubmarine.isSunk()):
    oppSubmarine.sink()
    printYouSankMy(oppSubmarine)
  if not(oppShipBoard.contains('p')) and not(oppPtBoat.isSunk()):
    oppPtBoat.sink()
    printYouSankMy(oppPtBoat)


while numberOfHits < 17:
  print
  print playerViewBoard

  targetRow = int(rowDict[raw_input("Row target letter: ").upper()])
  targetCol = int(input("Column target number: "))

  if playerViewBoard.get(targetRow, targetCol) != '.':
    print "Coordinates", rowLable[targetRow], targetCol, "already targeted."
  elif oppShipBoard.get(targetRow, targetCol) != '.':
    numberOfShots += 1
    numberOfHits += 1
    playerViewBoard.set(targetRow, targetCol, 'x')
    oppShipBoard.set(targetRow, targetCol, 'x')
    announceSinking()
  else:
    numberOfShots += 1
    playerViewBoard.set(targetRow, targetCol, 'o')    

print
print playerViewBoard
print "You took", numberOfShots, "shots."


import random
from ship import Ship
from board import Board
from ai import AI

rowDict = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9}
rowLabel = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']


# SETUP GAME

playerShipBoard = Board()
playerViewBoard = Board()
computerShipBoard = Board()
computerViewBoard = Board()

playerAircraftCarrier = Ship("Aircraft Carrier")
playerBattleship = Ship("Battleship")
playerDestroyer = Ship("Destroyer")
playerSubmarine = Ship("Submarine")
playerPtBoat = Ship("PT Boat")

computerAircraftCarrier = Ship("Aircraft Carrier")
computerBattleship = Ship("Battleship")
computerDestroyer = Ship("Destroyer")
computerSubmarine = Ship("Submarine")
computerPtBoat = Ship("PT Boat")


# Player placement

print(playerShipBoard)

def PlacementPrompt(ship):
  PlacementError = True
  while PlacementError:
    print("Place your size", ship.size, ship.name)
    PromptRow = int(rowDict[input("  Uppermost row letter: ").upper()])
    PromptCol = int(input("  Leftmost column number: "))
    Orientation = int(input("  Vertical (0) or Horizontal (1): "))
    if Orientation == 1:
      isHorz = True
    else:
      isHorz = False
    PlacementError = playerShipBoard.placeShip(PromptRow, PromptCol,
                                               isHorz, ship)
    if PlacementError:
      notify(" PLACEMENT ERROR!  Try again.")
    else:
      print(playerShipBoard)

PlacementPrompt(playerAircraftCarrier)
PlacementPrompt(playerBattleship)
PlacementPrompt(playerDestroyer)
PlacementPrompt(playerSubmarine)
PlacementPrompt(playerPtBoat)


# Computer placement


def computerPlacement(ship):
  Horz = [True, False]
  PlacementError = True
  while PlacementError:
    PlacementError = computerShipBoard.placeShip(random.randint(0,9),
                                                 random.randint(0,9),
                                                 random.choice(Horz),ship)

computerPlacement(computerAircraftCarrier)
computerPlacement(computerBattleship)
computerPlacement(computerDestroyer)
computerPlacement(computerSubmarine)
computerPlacement(computerPtBoat)

#print computerShipBoard #used for debugging



# PLAY GAME

print("\n   Starting game, fire at will!\n")

numberOfShots = 0
numberOfHits = 0

def notify(msg):
    print("\n**********************************")
    print("* ", msg, "!")
    print("**********************************\n")

def announceSinking():
  if not(computerShipBoard.contains('a')) and not(computerAircraftCarrier.isSunk()):
    computerAircraftCarrier.sink()
    notify(computerAircraftCarrier)
  if not(computerShipBoard.contains('b')) and not(computerBattleship.isSunk()):
    computerBattleship.sink()
    notify(computerBattleship)
  if not(computerShipBoard.contains('d')) and not(computerDestroyer.isSunk()):
    computerDestroyer.sink()
    notify(computerDestroyer)
  if not(computerShipBoard.contains('s')) and not(computerSubmarine.isSunk()):
    computerSubmarine.sink()
    notify(computerSubmarine)
  if not(computerShipBoard.contains('p')) and not(computerPtBoat.isSunk()):
    computerPtBoat.sink()
    notify(computerPtBoat)


def computerTurn():

  shot = 'x'
  while shot == 'x' or shot == 'o':  #Previously targeted
    randRow = random.randint(0,9)
    randCol = random.randint(0,9)
    shot = playerShipBoard.get(randRow, randCol)
    if shot == '.':
      result = "miss"
    else:
      result = "HIT"

  print("Computer shot at", rowLabel[randRow], randCol, ": ", result)
  if shot == '.':
    playerShipBoard.set(randRow, randCol, 'o')
  else:
    playerShipBoard.set(randRow, randCol, 'x')

     

while numberOfHits < 17:
  print()
  print(playerViewBoard)
  print(playerShipBoard)

  targetRow = int(rowDict[input("Row target letter: ").upper()])
  targetCol = int(input("Column target number: "))

  if playerViewBoard.get(targetRow, targetCol) != '.':
    print("Coordinates", rowLabel[targetRow], targetCol, "already targeted.")
  elif computerShipBoard.get(targetRow, targetCol) != '.':
    numberOfShots += 1
    numberOfHits += 1
    playerViewBoard.set(targetRow, targetCol, 'x')
    computerShipBoard.set(targetRow, targetCol, 'x')
    announceSinking()
  else:
    numberOfShots += 1
    playerViewBoard.set(targetRow, targetCol, 'o')

  computerTurn()

print()
print(playerViewBoard)
print("You took", numberOfShots, "shots.")


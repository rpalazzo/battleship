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

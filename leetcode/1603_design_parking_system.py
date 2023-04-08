# This is the initialization method of the ParkingSystem object.
# It takes in the number of available parking spots for large, medium and small cars and initializes them.
def __init__(self, big: int, medium: int, small: int):
    self.vehicle  =[big,medium,small]

# This method takes in a carType (1, 2 or 3) and returns True if there is an available spot for the carType.
# It returns False otherwise.
def addCar(self, carType: int) -> bool:
    if carType == 1 :
        if self.vehicle[0] > 0:
            self.vehicle[0]-=1
            return True
    elif carType == 2:
        if self.vehicle[1] > 0:
            self.vehicle[1]-=1
            return True
    elif carType == 3:
        if self.vehicle[2] > 0:
            self.vehicle[2]-=1
            return True
    return False

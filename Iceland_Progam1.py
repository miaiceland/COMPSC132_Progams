'''
Program 1
Mia Iceland
July 4, 2023
'''

class Car:

  def __init__(self, year, model, make, doors):
    self.__year = year
    self.__model = model
    self.__make = make
    self.__doors = doors
    self.__speed = 0


# Accessors for year, model, make, and doors
  def getYear(self):
    return self.__year

  def getModel(self):
    return self.__model

  def getMake(self):
    return self.__make

  def getDoors(self):
    return self.__doors

# 'getSpeed' returns the current speed
  def getSpeed(self):
    return self.__speed

# Mutators for year, model, make, and doors
  def mutateYear(self, year):
    self.__year = year

  def mutateModel(self, model):
    self.__model = model

  def mutateMake(self, make):
    self.__make = make

  def mutateDoors(self, doors):
    self.__doors = doors

# Acceleration
  def accelerate(self):
    self.__speed += 5

# Brake
  def brake(self):
    if self.__speed >= 5: # ensures I don't get a negative speed
      self.__speed -= 5
    else:
      self.__speed = 0

def main():

# My 'Car' object set up
    car_example = Car(2023, 'Wrangler', 'Jeep', 2)
    print(car_example.getYear())
    print(car_example.getModel())
    print(car_example.getMake())
    print(car_example.getDoors())

# Using the 'Acceleration' method and tracking speed
    for i in range(5):
      car_example.accelerate()
      print(f'Accelerating the speed to: {car_example.getSpeed()}')

# Using the 'Brake' method and tracking speed
    for i in range(5):
      car_example.brake()
      print(f'Braking the speed to: {car_example.getSpeed()}')

# Using the Mutator method
    car_example.mutateYear(2002)
    car_example.mutateModel("Malibu")
    car_example.mutateMake("Chevy")
    car_example.mutateDoors(2)

# Using the Accessor method
    print(car_example.getYear())
    print(car_example.getModel())
    print(car_example.getMake())
    print(car_example.getDoors())

main()

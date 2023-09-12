'''
Program 2
Mia Iceland
July 4, 2023
'''


class Employee:

  def __init__(self, name, number, email):
    self.__name = name
    self.__number = number
    self.__email = email

# Accessors
  def getName(self):
    return self.__name

  def getNumber(self):
    return self.__number

  def getEmail(self):
    return self.__email

# Mutators
  def mutateName(self, name):
    self.__name = name

  def mutateNumber(self, number):
    self.__number = number

  def mutateEmail(self, email):
    self.__email = email


class ProductionWorker(Employee): # putting' Employee' in the parentheses makes 'ProductionWorker' a subclass

  def __init__(self, name, number, email, shift_num, hourlyPayRate):
    super().__init__(name, number, email) # this line applies 'Employee' attributes to the 'ProductionWorker' class
    self.__shift_num = shift_num
    self.__hourlyPayRate = hourlyPayRate

#Accessors
  def get_shift_num(self):
    return self.__shift_num

  def get_hourlyPayRate(self):
    return self.__hourlyPayRate

#Mutators
  def mutate_shift_num(self, shift_num):
    self.__shift_num = shift_num

  def mutate_hourlyPayRate(self, hourlyPayRate):
    self.__hourlyPayRate = hourlyPayRate


def main():

# 'input' allows the user to enter their own information
  name = input("Name: ")
  number = input("Employee Number: ")
  email = input("Email: ")
  shift_num = input("Shift Time (enter 1 for day shift, enter 2 for night shift): ")
  hourlyPayRate = input("Hourly Pay Rate: ")

# Stores the user's information into the object 'productionworker'
  productionworker = ProductionWorker(name, number, email, shift_num, hourlyPayRate)

# Prints the user's 'input' information
  print(f'Name: {productionworker.getName()}')
  print(f'Employee Number: {productionworker.getNumber()}')
  print(f'Email: {productionworker.getEmail()}')
  print(f'Shift Number: {productionworker.get_shift_num()}')
  print(f'Hourly Pay: {productionworker.get_hourlyPayRate()}')
  

main()

'''
Program 3
Mia Iceland
July 11, 2023
'''

class PersonData:

  def __init__(self, lastName, firstName, address, city, state, zip, phone):
    self.__lastName = lastName
    self.__firstName = firstName
    self.__address = address
    self.__city = city
    self.__state = state
    self.__zip = zip
    self.__phone = phone

  # Accessors
  def getlastName(self):
    return self.__lastName

  def getfirstName(self):
    return self.__firstName

  def getaddress(self):
    return self.__address

  def getcity(self):
    return self.__city

  def getstate(self):
    return self.__state

  def getzip(self):
    return self.__zip
  
  def getphone(self):
    return self.__phone


  # Mutators
  def mutatelastName(self, lastName):
    self.__lastName = lastName

  def mutatefirstName(self, firstName):
    self.__firstName = firstName

  def mutateaddress(self, address):
    self.__address = address

  def mutatecity(self, city):
    self.__city = city

  def mutatestate(self, state):
    self.__state = state

  def mutatezip(self, zip):
    self.__zip = int(zip)

  def mutatephone(self, phone):
    self.__phone = int(phone)

  
class CustomerData(PersonData):

  def __init__(self, lastName, firstName, address, city, state, zip, phone, customerNumber, mailingList):
    super().__init__(lastName, firstName, address, city, state, zip, phone)
    self.__customerNumber = customerNumber
    self.__mailingList = True #sets 'True' as the defult response

  # Accessors
  def getcustomerNumber(self):
    return int(self.__customerNumber)

  def getmailingList(self):
    return self.__mailingList

  # Mutators
  def mutatecustomerNumber(self, customerNumber):
    self.__customerNumber = int(customerNumber)

  def mutatemailingList(self, mailingList):
    self.__mailingList = mailingList

  def main():

  try:
    customer = CustomerData("Thompson", "Sarah", "1234 Pickle Rd", "Springfield", "IL", 54321, 1234567890, 5, True)
  
    print(customer.getlastName())
    print(customer.getfirstName())
    print(customer.getaddress())
    print(customer.getcity())
    print(customer.getstate())
    print(customer.getzip())
    print(customer.getphone())
    print(customer.getcustomerNumber())
    print(customer.getcity())

  # Finds any type of error, stores the error in the variable 'a'
  except Exception as a:
    print(f'There is an Error: {a}')

main()

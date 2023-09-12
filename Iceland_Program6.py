'''
Program 6
Mia Iceland
July 18, 2023
'''

class Inventory:
  
  def __init__(self, serialNum, manufactDate, lotNum):
    self.__serialNum = int(serialNum)
    self.__manufactDate = manufactDate
    self.__lotNum = int(lotNum)

  # Accessors
  def get_serialNum(self):
    return self.__serialNum

  def get_manufactDate(self):
    return self.__manufactDate

  def get_lotNum(self):
    return self.__lotNum

  # Mutators
  def mutateserialNum(self, serialNum):
    self.__serialNum = serialNum

  def mutatemanufactDate(self, manufactDate):
    self.__manufactDate = manufactDate  

  def mutatelotNum(self, lotNum):
    self.__lotNum = lotNum


class LLNode:

  def __init__(self, data):
    self.data = data
    self.next = None
    self.previous = None

  def __repr__(self):
    return "{}".format(self.data)

  def get_data(self):
    return self.data

  def set_data(self, new_data):
    self.data = new_data

  def get_next(self):
    return self.next

  def set_next(self, new_next):
    self.next = new_next


class Stack:

  def __init__(self):
    self.top = None

  def __repr__(self):
    return "{}".format(self.top)

  def is_empty(self):
    return self.top is None

  def push(self, new_data):
    # Switches the new data and the old 'self.top' data using a temporary variable
    temp = LLNode(new_data)
    temp.set_next(self.top)
    self.top = temp

  def pop(self):
    if self.top is None:
      return "Stack is empty. No Nodes to remove."
    # Switches the old top of the stack to the next node in the stack
    current = self.top
    self.top = self.top.next
    return current

def main():

  stack = Stack()
  
  # 'while True' means that the loop will run forever or until the code breaks
  # As long as there are no errors, the ability to edit to inventory can occur indefinitely
  # A user can exit this loop by clicking '3'
  while True: 
    print("Click '1' Add to Inventory")
    print("Click '2' Remove from Inventory")
    print("Click '3' to Exit the Program")
    user_input = int(input("Enter: "))
    
    if user_input == 1:
      # User creates an object
      serial_num = int(input("Serial Number: "))
      manufact_date = input("Manufacture Date: ")
      lot_num = int(input("Lot Number: "))
      
      # Putting the new object into a variable
      inventory_object = Inventory(serial_num, manufact_date, lot_num)
      # Adding object to the stack
      stack.push(inventory_object)


    elif user_input == 2:
      if stack.is_empty():
        print("Inventory is empty.")
      else:
        popped_inventory = stack.pop()
        print("Removed Successfully.")


    elif user_input == 3: 
      current = stack.top # 'current2' is stack based data
      inventory_num = 1 # Allows me to differentiate the objects when printed
      while current != None: # Sees if there are anymore objects in the stack
        current2 = current.data # 'current2' is node based data
        print("Inventory", inventory_num)
        print(f"{current2.get_serialNum()}")
        print(f"{current2.get_manufactDate()}")
        print(f"{current2.get_lotNum()}")
        inventory_num += 1
        current = current.next # the next node becomes the current node
      break

    # If the user input is not valid
    elif user_input != 1 or user_input != 2 or user_input != 3:
        print("Error. Please Try Again.")

main()

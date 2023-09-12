'''
Program 7
Mia Iceland
July 25, 2023
'''

class Inventory:

  def __init__(self, UPC_num, price, cost, quantity):
    self.UPC_num = UPC_num
    self.price = price
    self.cost = cost
    self.quantity = quantity

class ManageInventory:

  def __init__(self):
    self.inventory_dic = {}

  def add_inventory(self, item):
    self.inventory_dic[item.UPC_num] = item

  def delete_inventory(self, UPC_num):
    del self.inventory_dic[UPC_num]

  def modify_item(self, UPC_num, price, cost, quantity):
        # Similar to a Mutator method but you use the key to pull up the value
        self.inventory_dic[UPC_num].price = price
        self.inventory_dic[UPC_num].cost = cost
        self.inventory_dic[UPC_num].quantity = quantity

  def display_inventory(self):
    # Alots spaces between each phrase
    print("{:<15} {:<10} {:<10} {:<10}".format('UPC Number', 'Price', 'Cost', 'Quantity'))
    # Prints each value in the dictionary
    for inventory in self.inventory_dic.values():
      print("{:<15} {:<10} {:<10} {:<10}".format(inventory.UPC_num, inventory.price, inventory.cost, inventory.quantity))

  # Determines if the UPC number entered is in the inventory dictionary
  def upc_in_dic(self, UPC_num):
    return UPC_num in self.inventory_dic

# Ensures each UPC number is 6-digit integer
def upc_error_detection(entry):
  value = int(input(entry)) # integer inputted by the user
  if 100000 <= value <= 999999: # makes sure the value entry is 6 digits
       return value
  else:
    print("Error. Please Enter a 6-Digit Integer.")

# Ensures each value entered is a float number
def float_error_detection(entry):
  while True:
    try:
      value = float(input(entry))
      return value
    except ValueError:
      print("Error. Please Enter a Number.")

# Ensures each value entered is an integer
def int_error_detection(entry):
  while True:
    try:
      value = int(input(entry))
      return value
    except ValueError:
      print("Error. Please Enter an Integer.")

def main():

  manage_inventory = ManageInventory()

  user_access = True

  while user_access:
    print("Click '1' to Add an Item to Inventory")
    print("Click '2' to Remove an Item from Inventory")
    print("Click '3' to Modify an Item from Inventory")
    print("Click '4' to Display Inventory")
    print("Click '5' to Exit the Program")
    user_input = int_error_detection("Enter: ")


    if user_input == 1:
      UPC_num = upc_error_detection("UPC Number: ")
      price = float_error_detection("Price: ")
      cost = float_error_detection("Cost: ")
      quantity = int_error_detection("Quantity: ")

      # Puts entered information into an object and adds object to the dictionary
      inventory_object = Inventory(UPC_num, price, cost, quantity)
      manage_inventory.add_inventory(inventory_object)
      print("Added.")


    elif user_input == 2:

      # Removes object from the dictonary using the UPC number
      user_UPC = upc_error_detection("Enter UPC Number: ")
      
      if not manage_inventory.upc_in_dic(user_UPC):
        print("Invalid UPC Number.")
      else:
        manage_inventory.delete_inventory(user_UPC)
        print("Removed Successfully.")


    elif user_input == 3:
      
      # Edits an existing object in the dictonary
      user_UPC = upc_error_detection("Enter UPC Number: ")

      if not manage_inventory.upc_in_dic(user_UPC):
        print("Invalid UPC Number.")
      else:
        price = float_error_detection("Enter New Price: ")
        cost = float_error_detection("Enter New Cost: ")
        quantity = int_error_detection("Enter New Quantity: ")
        manage_inventory.modify_item(user_UPC, price, cost, quantity)
        print("Modified Successfully.")



    elif user_input == 4:
      manage_inventory.display_inventory()


    elif user_input == 5:
      print("Exited.")
      user_access = False


    else:
      print("Error. Please Try Again.")


main()

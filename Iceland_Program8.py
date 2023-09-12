'''
Program 8
Mia Iceland
July 25, 2023
'''

class EmployeeInfo:

  def __init__(self, id_num, name):
    self.id_num = id_num
    self.name = name

''' This class sets up the tree branch structure
    by creating a parent node with its right and left child nodes '''
class Node:

  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value


class BinaryTree:

  def __init__(self):
    self.root = None

  def insert(self, value):
    if self.root is None: # determines if a root node has been established yet
      self.root = Node(value)
    else:
      self.recursive_insert(self.root, value) # calls the recursive insert method

  def recursive_insert(self, node, value):

    if value.id_num < node.value.id_num: # smaller values than the root node go to the left 
      if node.left is None: # determines if the user is at a left leaf node
        node.left = Node(value) # If so, then it is added to the tree
      else:
        self.recursive_insert(node.left, value)
    else:
      if node.right is None: # determines if the user is at a right leaf node
        node.right = Node(value)
      else:
        self.recursive_insert(node.right, value)
  
  def search(self, id_num):
    if self.root is None:
      return None # Can't search the tree if there are no nodes in the tree
    else:
      return self.recursive_search(self.root, id_num)

  def recursive_search(self, node, id_num):
    if node.value.id_num == id_num: # If the value entered by the user is equal to a value already in the tree
      return node
    elif id_num < node.value.id_num: # If the value entered is less than the node in the tree
      return self.recursive_search(node.left, id_num) # calls the first if statement in the method
    elif id_num > node.value.id_num:  # If the value entered is greater than the node in the tree
      return self.recursive_search(node.right, id_num) # calls the first if statement in the method


def main():


  binarytree = BinaryTree()

  binarytree.insert(EmployeeInfo(2932, "Catelyn Stark"))
  binarytree.insert(EmployeeInfo(1034, "Cersei Lannister"))
  binarytree.insert(EmployeeInfo(3493, "Daenerys Targaryen"))
  binarytree.insert(EmployeeInfo(2293, "Jon Snow"))
  binarytree.insert(EmployeeInfo(2497, "Sansa Stark"))
  binarytree.insert(EmployeeInfo(5483, "Arya Stark"))
  binarytree.insert(EmployeeInfo(3994, "Tywin Lannister"))
  
  # This allows the user to re-enter a value if they incorrectly enter it the first time
  user_access = True

  while user_access:
    
    try:

      employee_object = int(input("Enter Employee ID Number: "))
      user_input = binarytree.search(employee_object) # Searches for the value the user entered
    
      if user_input:
       print("Employee Name is: {}".format(user_input.value.name))
       user_access = False # Ends the loop once the user input is valid

    except Exception:
      print("Error. Invalid Input. Try Again.")

main()

'''
Program 5
Mia Iceland
July 18, 2023
'''

class SLLNode:

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


class SLL:

  def __init__(self):
    self.head = None

  def __repr__(self):
    return "{}".format(self.head)

  def is_empty(self):
    return self.head is None

  def add_front(self, new_data):
    # Switches the new data and the old 'self.head' data using a temporary variable
    temp = SLLNode(new_data)
    temp.set_next(self.head)
    self.head = temp


  def search(self, data):
    if self.head is None:
      return "Linked List is empty. No Nodes to search."

    current = self.head
    while current is not None:
      # Node's data matches what we're looking for
      if current.get_data() == data:
        return True
      else: # If the data doesn't match what we're looking for
        current = current.get_next()

      return False


  def remove(self, data):
    if self.head is None:
      return "Linked List is empty. No Nodes to remove."

    current = self.head
    previous = None
    found = False

    while not found:
      if current.get_data() == data:
        found = True
      else:
        if current.get_next() == None:
          return "A Node with that data value is not present."
        else:
          previous = current
          current = current.get_next()

    if previous is None:
      self.head = current.get_next()
    else:
      previous.set_next(current.get_next())


def main():
  
  # This connects the work done in 'def main():' to the SSL code created above
  sll = SLL()

  grade_list = []
  print("Please Enter 10 Grades: ")

  # Allows user to input 10 grades, adds those grades to a list
  for i in range(10):
    grade_input = int(input("Assignment Grade: "))
    grade_list.append(grade_input)
    sll.add_front(grade_input)
  
  # Prints each value in the list
  print("Grades Entered: ")
  sll_head = sll.head 
  while sll_head: # Interates through the list until it reaches "None" (there is no head of the list)
      print(sll_head.get_data())
      sll_head = sll_head.get_next() # the new head of the list is the next value in the list
  
  # I'm dividing by 10 because the program specifically asks the user to put in 10 grades
  print("Grade Average: ")
  return sum(grade_list) / 10 

main()

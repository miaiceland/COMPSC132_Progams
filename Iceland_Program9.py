'''
Program 9
Mia Iceland
August 1, 2023
'''

import matplotlib.pyplot as plt
from datetime import datetime

class Sales:
  
  # Creating the date/sales dictionary
  def __init__(self):
    self.ticket_sales = {}

  # Mutating
  def add_ticket_sale(self, date, sales):
    self.ticket_sales[date] = sales

  # Removing
  def remove_ticket_sale(self, date):
    if date in self.ticket_sales:
      del self.ticket_sales[date]
    else:
      print("Error. Invalid Date.")

  # Returns the dictionary
  def display_ticket_sale(self):
    return self.ticket_sales

  # Displays a key's value (the sales for a specific date)
  def get_ticket_sales(self, date):
    if date in self.ticket_sales:
      return self.ticket_sales[date]
    else:
      print("Error. Data Does Not Exist.")

# Ensures the date is corretcly entered
def date_error_detection(entry):
  user_input_access = True

  while user_input_access:
    try:
      # Using the package "Datetime" I can ensure that the date is in the correct format
      date = datetime.strptime(entry, "%m/%d/%Y")
      return date.strptime(entry, "%m/%d/%Y")
      user_input_access = False
    except Exception:
      print("Error. Please Enter a Valid Date with the Format: 'mm/dd/yyyy'.")
      # If there is an error, this allows the user to re-enter a date
      entry = input("Enter Date in 'mm/dd/yyyy': ")

# Ensures each value entered is an integer
def int_error_detection(entry):
  
  user_input_access = True
  
  while user_input_access:
    try:
      user_input = int(entry)
      return user_input
      user_input_access = False
    except Exception:
      print("Error. Please Enter an Integer.")


# plotting the data
def plot_ticket_sales(dates, sales):

  # I have set up the x and y axis and their respective labels
  plt.xlabel("Date")
  plt.ylabel("Ticket Sales")
  plt.title("Date v. Ticket Sales")
  plt.plot(dates, sales, marker = 'o', linestyle = 'solid') # This creates a line graph
  plt.xticks(rotation=90) # Makes the labels sideways so that they do not overlap
  plt.show()


def main():

  sales = Sales()

  user_input = True

  while user_input:
    
    print("Menu")
    print("Click '1' to Add Ticket Sales for a Date")
    print("Click '2' to Remove Ticket Sales for a Date")
    print("Click '3' to View Ticket Sales for a Date")
    print("Click '4' to Plot Ticket Sales")
    print("Click '5' to Exit the Program")

    user_choice = input("Enter: ")

    # Allows user to add a date and ticket sales to the dictionary by creating an object
    if user_choice == "1":
      
      # user enters information and date_error_detection checks for errors
      user_input_check = input("Enter Date in 'mm/dd/yyyy': ")
      date = date_error_detection(user_input_check)
      
      # user enters information and int_error_detection checks for errors
      user_input_ticket_count = input("Number of Tickets Sold: ")
      tickets_sales = int_error_detection(user_input_ticket_count)
      
      sales.add_ticket_sale(date, tickets_sales)
      print("Successfully Added.")

    # Allows user to remove a date and ticket sales to the dictionary by creating an object
    elif user_choice == "2":
      
      user_input_check = input("Enter Date in 'mm/dd/yyyy': ")
      date = date_error_detection(user_input_check)

      sales.remove_ticket_sale(date)
      print("Successfully Deleted.")

    elif user_choice == "3":

      user_input_check = input("Enter Date in 'mm/dd/yyyy': ")
      date1 = date_error_detection(user_input_check)
      
      # gets the sale value for a specific date entered by the user
      tickets_sales = sales.get_ticket_sales(date1)
      print(f"Number of Ticket Sales: {tickets_sales}")

    elif user_choice == "4":
      # puts ticket sales dictionary into an object
      ticket_sales = sales.display_ticket_sale()
      if not ticket_sales:
        print("There are No Ticket Sales.")
      else:
        # puts keys and values into seperate lists
        date = list(ticket_sales.keys())
        sales = list(ticket_sales.values())
        # uses the lists as the x and y axis
        plot_ticket_sales(date, sales)

    elif user_choice == "5":
      print("Exited.")
      user_input = False

    else:
      print("Error. Please Try Again.")

main()

'''
Program 10
Mia Iceland
August 8, 2023
'''
import time
import random

# Random integer generators that pulls integers between 0 and 1000 
def random_list_generator(list_length):
  lst = []
  for i in range(list_length):
    lst.append(random.randint(0,1000))
  return lst


def selectionSort(lst):
  for i in range(len(lst) - 1):
      # Finds index of smallest remaining number in the list
      index1 = i
      for j in range(i + 1, len(lst)):
          if lst[j] < lst[index1]:
              index1 = j

      # Swaps 'i' and 'index1'
      temp = lst[i]
      lst[i] = lst[index1]
      lst[index1] = temp


def bubbleSort(lst):
  for i in range(len(lst)-1, 0, -1):
    for j in range(i):
      
      # Swaps 'lst[j]' and 'lst[j+1]'
      if lst[j] > lst[j+1]:
        temp = lst[j]
        lst[j] = lst[j+1]
        lst[j+1] = temp


def main():

  # Setting the length of the list to 1000
  list1 = random_list_generator(1000)
  list2 = list1.copy()

  # records the time before the fuction and after the function is run
  timestamp = lambda function, argument: (time.time(), function(argument), time.time())
  # subtracts the time after the function is run from the time before it ran
  difference = lambda t0, retrival, t1: t1 - t0
  ''' 'timer' calls the previous two lambda functions
  so that both can be used while only inputting one function and argument'''
  timer = lambda function, argument: difference(*timestamp(function, argument))


  time_selectionSort = timer(selectionSort, list1)
  print(f'Selection Sort Time: {time_selectionSort:.5f} s')

  time_bubbleSort = timer(bubbleSort, list2)
  print(f'Bubble Sort Time: {time_bubbleSort:.5f} s')

main()

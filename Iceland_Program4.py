'''
Program 4
Mia Iceland
July 11, 2023
'''

class Assignment:

  def __init__(self, name, grades):
    self.name = name
    self.grades = grades

  # Accessors
  def getname(self):
    return self.__name

  def getgrades(self):
    return self.__grades

  # Mutators
  def mutatename(self, name):
    self.__name = name

  def mutatefirstName(self, grades):
    self.__grades = grades

  # Prints the list of grades
  def printgrades(self):
    lst = []
    for i in self.grades:
      lst.append(i)
    print(lst)

  def selectionSort(self):
    for i in range(len(self.grades) - 1):
        # Finds index of smallest remaining number in the list
        index1 = i
        for j in range(i + 1, len(self.grades)):
            if self.grades[j] < self.grades[index1]:
                index1 = j
    
        # Swaps 'i' and 'index1'
        temp = self.grades[i]
        self.grades[i] = self.grades[index1]
        self.grades[index1] = temp

def main():

  # Sets up name and grade list, stores them in the object 'examGradeList'
  assignmentName = "Math Exam"
  gradeList = [85.6, 100, 56.3, 23, 87, 23, 45, 94, 83.2, 73.4]
  examGradeList= Assignment(assignmentName, gradeList)

  print("Before Sorting: ")
  examGradeList.printgrades()

  examGradeList.selectionSort()

  print("After Sorting: ")
  examGradeList.printgrades()

main()

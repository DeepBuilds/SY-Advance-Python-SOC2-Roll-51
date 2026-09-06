'''1. Student Management System Develop a Python application to manage student details using Object-Oriented Programming. Requirements Create a Student class with the following data members: Roll Number Name Marks Assign Grade based on marks: A (Marks ≥ 90) B (Marks ≥ 75) C (Marks ≥ 60) F (Marks < 60) Create a College class. Add student objects to the college. Display all student details.'''
def decorator(func):
    def wrapper(*args,**kwargs):
        print("="*40)
        print("MIT ADT")
        print("="*40)
        func(*args,**kwargs)
        print("="*40)
    return wrapper

class Student:
  def __init__(self,name,roll,marks):
    self.name=name
    self.roll=roll
    self.marks=marks
  def grade(self):
    if self.marks >=90:
      return "A"
    elif self.marks>=80:
      return "B"
    elif self.marks>=70:
      return "C"
    elif self.marks>=60:
      return "D"
    else:
      return "F"
  @decorator
  def display(self):
    print("Name:",self.name)
    print("Roll:",self.roll)
    print("Marks:",self.marks)
    print("Grade:",self.grade())
    print()
class college:
  def __init__(self):
    self.students=[]
  def add_student(self,student):
    self.students.append(student)
  def display_students(self):
    for student in self.students:
      student.display()
col=college()

s1=Student("Shriram",51,99)
s2=Student("ram",51,19)
s3=Student("Dev",51,79)
col.add_student(s1)
col.add_student(s2)
col.add_student(s3)
col.display_students()
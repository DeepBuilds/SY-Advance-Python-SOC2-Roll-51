#Demonstration of Encapsulation

class Employee:
    def __init__(self):
        self.name = "Shriram"      # Public member
        self._department = "CSE"   # Protected member
        self.__salary = 5000000000      # Private member

    # Public method to access private member
    def display(self):
        print("Name:", self.name)
        print("Department:", self._department)
        print("Salary:", self.__salary)


# Create object
emp = Employee()

# Accessing public member
print("Public Member:", emp.name)

# Accessing protected member
print("Protected Member:", emp._department)

# Accessing private member (Not Allowed)
# print(emp.__salary)   # AttributeError
# Accessing private member through public method
emp.display()
'''
Output:
PS C:\Users\Shriram\Desktop\SY-Advance-Python> & C:\Users\Shriram\AppData\Local\Microsoft\WindowsApps\python3.13.exe "c:/Users/Shriram/Desktop/SY-Advance-Python/Basic  OOP programs/Demonstration of Encapsulation.py"
Public Member: Shriram
Protected Member: CSE
Name: Shriram
Department: CSE
Salary: 5000000000
'''
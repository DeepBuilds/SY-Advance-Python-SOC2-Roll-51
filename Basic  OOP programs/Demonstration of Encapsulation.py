#Demonstration of Encapsulation

class Employee:
    def __init__(self):
        self.name = "Shriram"      # Public member
        self._department = "CSE"   # Protected member
        self.__salary = 50000      # Private member

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
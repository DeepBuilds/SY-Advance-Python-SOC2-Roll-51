#Class and object demonstration
class car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"
    
car1=car("German", "BMW", 2020)
print(car1.display_info())
'''
Output:
PS C:\Users\Shriram\Desktop\SY-Advance-Python> & C:\Users\Shriram\AppData\Local\Microsoft\WindowsApps\python3.13.exe "c:/Users/Shriram/Desktop/SY-Advance-Python/Basic  OOP programs/Class and object demonstration.py"
2020 German BMW
'''
#Polymorphism demonstration

class Animal:
    def sound(self):
        return "Some animal sound"


class Dog(Animal):
    def sound(self):
        return "Bark"


class Cat(Animal):
    def sound(self):
        return "Meow"


def show_sound(animal):
    print(animal.sound())


dog = Dog()
cat = Cat()

show_sound(dog)
show_sound(cat)
'''
Output:
PS C:\Users\Shriram\Desktop\SY-Advance-Python> & C:\Users\Shriram\AppData\Local\Microsoft\WindowsApps\python3.13.exe "c:/Users/Shriram/Desktop/SY-Advance-Python/Basic  OOP programs/Polymorphism demonstration.py"
Bark
Meow
'''
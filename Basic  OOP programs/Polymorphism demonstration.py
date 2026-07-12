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

# Base class
class Animal:
    def fur(self):
        print("I have fur all over my body")

# Dog class inheriting from Animal
class Dog(Animal):
    def bark(self):
        print("Dog barking")

# Puppy class inheriting from Dog
class Puppy(Dog):
    def play(self):
        print("I play all the time")

# Creating an instance of Puppy
bosco = Puppy()

# Calling the methods
bosco.play()
bosco.bark()
bosco.fur()

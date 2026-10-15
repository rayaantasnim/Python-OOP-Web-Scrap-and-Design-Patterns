from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod

    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Dog: Gheu Gheu")

dog = Dog()
dog.make_sound()

class Cat(Animal):
    def make_sound(self):
        print("Cat: Meouw Meouw")

cat = Cat()
cat.make_sound()
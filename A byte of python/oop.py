from abc import ABCMeta, abstractmethod


# Abstract class
class Champion(metaclass=ABCMeta):
    @abstractmethod
    def info(self):
        return "There can be only one Champion"

# person = Champion() # Error abstract class

# Class with class & static methods and private attributes
class Hero():
    __priority = "HIGH"  # private attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return self.name + " " + str(self.age) + " years old"

    # Static method
    @staticmethod
    def destroyAll():
        print("All heroes have been destroyed")

    # Class method
    @classmethod
    def getPriority(cls):
        return cls.__priority

Hero.destroyAll()
print(Hero.getPriority())

archer = Hero('Strong Archer', 24)
print(archer.name)
print(archer.info())


# Class inheritance & hierarchy
class Parent():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def info(self):
        return self.name + " " + self.surname

class Child(Parent):
    def __init__(self, name, surname, age):
        super().__init__(name, surname)
        self.age = age

    def info(self):
        return self.name + " " + self.surname + " " + str(self.age)

father = Parent('Garry', 'Simpson')
print(father.info())

son = Child('John', 'Simpson', 7)
print(son.info())
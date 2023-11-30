from abc import ABCMeta, abstractmethod


class User(metaclass=ABCMeta):
    __priority = "HIGH"  # private attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def info(self):
        print(self.name, "age:", self.age)
    # abstractmethod(info)

    @staticmethod
    def hello():
        print('hellow there')

class Teacher(User):

    def __init__(self, name, age, salary):
        User.__init__(self, name, age)
        self.salary = salary

    def info(self):
        print(self.name, "salary:", self.salary)

class Student(User):
    def __init__(self, name, age, marks):
        User.__init__(self, name, age)
        self.marks = marks

    def info(self):
        print(self.name, "marks:", self.marks)

teachik = Teacher("Toshpalov Pulatov", 99, "800$")
teachik.info()

studik = Student("Bobur Nuridinov", 27, "ALL 5")
studik.info()

User.hello()

# print(teachik.priority)  # Error private attribute
# usik = User("Bobur Nuridinov", 27)  # Error abstract class

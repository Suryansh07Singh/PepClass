'''from abc import ABC, abstractmethod

# ============================================
# 1. CLASSES AND OBJECTS
# ============================================

class Car:
    """A simple class to represent a car"""
    def __init__(self, brand, model):   
        self.brand = brand
        self.model = model
    
    def display_info(self):
        print(f"Car: {self.brand} {self.model}")

# Creating objects (instances)
car1 = Car("Toyota", "Camry")
car1.display_info()


# ============================================
# 2. ENCAPSULATION (Data Hiding)
# ============================================

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute (__)
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def get_balance(self):
        return self.__balance

account = BankAccount("John", 1000)
account.deposit(500)
print(f"Balance: {account.get_balance()}")


# ============================================
# 3. INHERITANCE
# ============================================

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def speak(self):  # Override parent method
        print(f"{self.name} barks")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows")

dog = Dog("Buddy")
cat = Cat("Whiskers")
dog.speak()
cat.speak()


# ============================================
# 4. POLYMORPHISM
# ============================================

def animal_sound(animal):
    animal.speak()

animals = [Dog("Rex"), Cat("Mittens")]
for animal in animals:
    animal_sound(animal)


# ============================================
# 5. ABSTRACTION
# ============================================


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

rect = Rectangle(5, 10)
print(f"Rectangle area: {rect.area()}")


# ============================================
# 6. CLASS AND INSTANCE VARIABLES
# ============================================

class Student:
    school = "XYZ School"  # Class variable
    
    def __init__(self, name, grade):
        self.name = name  # Instance variable
        self.grade = grade

s1 = Student("Alice", 10)
s2 = Student("Bob", 9)
print(f"{s1.name} studies at {s1.school}")


# ============================================
# 7. STATIC AND CLASS METHODS
# ============================================

class MathOperations:
    pi = 3.14
    
    @staticmethod
    def add(a, b):
        return a + b
    
    @classmethod
    def get_pi(cls):
        return cls.pi

print(MathOperations.add(5, 3))
print(MathOperations.get_pi())


# ============================================
# 8. SPECIAL METHODS (__init__, __str__, etc.)
# ============================================

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    def __len__(self):
        return len(self.title)

book = Book("Python 101", "John Doe")
print(book)
print(f"Title length: {len(book)}")
'''
# class MyClass:
#     '''Hello Suryansh Vikram Singh'''
#     pass
# obj = MyClass()
# obj1=MyClass()
# print(MyClass.__dict__)
# print(MyClass.__doc__)
#print(type(obj))
# print(obj)
# print(id(obj))
# print(hex(id(obj)))
# print(type(MyClass))
# print(type(type))
# print(type(len))
# help(MyClass)

# class Student:
#     pass
# s1=Student()
# s1.name="Suryansh Vikram Singh"
# s1.roll=34
# print(s1.name)
# print(s1.roll)
# Student.var=100
# s2=Student()
# s2.name="Rahul"
# s2.roll=35
# print(s1.var)
# x=s1.__dict__
# print(x)
# print(type(x))
# print(Student.var)

#Everything in Python is an Object
# def greet():
#     print("Hello, World!")
# print(type(greet))   #greet is an object of function class

# Instance Method-->Defined inside a class and works with instance/object of the class.
# class Person:
#     def studying(self,m):
#         print(self)
#         return f"Students are studying for {m} hours."
# s1=Person()
# print(s1.studying(10))   #Error-->studying() takes 0 positional arguments
# print(s1)


# __init__ is a special method called a constructor used to initialize object attributes.
# class Student:
#     def __init__(self,arg1,arg2=0):
#         self.name = arg1
#         self.age = arg2

#         def studying(self,hours):
#             return f"Student is studying for {hours} hours."
# s1=Student("Suryansh",20)
# s2=Student("Rahul")
# print(s1.__dict__)
# print(s2.__dict__)

class Student:
    college='LPU'
    depart=['CSE','ECE','ME','CE']
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def studying(self,hours):
        return f"{self.name} is studying for {hours} hours."
s1=Student("Suryansh",20)
s2=Student("Rahul",21)
print(s1.__dict__)
print(s2.__dict__)
print(Student.__dict__)
s1.college="MIT" #Error-->'str' object is not callable
print(s1.college)
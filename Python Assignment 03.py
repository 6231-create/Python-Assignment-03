#Example of Overloading
class Math:
    def add(self, a, b=0, c=0):
        return a + b + c

m = Math()
print(m.add(5))        # 5
print(m.add(5, 10))    # 15
print(m.add(5, 10, 15))  # 30

#Example of Overriding
class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

d = Dog()
print(d.sound())   

#Example Demonstrating Both

class Student:
    # Default constructor
    def __init__(self):
        self.name = "Unknown"
        self.age = 0

class Person:
    # Parameterized constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Using default constructor
s = Student()
print(s.name, s.age)

# Using parameterized constructor
p = Person("John", 21)
print(p.name, p.age)


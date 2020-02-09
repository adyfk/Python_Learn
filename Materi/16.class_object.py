# Class in python

# Create Class
class MyFirstClass:
    name = "Adi Fatkhurozi"


print(MyFirstClass)

# Cretate An Object
class1 = MyFirstClass()

print(class1.name)

# create a class that has a constructor
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)

print(p1.name + " " + str(p1.age))

# Create a method in class
class Person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person1("John", 36)
p1.myfunc()

# Set the age property from p1
p1.age = 90

# Delete the age property from p1
del p1.age

# Pass Class
class Person2:
    pass

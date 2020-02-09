# Inheritance in python


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


# Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()


class Student(Person):
    pass


x = Student("Mike", "Olsen")
x.printname()


# Keep Call parent when override function
class Student1(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)


# Use the super() function to call parent
class Student2(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

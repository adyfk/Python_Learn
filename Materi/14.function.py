#Function in python

# Definition function


def my_function1():
    print("Hello from a function")


# Calling function
my_function1()


# Adding Parameter to function
def my_function2(fname):
    print(fname + " Refsnes")


my_function2("Emil")
my_function2("Tobias")
my_function2("Linus")


# Args to default parameter
def my_function3(*kids):
    print("The youngest child is " + kids[2])


my_function3("Emil", "Tobias", "Linus")


# Keyword Args
def my_function4(child3, child2, child1):
    print("The youngest child is " + child3)


my_function4(child1="Emil", child2="Tobias", child3="Linus")


# Arbitrary Keyword Arguments
# we can define like dict
def my_function5(**kid):
    print("His last name is " + kid["lname"])


my_function5(fname="Tobias", lname="Refsnes")


# Default Parameter Value
def my_function6(country="Norway"):
    print("I am from " + country)


my_function6("Sweden")
my_function6("India")
my_function6()
my_function6("Brazil")


# Passing list as arguments
def my_function7(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]

my_function7(fruits)


# Return Value
def my_function8(x):
    return 5 * x


print(my_function8(3))
print(my_function8(5))
print(my_function8(9))


# Pass function
def myfunction9():
    pass


# Recrusif / Recursion  Function
def tri_recursion(k):
    if(k > 0):
        result = k+tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
tri_recursion(6)

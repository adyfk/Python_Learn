try:
    print(x)
except:
    print("An exception occurred")

try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

# x = "hello"

# if not type(x) is int:
#     raise TypeError("Only integers are allowed")


# x = -1

# if x < 0:
#     raise Exception("Sorry, no numbers below zero")


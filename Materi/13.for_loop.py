# For Looping

# Looping String
for x in "banana":
    print(x)

# Looping List Array
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# Break Looping
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

# Continue Looping
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# Using Range to Loop
# range(start,stop,step)

for x in range(6):
    print(x)

for x in range(2, 6):
    print(x)

for x in range(2, 30, 3):
    print(x)

for x in range(6):
    print(x)
else:
    print("Finally finished!")


# Nested Loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

# Pass Loop
for x in [0, 1, 2]:
    pass

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

for x, y in thisdict.items():
    print(x, y)

# Looping dict
for x in thisdict.values():
    print(x)


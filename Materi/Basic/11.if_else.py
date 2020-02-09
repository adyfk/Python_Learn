# IF ELSE

if True:
    print("Test if True")
else:
    print("Test else")

if False:
    print("Test if True")
elif True:
    print("Test else True")


# sort hand If
print("A") if False else print("B")

print("A") if False else print("=") if True else print("B")

# Implement Logic
if True and True:
    print("Tampil")

if False or True:
    print("Tampil")


# Nested If
if True:
    print("Tampil")
    if True:
        print("True")
        if True:
            print("True")
        else:
            print("else")
    else:
        print("else")


# Empty IF
if True:
    pass

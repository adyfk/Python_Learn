# Scope area code
def myfunc():
    x = 300
    print(x)


myfunc()


def myfunc1():
    x = 300

    def myinnerfunc():
        print(x)

    myinnerfunc()


myfunc1()

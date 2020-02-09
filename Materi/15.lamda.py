# Lamda Function

# format using yapf
# x = lambda a : a + 10
# print(x(5))

# format using black
# def x(a):
#     return a + 10
# print(x(10))

x = lambda a, b: a * b
print(x(5, 6))

x = lambda a, b, c: a + b + c
print(x(5, 6, 2))


# Gunakan definisi fungsi itu untuk membuat fungsi yang selalu menggandakan nomor yang Anda kirim
def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)

print(mydoubler(11))

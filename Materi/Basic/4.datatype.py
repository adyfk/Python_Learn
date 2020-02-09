# BAB 1 Number

# ======================================================================
# Integer atau Int

x = 1
y = 33434343434343434
z = -2324234

# Float

v = 35e3
w = 12e4
x = 1.10
y = 1.0
z = -35.59

# complex

x = 3 + 5j
y = 5j
z = -5j


x = 1  # int
y = 2.8  # float
z = 1j  # complex

# convert from int to float:
a = float(x)

# convert from float to int:
b = int(y)

# convert from int to complex:
c = complex(x)

# You cannot convert complex numbers into another number type


# ========================================================================
# String varible

# Multiline string

a = """consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

a = """consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

text = " this is, mytext "
# index of string text[1]

# slice text[2:4]
# slice text[-2:-3]
# mengiris string

# len(text)
# menghitung panjang string

# text.strip()
# menghapus whitespace di depan atau di belakang

# text.lower()
# menjadikan string menjadi huruf kecil
# text.upper()
# menjadikan string menjadi huruf besar

# text.title()
# menjadikan capitalize

# text.replace("i","u")
# mengganti sebuah huruf / kata

# text.split(",")
# membagi string manjadi array berdasar parameter yang di tentukan

# text.join(",")

# "this is" in text
# "this is" not in text
#  check isi dalam string

# " " + " " + text
# Menggabungkan String (!Harus string)
# solusi convert to string
# str()
# atau
# text.format(number) // syarat define {} di dalam string , dalam parameter dapat di sisipkan angka untuk penjelasan {2}
# {:.2f}

# Escape Caracter
# "Test \"Test\" test"

# text.startswith("Hello")
# apakah text di awali dengan ""
# text.find("Hello")
# mencari "Hello" dalam text

# text.center(20, "O")
# Untuk memberi space kiri dan kanan text

# text.count("apple", 10, 24)
# Menghitung banyak text di antara index


# ========================================================================
# Bolean varible

# True
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

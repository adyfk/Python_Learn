# What is Standard Deviation (Simpangan Baku)?
# Standard deviation is a number that describes how spread out the values are.
# A low standard deviation means that most of the numbers are close to the mean (average) value.
# A high standard deviation means that the values are spread out over a wider range.

# Standard Deviation
# Contoh: Kali ini kami telah mendaftarkan kecepatan 7 mobil:
# speed = [86,87,88,86,87,85,86]
# 0.9
import numpy

speed = [86, 87, 88, 86, 87, 85, 86]
x = numpy.std(speed)
print(x)

# Variance
speed = [32, 111, 138, 28, 59, 77, 97]
x = numpy.var(speed)
print(x)


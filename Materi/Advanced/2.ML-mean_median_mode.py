import numpy

# Mean ====================
# The mean value is the average value.

# (99+86+87+88+111+86+103+87+94+78+77+85+86) / 13 = 89.77


speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
x = numpy.mean(speed)
print(x)


# Median ====================
# The median value is the value in the middle, after you have sorted all the values:

# 77, 78, 85, 86, 86, 86, [87], 87, 88, 94, 99, 103, 111

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
x = numpy.median(speed)
print(x)

# If there are two numbers in the middle, divide the sum of those numbers by two.

# 77, 78, 85, 86, 86, 86, 87, 87, 94, 98, 99, 103
# (86 + 87) / 2 = 86.5

speed = [99, 86, 87, 88, 86, 103, 87, 94, 78, 77, 85, 86]
x = numpy.median(speed)
print(x)

# Mode
# The Mode value is the value that appears the most number of times:

# 99, [86], 87, 88, 111, [86], 103, 87, 94, 78, 77, 85, [86] = 86

from scipy import stats

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

x = stats.mode(speed)
print(x)

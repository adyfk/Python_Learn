# What are Percentiles?
# Percentiles are used in statistics to give you a number
# that describes the value that a given percent of the values are lower than.

# Contoh: Katakanlah kita memiliki sederetan usia semua orang yang hidup di jalanan.
# ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
# Berapakah persentase 75.? Jawabannya adalah 43, artinya 75% orang berusia 43 atau lebih muda.

import numpy

ages = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39, 80, 82, 32, 2, 8, 6, 25, 36, 27, 61, 31]
x = numpy.percentile(ages, 75)
print(x)

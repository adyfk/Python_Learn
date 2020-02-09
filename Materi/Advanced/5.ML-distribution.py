# Buat array yang berisi 250 float acak antara 0 dan 5:

import numpy

x = numpy.random.uniform(0.0, 5.0, 250)
print(x)


# Histogram
# Untuk memvisualisasikan set data, kami dapat menggambar histogram dengan data yang kami kumpulkan.

import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 9.0, 250)

plt.hist(x, 5)
plt.show()

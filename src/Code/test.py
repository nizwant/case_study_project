from matplotlib import pyplot as plt
from random import shuffle
from initialization import initialize_temperatures

# plt.hist(initialize_temperatures(10000, 20, 35))
# plt.show()


x = list(range(1, 10))
shuffle(x)
print(x)

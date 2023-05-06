from initialization import initiate_temperatures
from matplotlib import pyplot as plt

plt.hist(initiate_temperatures(10000, 20, 35))
plt.show()

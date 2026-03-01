import numpy as np


data = np.loadtxt("Data.txt", delimiter="\t", skiprows=1)

x = data[:, 0]   # first column
y = data[:, 1]   # second column

print(data)
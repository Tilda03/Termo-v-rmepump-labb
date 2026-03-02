import numpy as np


data = np.loadtxt("Data.txt", delimiter="\t", skiprows=1)

minutes = data[:, 0]   # first column
T_w = data[:, 1]   # second column
T_k = data[:, 2]
P_effect = data[:, 3]
T_1 = data[:, 4]
T_2 = data[:, 5]
T_3 = data[:, 6]
T_4 = data[:, 7]
P_1 = data[:, 8]
P_2 = data[:, 9]


print(data)

print(T_3)
import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt("Data.txt", delimiter="\t", skiprows=1)

minutes = data[:, 0] 
T_w = data[:, 1]  
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

plt.scatter(minutes, T_1, label='T1')
plt.scatter(minutes, T_2, label='T2')
plt.scatter(minutes, T_3, label='T3')
plt.scatter(minutes, T_4, label='T4')
plt.legend()
plt.show()
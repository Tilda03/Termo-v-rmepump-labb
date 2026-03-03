import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt("Data.txt", delimiter="\t", skiprows=1)

seconds = data[:, 0] * 60 # seconds
T_w = data[:, 1]  
T_k = data[:, 2]
P_effect = data[:, 3]
T_1 = data[:, 4]
T_2 = data[:, 5]
T_3 = data[:, 6]
T_4 = data[:, 7]
P_1 = data[:, 8]
P_2 = data[:, 9]


c = 4180 # J / kg * K
m = 3 # kg


def COP(c, m, T, P, t):
    dT_dt = np.gradient(T, t)
    return (c * m * dT_dt) / P



COP_HP = COP(c, m, T_w, P_effect, seconds)
COP_R = COP(c, m, T_k, P_effect, seconds)

mean_HP = np.nanmean(COP_HP)
mean_R  = np.nanmean(COP_R)

print(f'Medelvärde COP_HP {mean_HP} och medelvärde COP_R {mean_R}')

plt.plot(seconds, T_1, label='T1')
plt.plot(seconds, T_2, label='T2')
plt.plot(seconds, T_3, label='T3')
plt.plot(seconds, T_4, label='T4')
plt.legend()
plt.show()

plt.plot(seconds / 60, COP_HP, label='COP_HP', color='crimson')
plt.plot(seconds / 60, COP_R, label='COP_R', color='royalblue')
plt.axhline(mean_HP, linestyle='--', label='COP_HP medelvärde', color='crimson')
plt.axhline(mean_R, linestyle='--', label='COP_R medelvärde', color='royalblue')

plt.xlabel('Tid (minuter)')
plt.ylabel('COP')
plt.legend()
plt.show()
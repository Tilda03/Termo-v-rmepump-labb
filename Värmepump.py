import numpy as np
import matplotlib.pyplot as plt
import Entalpi

data = np.loadtxt("Data.txt", delimiter="\t", skiprows=1)

seconds = data[:, 0] * 60 # seconds
minutes = data[:, 0] # minutes
T_w = data[:, 1] + 273
T_k = data[:, 2] + 273
P_effect = data[:, 3]
T_1 = data[:, 4] + 273
T_2 = data[:, 5] + 273
T_3 = data[:, 6] + 273
T_4 = data[:, 7] + 273
P_1 = data[:, 8] + 273
P_2 = data[:, 9] + 273


c = 4180 # J / kg * K
m = 6 # kg


def COP(c, m, T, P, t):
    dT_dt = np.gradient(T, t)
    return (c * m * dT_dt) / P



COP_HP = COP(c, m, T_w, P_effect, seconds)
COP_R = -COP(c, m, T_k, P_effect, seconds) # temperature is decreasing

steady = slice(10, 25)  # välj efter grafen
mean_HP = np.nanmean(COP_HP[steady])
mean_R  = np.nanmean(COP_R[steady])

print(f'Medelvärde COP_HP {mean_HP} och medelvärde COP_R {mean_R}')


plt.plot(minutes, T_3, label='T3', color='darkred')
plt.plot(minutes, T_4, label='T4', color='crimson')
plt.plot(minutes, T_w, label='T_w', color='darkorange')
plt.plot(minutes, T_1, label='T1', color='royalblue')
plt.plot(minutes, T_2, label='T2', color='lightblue')
plt.plot(minutes, T_k, label='T_k', color='forestgreen')
plt.title('Temperatur som en funktion av tid')
plt.xlabel('Tid (minuter)')
plt.ylabel('Temperatur (K)')
plt.legend()
plt.show()

plt.plot(minutes, COP_HP, label=r'$COP_{HP}$', color='crimson')
plt.plot(minutes, COP_R, label=r'$COP_R$', color='royalblue')
plt.axhline(mean_HP, linestyle='--', label=r'$COP_{HP} medelvärde$', color='crimson')
plt.axhline(mean_R, linestyle='--', label=r'$COP_R medelvärde$', color='royalblue')
Entalpi.get_plot()
plt.title('COP som en funktion av tid')
plt.xlabel('Tid (minuter)')
plt.ylabel('COP')
plt.legend()
plt.show()



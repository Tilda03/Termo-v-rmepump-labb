import numpy as np
import matplotlib.pyplot as plt

val = np.loadtxt('./labbvärden.csv', skiprows=1, delimiter=';')

th= val[:,1]
tl= val[:,2]
tid= val[:,0]

COP_w=th/(th-tl)
COP_k=tl/(th-tl)

plt.plot(tid, COP_w, label='COP kylning')
plt.plot(tid, COP_k, label='COP värmning')
plt.xlabel('Tid (min)')
plt.ylabel('COP')
plt.ylim(0,10)
plt.title('COP för kylning och värmning över tid')

plt.legend()
plt.grid()
plt.show()

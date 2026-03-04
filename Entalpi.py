from cProfile import label

from pyfluids import Fluid, FluidsList, Input
import numpy as np
import matplotlib.pyplot as plt

def get_plot():
    plt.plot(tid, COP_w1, '--', color='forestgreen',label=r'$COP_k$, carnotcykel')
    plt.plot(tid, COP_k1, '--', color='darkgreen', label=r'$COP_w$, carnotcykel')
    plt.plot(tid, COP_w, color= "deeppink", label=r'$COP_w$')
    plt.plot(tid, COP_k, color= "rebeccapurple", label=r'$COP_k$')
    plt.axhline(mean_w, linestyle='--', label=r'$COP_w medelvärde$', color='deeppink')
    plt.axhline(mean_k, linestyle='--', label=r'$COP_k medelvärde$', color='rebeccapurple')
    plt.ylim(-0.5,4.5)


val = np.loadtxt('./temptryck.csv', skiprows=1, delimiter=';')
#np arrays för Temperaturer och tryck
T1c= val[:,0]
T2c= val[:,1]
T3c= val[:,2]
T4c= val[:,3]
P1b= val[:,4]
P2b= val[:,5]

#konvertera till Kelvin
T1= T1c + 273.15
T2= T2c + 273.15
T3= T3c + 273.15
T4= T4c + 273.15
P1= P1b * 100000
P2= P2b * 100000

kylmedium= Fluid(FluidsList.R134a)

h1= np.zeros(len(T1))
h2= np.zeros(len(T1))
h3= np.zeros(len(T1))
h4= np.zeros(len(T1))

for i in range(len(T1)):
    kylmedium.update(
        Input.pressure(P1[i]),
        Input.temperature(T1[i])
    )
    h1[i]= kylmedium.enthalpy
    kylmedium.update(
        Input.pressure(P1[i]),
        Input.temperature(T2[i])
    )
    h2[i]= kylmedium.enthalpy
    kylmedium.update(
        Input.pressure(P2[i]),
        Input.temperature(T3[i])
    )
    h3[i]= kylmedium.enthalpy
    kylmedium.update(
        Input.pressure(P2[i]),
        Input.temperature(T4[i])
    )
    h4[i]= kylmedium.enthalpy   

 
vals = np.loadtxt('./labbvärden.csv', skiprows=1, delimiter=';')

th= vals[:,1]
tl= vals[:,2]
tid= vals[:,0]

th = th + 273
tl = tl + 273

COP_w1=th/(th-tl)
COP_k1=tl/(th-tl)


COP_w= (h3-h4)/(h3-h2)
COP_k= (h2-h1)/(h3-h2)
mean_w = np.nanmean(COP_w)
mean_k  = np.nanmean(COP_k)

tid= np.arange(0,38, 1, dtype=float)
tid[31]=31.6

#print( h1,h2,h3,h4 )

#plt.plot(tid, T1, label='T1')
#plt.plot(tid, T2, label='T2')
#plt.plot(tid, T3, label='T3')
#plt.plot(tid, T4, label='T4')
#plt.plot(tid, COP_w1, '--', color='rebeccapurple',label=r'$COP_k$, carnotcykel')
#plt.plot(tid, COP_k1, '--', color='deeppink', label=r'$COP_w$, carnotcykel')
#plt.ylim(-1,4)
#plt.plot(tid, COP_w, color= "deeppink", label=r'$COP_w$')
#plt.plot(tid, COP_k, color= "rebeccapurple", label=r'$COP_k$')
#plt.axhline(mean_w, linestyle='--', label=r'$COP_w medelvärde$', color='deeppink')
#plt.axhline(mean_k, linestyle='--', label=r'$COP_k medelvärde$', color='rebeccapurple')
#plt.xlabel('Tid (min)')
#plt.ylabel('COP')
#plt.title('COP för värmepumpen över tid')
#plt.legend()
#plt.grid()
#plt.show()

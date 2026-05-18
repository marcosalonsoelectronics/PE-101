# -*- coding: utf-8 -*-
"""
Curve fitting Zth
"""
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
# Thermal resistance
Rth=1.76
# Zth expression
def Zth(t, tau):
    return Rth*( 1-np.exp(-t/tau) )
# Curve data
Npoints = 11
tdata = np.array([0, 1e-5, 3e-5, 1e-4, 3e-4, 1e-3, 3e-3, 1e-2, 3e-2,\
1e-1, 3e-1])   
Zdata = np.array([0, 0.0340, 0.0591, 0.1067, 0.1880, 0.3436, 0.6165,\
1.0608, 1.4339, 1.7285, 1.7600])
Zfit=  np.arange(0, Npoints, 1, dtype=float)
Err=   np.arange(0, Npoints, 1, dtype=float)
# Curve fitting
popt, pcov = curve_fit(Zth, tdata, Zdata)
tau=popt[0]; C=tau/Rth
print("Tau= ", tau); print("C= ", C)
# Print data and error
for i in range (0, Npoints):
    Zfit[i]= Zth(tdata[i], tau)
    Err[i]= (Zfit[i] - Zdata[i])*100/Zdata[i]
    print(tdata[i], Zdata[i], Zfit[i], Err[i]) 
# Plot curves
plt.figure(1)
plt.plot(tdata, Zdata, 'bs-', label='data') 
plt.plot(tdata, Zfit, 'rs', label='fitting') 
plt.xlabel('Time (s)'); plt.ylabel('Zth (ºC/W)')
# plt.xlim(-0.05, 0.3)
plt.grid(); plt.legend(); plt.show();
# Plot error
plt.figure(2)
plt.plot(tdata, Err, 'bs', label='%Error') 
plt.bar(tdata, Err, width=0.001, color='r') 
plt.xlabel('Time (s)')
plt.grid(); plt.ylabel('%Err'); plt.legend(); plt.show()



from __future__ import division
import numpy as np

import matplotlib.pyplot as plt

data = np.genfromtxt('data_1_b.csv', delimiter = ',')


T = data[1:,0] #Temperature


ror_may=data[1:,1] #obtained from Data Thief (Rosenthal and Bezanilla 2000)

rof_may=data[1:,6] #obtained from Data Thief (Rosenthal and Bezanilla 2000)

ror_mhh = data[1:,2] #mHH model estimates for ROR 
rof_mhh = data[1:,5] #mHH model estimates for ROF 

ror_hh = data[1:,3] #HH model estimates for ROR 
rof_hh = data[1:,4] #HH model estimates for ROF

rof_error_lower = data[1:,7]
rof_error_lower = np.abs(list(np.array(rof_error_lower) - np.array(rof_may)))
rof_error_upper = data[1:,8] 
rof_error_upper = np.abs(list(np.array(rof_error_upper) - np.array(rof_may)))

ror_error_lower = data[1:,9]
ror_error_lower = np.abs(list(np.array(ror_error_lower) - np.array(ror_may)))
ror_error_upper = data[1:,10]
ror_error_upper = np.abs(list(np.array(ror_error_upper) - np.array(ror_may)))

plt.plot(T,ror_mhh,"r",lw = 3, zorder = 1)
plt.scatter(T,ror_may,marker='o',color='k',s = 2,  label='Published experimental results (ROR)', lw = 3, zorder = 3)
plt.errorbar(T, ror_may,xerr = 0, yerr = [ror_error_lower, ror_error_upper], color = 'k', fmt = 'o', markersize = 1, capsize = 1, zorder = 2)



plt.plot(T,ror_hh,"k--",label='HH model predictions', lw = 3)




plt.plot(T,rof_mhh,"r",lw = 3, zorder = 1)
plt.scatter(T,rof_may,marker='o',color='blue',s = 2,  label='Published experimental results (ROR)', lw = 3, zorder = 3)
plt.errorbar(T, rof_may,xerr = 0, yerr = [rof_error_lower, rof_error_upper], color = 'k', fmt = 'o', markersize = 1, capsize = 1, zorder = 2)


plt.plot(T,rof_hh,"k--", lw = 3)



#plt.xlabel(r'Temperature ($^o$C)', fontsize = 16)
#plt.ylabel('dV/dt (mV/ms)', fontsize = 16)
plt.xlim(2.5,30)
plt.ylim(0, 900)
###Optional labeling if required 
#plt.text(25.5, 784, 'mHH model \n ROR')
#plt.text(25.5, 585, 'HH model \n ROR')
#plt.text(25.5, 516, 'mHH model \nROF')
#plt.text(25.5, 278, 'HH model \n ROF')
#plt.legend(loc=2,prop={'size':10})

plt.savefig('1b.png',format='png',dpi=600,bbox_inches='tight')
plt.show()


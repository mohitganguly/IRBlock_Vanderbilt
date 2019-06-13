from __future__ import division

import numpy as np
import matplotlib
import matplotlib.pyplot as plt


temp = [32, 33, 34, 35, 36, 37, 38, 39]

pas = [16375, 16375, 16375, 16375,16375,16375,16375,16375,]
na_only = [11100,11000,10975,10950,10900,10850,10800,10750]
k_only = [4570,4540,4510,4490,4470,4460,4450,4440]
norm = [9525,6850,6025,5625,5375,5275,5200,5150]


plt.plot(temp, pas, '-o', lw = 2)
plt.plot(temp, na_only, '-o', lw = 2)
plt.plot(temp, k_only, '-o', lw = 2)
plt.plot(temp, norm, '-o', lw = 2)

plt.xlim(31.5, 39.5)
plt.ylim(0, 18000)

#plt.xticks([])
#plt.yticks([])

#plt.savefig('HH_noclamp.png', format = 'png', dpi = 600, bbox_inches = 'tight')
plt.show()

pas_clamp = [12450,12450,12450,12450,12450,12450,12450,12450] 
na_only_clamp = [12525,12375,12350,12325,12300,12200,12125,12100]
k_only_clamp = [4400,4360,4340,4300,4240,4220,4210,4200]


plt.plot(temp, pas_clamp, '-o', lw = 2)
#plt.plot(temp, na_only_clamp, '-o', lw = 2)
plt.plot(temp, k_only_clamp, '-o', lw = 2, color = 'indianred')
plt.plot(temp, norm, '--', lw = 2, color = 'k')

plt.xlim(31.5, 39.5)
plt.ylim(0, 18000)

#plt.savefig('HH_clamp.png', format = 'png', dpi = 600, bbox_inches = 'tight')
plt.show()

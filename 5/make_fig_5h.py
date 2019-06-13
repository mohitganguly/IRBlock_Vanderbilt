import numpy as np

import matplotlib.pyplot as plt

import matplotlib as mpl


v_prox_cont = np.genfromtxt('v_prox_cont.txt', delimiter = ',')
v_end_cont = np.genfromtxt('v_end_cont.txt', delimiter = ',')
time = np.genfromtxt('time-2.txt', delimiter = ',')


plt.plot(time, v_prox_cont, lw = 2)
plt.plot(time, v_end_cont, lw = 2, linestyle = '--')
plt.xlim(250, 400)

plt.savefig('fig5h.png', format = 'png', dpi = 600, bbox_inches = 'tight')

plt.show()

plt.plot(time, v_end_cont, lw = 5, color = 'green',linestyle = '--')
plt.xlim(255, 275)
plt.ylim(-67.60, -67.55)
plt.xticks([])
plt.yticks([])
plt.savefig('inset.png', format = 'png', dpi = 600, bbox_inches = 'tight')
plt.show()






v_prox_pulse = np.genfromtxt('v_prox_pulse.txt', delimiter = ',')
v_end_pulse = np.genfromtxt('v_end_pulse.txt', delimiter = ',')
time = np.genfromtxt('time-2.txt', delimiter = ',')


plt.plot(time, v_prox_pulse, lw = 2)
plt.plot(time, v_end_pulse, lw = 2, linestyle = '--')
plt.xlim(250, 400)
plt.savefig('fig5i.png', format = 'png', dpi = 600, bbox_inches = 'tight')
plt.show()

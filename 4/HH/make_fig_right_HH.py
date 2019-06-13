import numpy as np
import matplotlib.pyplot as plt

t = np.genfromtxt('time.csv', delimiter = ',') 
v_c_hot = np.genfromtxt('v_c_hot_HHdclamp.csv', delimiter = ',')
v_c_cold = np.genfromtxt('v_c_cold_HHdclamp.csv', delimiter = ',')

v_e_hot = np.genfromtxt('v_e_hot_HHdclamp.csv', delimiter = ',')
v_e_cold = np.genfromtxt('v_e_cold_HHdclamp.csv', delimiter = ',')

v_g_hot = np.genfromtxt('v_g_hot_HHdclamp.csv', delimiter = ',')
v_g_cold = np.genfromtxt('v_g_cold_HHdclamp.csv', delimiter = ',')

v_i_hot = np.genfromtxt('v_i_hot_HHdclamp.csv', delimiter = ',')
v_i_cold = np.genfromtxt('v_i_cold_HHdclamp.csv', delimiter = ',')


#print len(t), len(v_c_hot)
#plt.legend()
#plt.xlim(0,20)

#plt.savefig('fig.jpeg', format = 'jpeg', dpi = 600, bbox_inches = 'tight')
#plt.show()

ax = plt.subplot(4, 1, 1)
plt.plot(t, v_c_hot, lw = 2, color = 'indianred', linestyle = ':')
plt.plot(t, v_c_cold, lw = 1, color = 'blue')
plt.xlim(100, 120)
plt.ylim(-80, 60)
ax.set_yticklabels([])
ax.set_yticks([])
ax.set_xticklabels([])
ax.set_xticks([])
x0,x1 = ax.get_xlim()
y0,y1 = ax.get_ylim()
ax.set_aspect(abs(x1-x0)/abs(y1-y0))

ax = plt.subplot(4, 1, 2)
plt.plot(t, v_e_hot, lw = 2, color = 'indianred', linestyle = ':')
plt.plot(t, v_e_cold, lw = 1, color = 'blue')
plt.xlim(100, 120)
plt.ylim(-80, 60)
ax.set_yticklabels([])
ax.set_yticks([])
ax.set_xticklabels([])
ax.set_xticks([])
x0,x1 = ax.get_xlim()
y0,y1 = ax.get_ylim()
ax.set_aspect(abs(x1-x0)/abs(y1-y0))

ax = plt.subplot(4, 1, 3)
plt.plot(t, v_g_hot, lw = 2, color = 'indianred', linestyle = ':')
plt.plot(t, v_g_cold, lw = 1, color = 'blue')
plt.xlim(100, 120)
plt.ylim(-80, 60)
ax.set_yticklabels([])
ax.set_yticks([])
ax.set_xticklabels([])
ax.set_xticks([])
x0,x1 = ax.get_xlim()
y0,y1 = ax.get_ylim()
ax.set_aspect(abs(x1-x0)/abs(y1-y0))

ax = plt.subplot(4, 1, 4)
plt.plot(t, v_i_hot,lw = 2, color = 'indianred', linestyle = ':')
plt.plot(t, v_i_cold, lw = 1, color = 'blue')

plt.xlim(100, 120)
plt.ylim(-80, 60)
ax.set_yticklabels([])
ax.set_yticks([])
ax.set_xticklabels([])
ax.set_xticks([])
x0,x1 = ax.get_xlim()
y0,y1 = ax.get_ylim()
ax.set_aspect(abs(x1-x0)/abs(y1-y0))

plt.savefig('fig_right_HH.png', format = 'png', dpi = 600, bbox_inches = 'tight')
plt.show()

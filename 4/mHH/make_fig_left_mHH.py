import numpy as np
import matplotlib.pyplot as plt

t = np.genfromtxt('time.csv', delimiter = ',')
v_b_hot = np.genfromtxt('v_b_hot_mHHdclamp.csv', delimiter = ',')
v_b_cold = np.genfromtxt('v_b_cold_mHHdclamp.csv', delimiter = ',')

v_d_hot = np.genfromtxt('v_d_hot_mHHdclamp.csv', delimiter = ',')
v_d_cold = np.genfromtxt('v_d_cold_mHHdclamp.csv', delimiter = ',')

v_f_hot = np.genfromtxt('v_f_hot_mHHdclamp.csv', delimiter = ',')
v_f_cold = np.genfromtxt('v_f_cold_mHHdclamp.csv', delimiter = ',')

v_h_hot = np.genfromtxt('v_h_hot_mHHdclamp.csv', delimiter = ',')
v_h_cold = np.genfromtxt('v_h_cold_mHHdclamp.csv', delimiter = ',')



#plt.legend()
#plt.xlim(0,20)

#plt.savefig('fig.jpeg', format = 'jpeg', dpi = 600, bbox_inches = 'tight')
#plt.show()

ax = plt.subplot(4, 1, 1)
plt.plot(t, v_b_hot, lw = 2, linestyle = ':', color = 'indianred')
plt.plot(t, v_b_cold, lw = 1, color = 'blue')
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
plt.plot(t, v_d_hot, lw = 2, linestyle = ':', color = 'indianred')
plt.plot(t, v_d_cold, lw = 1, color = 'blue')
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
plt.plot(t, v_f_hot, lw = 2, linestyle = ':', color = 'indianred')
plt.plot(t, v_f_cold, lw = 1, color = 'blue')
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
plt.plot(t, v_h_hot, lw = 2, linestyle = ':', color = 'indianred')
plt.plot(t, v_h_cold, lw = 1, color = 'blue')

plt.xlim(100, 120)
plt.ylim(-80, 60)
ax.set_yticklabels([])
ax.set_yticks([])
ax.set_xticklabels([])
ax.set_xticks([])
x0,x1 = ax.get_xlim()
y0,y1 = ax.get_ylim()
ax.set_aspect(abs(x1-x0)/abs(y1-y0))
plt.savefig('fig_left_mHH.png', format = 'png', dpi = 600, bbox_inches = 'tight')
plt.show()

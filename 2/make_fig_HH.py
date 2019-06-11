import numpy as np

import matplotlib.pyplot as plt




time = np.genfromtxt('time.csv', delimiter = ',')
ina = np.genfromtxt('ina_HH_25.csv', delimiter = ',')
ik = np.genfromtxt('ik_HH_25.csv', delimiter = ',')
i = np.genfromtxt('i_HH_25.csv', delimiter = ',')
#i = ina + ik
temp_x = np.genfromtxt('temp_x.csv', delimiter = ',')
#area_norm = -0.2711

plt.plot(i)
plt.show()
i_na = i.copy()
i_k = i.copy()

i_na[i>0]=0
i_k[i<0]=0

plt.plot(i_na)
plt.plot(i_k)
plt.show()
area_norm=np.trapz(i_na,time,dx=0.001)


print (area_norm)

area_na = np.trapz(i_na,time,dx=0.001)/area_norm
area_k = np.trapz(i_k,time,dx=0.001)/area_norm



print area_na, area_k, (area_k/area_na)
ax = plt.subplot(1, 1, 1)
plt.plot(temp_x, lw = 3)
#plt.xlim(0, 100)
plt.ylim(0, 30)
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_xticks([])

x0,x1 = ax.get_xlim()
y0,y1 = ax.get_ylim()
ax.set_aspect(0.5*abs(x1-x0)/abs(y1-y0))
plt.savefig('temp_x.png', format = 'png', dpi = 600, bbox_inches = 'tight')
plt.show()




ax = plt.subplot(1, 4, 1)
plt.plot(time,ina,lw=1)
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_xticks([])
plt.ylim(-5, 5)
plt.xlim(50, 60)
x0,x1 = ax.get_xlim()
y0,y1 = ax.get_ylim()
ax.set_aspect(abs(x1-x0)/abs(y1-y0))



ax = plt.subplot(1, 4, 2)
plt.plot(time,ik,lw=1)
ax.set_xticklabels([])
ax.set_xticks([])
ax.set_yticklabels([])
plt.ylim(-5, 5)
plt.xlim(50, 60)
x0,x1 = ax.get_xlim()
y0,y1 = ax.get_ylim()
ax.set_aspect(abs(x1-x0)/abs(y1-y0))


ax = plt.subplot(1, 4, 3)
plt.plot(time,i,lw=1)
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_xticks([])
plt.ylim(-5, 5)
plt.xlim(50, 60)
x0,x1 = ax.get_xlim()
y0,y1 = ax.get_ylim()
ax.set_aspect(abs(x1-x0)/abs(y1-y0))


T = 25
width = 2
ax = plt.subplot(1, 4, 4)
plt.bar(T-width,area_na, width , color = 'darkgreen')
plt.bar(T,-area_k,  width, color='indianred')
ax.set_xticklabels([])
ax.set_yticklabels([])
plt.ylim(0,5)
ax.set_xticks([])
x0,x1 = ax.get_xlim()
y0,y1 = ax.get_ylim()
ax.set_aspect(abs(x1-x0)/abs(y1-y0))



#plt.savefig('HH_25.png', format = 'png', dpi = 600, bbox_inches = 'tight')


plt.show()

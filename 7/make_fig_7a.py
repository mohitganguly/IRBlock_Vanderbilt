from __future__ import division 

import numpy as np

import matplotlib.pyplot as plt
import itertools

nseg = 999
l = 20
blocks = np.genfromtxt('block_HH.txt', delimiter = '	')
x = range(32,40)
dia = blocks[0:,0]
print len(dia)
block1 = blocks[0,1:]
block1 = block1*l/nseg
block2 = blocks[1,1:]
block1 = block2*l/nseg
block3 = blocks[2,1:]
block1 = block3*l/nseg
block4 = blocks[3,1:]
block1 = block4*l/nseg
block5 = blocks[4,1:]
block1 = block5*l/nseg

i = 0

for i in range(5):
	plt.plot(x, blocks[i,1:]*l/nseg, '-o', lw = 3)
	

plt.xlim(31,40)
#plt.ylabel('Threshold Block Width (mm)', fontsize = 16)
#plt.xlabel('Temperature of Block ($^o$C)', fontsize = 16)
#plt.text(39.1, blocks[0,-1]*l/nseg, '500 $\mu m$')

#plt.text(39.1, blocks[1,-1]*l/nseg, '250 $\mu m$')
#plt.text(39.1, blocks[2,-1]*l/nseg, '100 $\mu m$')
#plt.text(39.1, blocks[3,-1]*l/nseg, '10 $\mu m$')
#plt.text(39.1, blocks[4,-1]*l/nseg, '1 $\mu m$')

plt.ylim(-1,11)
plt.vlines(x=33, ymin = float(21*l/nseg), ymax = float(347*l/nseg), linewidth=3, color = 'k')
plt.vlines(x=36, ymin = float(19*l/nseg), ymax = float(268*l/nseg), linewidth=3, color = 'k')
plt.vlines(x=39, ymin = float(19*l/nseg), ymax = float(257*l/nseg), linewidth=3, color = 'k')
plt.savefig('fig_supp.jpeg', format = 'jpeg', dpi = 600)
plt.show()

fig=plt.figure()
ax=fig.add_subplot(111)
ax.set_color_cycle(['b','g','r','c', 'm'])
sqrt_dia = np.sqrt(dia)
#marker_color = itertools.cycle(('b','g','r','b'))
a = [1,4,7]

m_33, c_33 = np.polyfit(sqrt_dia, blocks[:,2]*l/nseg, 1)
m_36, c_36 = np.polyfit(sqrt_dia, blocks[:,5]*l/nseg, 1)
m_39, c_39 = np.polyfit(sqrt_dia, blocks[:,8]*l/nseg, 1)
color = ['r', 'b', 'g']
x = 0
for i in a:
	
	plt.scatter(sqrt_dia, blocks[:,(i+1)]*l/nseg,c = color[x], s = 30)
	x = x+1
	#plt.plot(sqrt_dia, blocks[:,(i+1)]*l/nseg, color = 'k', lw = 1)
	#plt.text (23, blocks[0,(i+1)]*l/nseg, '%d'%x[i], fontsize = 10)
#dia = blocks[:,0]

#plt.scatter(sqrt_dia, block1, c=['b','g','r','c', 'm'], s = 72)

#plt.plot(sqrt_dia, block1, color = 'k')
#plt.plot(sqrt_dia, block2, color = 'k')

#plt.ylabel('Threshold Block Width (mm)', fontsize = 16)
#plt.xlabel('$\sqrt{Axon Diameter (\mu m)} $', fontsize = 16)
ax = plt.subplot(1, 1, 1)
plt.plot(sqrt_dia, m_33 * sqrt_dia + c_33, color = 'r', lw = 2.5)
plt.plot(sqrt_dia, m_36 * sqrt_dia + c_36, color = 'b', lw = 2.5)
plt.plot(sqrt_dia, m_39 * sqrt_dia + c_39, color = 'g', lw = 2.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.xlim(-1,24)
plt.ylim(0,7.5)
#plt.savefig('7c.jpeg', format = 'jpeg', dpi = 600)
plt.show()


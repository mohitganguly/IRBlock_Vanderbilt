import numpy as np
import matplotlib
import matplotlib.pyplot as plt
#matplotlib.use('tk')

#nseg = 999
#l = 20
#blocks = np.genfromtxt('large_dia.txt', delimiter = '	')
dia = [500, 250, 100, 50, 10, 5, 2.5, 1, 0.5]
sqrt_dia = np.sqrt(dia)
#print sqrt_dia

ax = plt.subplot(1, 1, 1)
block29_5 = [900, 636, 404, 286, 128, 92,64,42,28]
block30_5 = [880, 620, 390, 280, 126, 90,62,40,26]
block31_5 = [860, 610, 386, 272, 122, 86,60,38,24]

plt.plot(sqrt_dia, block29_5, 'o', lw = 3)
plt.plot(sqrt_dia, block30_5, 'o', lw = 3)
plt.plot(sqrt_dia, block31_5, 'o', lw = 3 )

m_29_5, c_29_5 = np.polyfit(sqrt_dia, block29_5, 1)
m_30_5, c_30_5 = np.polyfit(sqrt_dia, block30_5, 1)
m_31_5, c_31_5 = np.polyfit(sqrt_dia, block31_5, 1)
print m_29_5, c_29_5
print m_30_5, c_30_5
print m_31_5, c_31_5

plt.plot(sqrt_dia, m_29_5 * sqrt_dia + c_29_5, color = 'b', lw = 3)
plt.plot(sqrt_dia, m_30_5 * sqrt_dia + c_30_5, color = 'g' , lw = 3)
plt.plot(sqrt_dia, m_31_5 * sqrt_dia + c_31_5, color = 'r' , lw = 3)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
#plt.spines['bottom'].set_visible(False)
#plt.spines['left'].set_visible(False)
#plt.savefig('7a.png', format = 'png', dpi = 600)

plt.show()

##################################
#magnified version
dia = [5, 2.5, 1, 0.5]
sqrt_dia = np.sqrt(dia)
#print sqrt_dia
nseg1 = 4999
#block25 = blocks[5:, 1]
#block25 = 
#block28 = blocks[5:, 2]
#block28 = block28*l/nseg
#block31 = blocks[5:, 3]
#block31 = block31*l/nseg
block29_5 = [92,64,42,28]
block30_5 = [90,62,40,26]
block31_5 = [86,60,38,24]

plt.plot(sqrt_dia, block29_5, 'o')
plt.plot(sqrt_dia, block30_5, 'o')
plt.plot(sqrt_dia, block31_5, 'o')


#m_29_5, c_29_5 = np.polyfit(sqrt_dia, block29_5, 1)
#m_30_5, c_30_5 = np.polyfit(sqrt_dia, block30_5, 1)
#m_31_5, c_31_5 = np.polyfit(sqrt_dia, block31_5, 1)
#plt.text(sqrt_dia[0]+ d, block25[0], '25 $^o$C')
#plt.text(sqrt_dia[0]+ d, block28[0], '28 $^o$C')
#plt.text(sqrt_dia[0]+ d, block31[0], '31 $^o$C')

ax = plt.subplot(1, 1, 1)
plt.plot(sqrt_dia, m_29_5 * sqrt_dia + c_29_5, color = 'b', lw = 3)
plt.plot(sqrt_dia, m_30_5 * sqrt_dia + c_30_5, color = 'g',  lw = 3)
plt.plot(sqrt_dia, m_31_5 * sqrt_dia + c_31_5, color = 'r' , lw = 3)

print m_29_5, c_29_5
print m_30_5, c_30_5
print m_31_5, c_31_5


#plt.xlabel('$\sqrt{Axon Diameter (\mu m)} $', fontsize = 16)
#plt.ylabel('Threshold Block Length (mm)', fontsize = 16)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.ylim(10,120)
#plt.savefig('7b.png', format = 'png', dpi = 600)
plt.show()

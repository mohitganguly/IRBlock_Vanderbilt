from __future__ import division

import numpy as np
import matplotlib
import matplotlib.pyplot as plt



def read_large_txt(path, delimiter=None, dtype=None):
    with open(path) as f:
        nrows = sum(1 for line in f)
        f.seek(0)
        ncols = len(f.next().split(delimiter))
        out = np.empty((nrows, ncols), dtype=dtype)
        f.seek(0)
        for i, line in enumerate(f):
            out[i] = line.split(delimiter)
    return out
    
#x = np.linspace(0, 100, 4998)
    
v500_noblock = np.genfromtxt('v_500_noblock-2.txt', delimiter = ',')
v500_block = np.genfromtxt('v_500_block-2.txt', delimiter = ',')

v10_noblock = np.genfromtxt('v_10_noblock-2.txt', delimiter = ',')
v10_block = np.genfromtxt('v_10_block-2.txt', delimiter = ',')

x_500 = np.genfromtxt('x_500_block.txt', delimiter = ',')
x_10 = np.genfromtxt('x_10_block.txt', delimiter = ',')
n500 = 25458
n10 = 27293

plt.plot(x_500/1000, v500_noblock, lw = 3)
plt.plot(x_500/1000, v500_block, lw = 3, linestyle = '--')
plt.xlim(0, 100)
#lt.savefig('6a.png', dpi = 600, bbox_inches = 'tight')

plt.show()

plt.plot(x_10/1000, v10_noblock, lw = 3)
plt.plot(x_10/1000, v10_block, lw = 3, linestyle = '--')
plt.xlim(0, 100)
#plt.savefig('6b.png', dpi = 600, bbox_inches = 'tight')

plt.show()

#x1 = np.linspace(0, 5000/193, 4998)
x_500_half = x_500/3960
plt.plot(x_500_half, v500_noblock, lw = 3)
plt.plot(x_500_half, v500_block, lw = 3, linestyle = '--')
plt.xlim(0, 25)
#plt.savefig('6c.png', dpi = 600, bbox_inches = 'tight')
plt.show()

x_10_half = x_10/560

plt.plot(x_10_half, v10_noblock, lw = 3)
plt.plot(x_10_half, v10_block, lw = 3, linestyle = '--')
plt.xlim(77, 102)
#plt.savefig('6d.png', dpi = 600, bbox_inches = 'tight')
plt.show()

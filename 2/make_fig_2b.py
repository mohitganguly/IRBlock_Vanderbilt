from __future__ import division
#from neuron import h
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.collections as mcoll
import matplotlib.path as mpath
import matplotlib.cm as cm
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm



temp_x=np.genfromtxt('temp_x.csv',delimiter=',')

#frame  plt.gca()
plt.xticks([])
plt.yticks([])

plt.plot(range(3750),temp_x[:3750], lw = 3, color = 'k')
plt.plot(range(3751,7499),temp_x[3751:7499], lw = 3, color = 'k')

plt.xlim(0, 7499)
plt.ylim(0, 30)

#plt.savefig('temp_x.png', dpi = 600, format = 'png', bbox_inches = 'tight')
plt.show()

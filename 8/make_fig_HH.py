from __future__ import division

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

diam = [1,10,100, 300, 500]
diam_32 = np.power(diam, 1.5)

stim = [0.19,5.9,190,990, 2060]


plt.plot(diam_32, stim, 'o', lw = 3)

m, c = np.polyfit(diam_32, stim, 1)
plt.plot(diam_32, m * diam_32 + c, color = 'k', lw = 3)

plt.xlim(-400, 11500)
plt.ylim(-400, 2100)

plt.savefig('8e.jpeg', format = 'jpeg', dpi = 600, bbox_inches = 'tight')
plt.show()



temp = [27.1,27.4,28.3,28.7,29.1]
diam_05 = np.power(diam, 0.5)

plt.plot(diam_05, temp, 'o', lw = 3)
m, c = np.polyfit(diam_05, temp, 1)
plt.plot(diam_05, m * diam_05 + c, color = 'k', lw = 3)

plt.xlim(-0.4, 24)
plt.ylim(27,29.5)

plt.savefig('8f.jpeg', format = 'jpeg', dpi = 600, bbox_inches = 'tight')
plt.show()

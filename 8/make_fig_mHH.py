from __future__ import division

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

diam = [1, 10, 100, 300, 500]
diam_32 = np.power(diam, 1.5)

stim = [0.79, 24,750,3870, 8100]


plt.plot(diam_32, stim, 'o', lw = 3)

m, c = np.polyfit(diam_32, stim, 1)
plt.plot(diam_32, m * diam_32 + c, color = 'k', lw = 3)

plt.xlim(-400, 11500)
plt.ylim(-500, 8500)

plt.savefig('8b.jpeg', format = 'jpeg', dpi = 600, bbox_inches = 'tight')
plt.show()



temp = [10.2,10.8,12.7,14.3,15.5]
diam_05 = np.power(diam, 0.5)

plt.plot(diam_05, temp, 'o', lw = 3)
m, c = np.polyfit(diam_05, temp, 1)
plt.plot(diam_05, m * diam_05 + c, color = 'k', lw = 3)

plt.xlim(0.5, 24)
plt.ylim(10, 16)

plt.savefig('8c.jpeg', format = 'jpeg', dpi = 600, bbox_inches = 'tight')
plt.show()

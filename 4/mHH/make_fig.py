from __future__ import division

import numpy as np
import matplotlib
import matplotlib.pyplot as plt


temp = [25,26,27,28,29,29.5]

pas = [17575,17575,17575,17575,17575,17575]
na_only = [7275,7250,7225,7200,7175,7150]
k_only = [1070,980,930,910,900,875]
norm = [1300,1100,1030,950,925,900]


plt.plot(temp, pas, '-o', lw = 2)
plt.plot(temp, na_only, '-o', lw = 2)
plt.plot(temp, k_only, '-o', lw = 2)
plt.plot(temp, norm, '-o', lw = 2)

plt.xlim(24.5,29.95)
plt.ylim(0, 18000)

#plt.xticks([])
#plt.yticks([])

#plt.savefig('mHH_noclamp.png', format = 'png', dpi = 600, bbox_inches = 'tight')
plt.show()


pas_clamp = [13550,13550,13550,13550,13550,13550]
na_only_clamp = [7575,7250,7225,7200,7175,7150]
k_only_clamp = [1020,940,890,880,870,850]
#norm = [1300,1100,1030,950,925,900]


plt.plot(temp, pas_clamp, '-o', lw = 2)
#plt.plot(temp, na_only_clamp, '-o', lw = 2)
plt.plot(temp, k_only_clamp, '-o', lw = 2, color = 'indianred')
plt.plot(temp, norm, '--', lw = 2, color = 'k')

plt.xlim(24.5,29.95)
plt.ylim(0, 18000)

#plt.xticks([])
#plt.yticks([])

#plt.savefig('mHH_clamp.png', format = 'png', dpi = 600, bbox_inches = 'tight')
plt.show()

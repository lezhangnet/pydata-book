# run the following in "ipython --pylab"
# the plot doesn't show with either "python x.py" or "python"

# manual fig and subplot creation
import matplotlib.pyplot as plt
fig = plt.figure() # the empty container
ax1 = fig.add_subplot(2, 2, 1) # 2 x 2, slot 1
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)

import numpy as np # not necessary in ipython
from numpy.random import randn
plt.plot(randn(50).cumsum(), 'k--') # plot on the last subplot we touched
# line style: black dash
_ = ax1.hist(randn(100), bins=20, color='k', alpha=0.3)
ax2.scatter(np.arange(30), np.arange(30) + 3 * randn(30))

plt.close('all')

# auto plot - hiding fig and subplot creation
plot([1.5, 3.5, -2, 1.6]) # showing Undefined error in VSCode
plt.plot([1.5, 3.5, -2, 1.6]) # same as above

# auto fig and subplot creation
fig, axes = plt.subplots(2, 3) # 2 (rows) x 3 (columns)
axes
# array([[<AxesSubplot:>, <AxesSubplot:>, <AxesSubplot:>],
#        [<AxesSubplot:>, <AxesSubplot:>, <AxesSubplot:>]], dtype=object)
axes[0,1].plot(randn(50).cumsum(), 'k--')
# plot on 1st row, 2nd column subplot

# adjusting spacing
fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)
for i in range(2):
    for j in range(2):
        axes[i, j].hist(randn(500), bins=50, color='k', alpha=0.5)
plt.subplots_adjust(wspace=0, hspace=0)

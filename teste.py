# libraries
import matplotlib.pyplot as plt
import numpy as np
 
# create data
x = np.linspace(-100,100, 1000)
y =  np.linspace(-100,100, 1000)
 
# Big bins
plt.hist2d(x, y, bins=(50, 50), cmap=plt.cm.jet)
#plt.show()
 
# Small bins
plt.hist2d(x, y, bins=(300, 300), cmap=plt.cm.jet)
plt.show()
 
# If you do not set the same values for X and Y, the bins aren't square !
plt.hist2d(x, y, bins=(300, 30), cmap=plt.cm.jet)
 
#plt.show()

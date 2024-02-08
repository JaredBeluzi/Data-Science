import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# generate data
x = np.linspace(0,5,101) # 0, 0.05, 0.1, ..., 4.95, 5
y_11 = x**2
y_12 = x**3
y_21 = sin(x)
y_22 = cos(x)
y_31 = x/2
y_32 = 1/x

# create 6 plots in grid with 3 rows and 2 columns
# first row
plt.subplot(3,2,1)
plt.plot(x,y_11, 'r-')
plt.subplot(3,2,2)
plt.plot(x,y_12, 'b.')

# second row
plt.subplot(3,2,3)
plt.plot(x,y_21, 'g.-')
plt.subplot(3,2,4)
plt.plot(x,y_22, 'o-')

# third row
plt.subplot(3,2,5)
plt.plot(x,y_31, '--')
plt.subplot(3,2,6)
plt.plot(x,y_32, 'g-.')

plt.show()

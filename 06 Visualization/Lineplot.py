import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# generate data
x = np.linspace(0,5,101) # 0, 0.05, 0.1, ..., 4.95, 5
y1 = x**2
y2 = np.sin(x)

# plot
plt.plot(x, y1, 'r-', label='f(x)=x^2')
plt.plot(x, y2, 'r-', label='f(x)=sin(x)')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend(loc='upper right')
plt.show()

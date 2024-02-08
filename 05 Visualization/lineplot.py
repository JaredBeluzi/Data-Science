import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11) # 0, 0.5, 1, ..., 4.5, 5
y1 = x**2
y2 = np.sin(x)
plt.plot(x, y1, 'r-', label='f(x)=x^2')
plt.plot(x, y2, 'r-', label='f(x)=sin(x)')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend(loc='upper right')
plt.show()

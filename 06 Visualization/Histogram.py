import numpy as np
import matplotlib.pyplot as plt

# generate data
x = np.random.normal(170, 10, 250)

# plot
plt.hist(x)

import matplotlib.pyplot as plt
import numpy as np

# generate data
x = [np.random.normal(100, std, 200) for std in range(1,4)]

# plot
plt.boxplot(x, vert=True, patch_artist=True)
plt.show()

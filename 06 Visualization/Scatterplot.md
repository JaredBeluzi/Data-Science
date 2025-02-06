# Code
```
import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(5.0, 1.0, 1000)
y = np.random.normal(10.0, 2.0, 1000)

# plot
plt.figure(figsize=(14, 6))
plt.scatter(x, y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()
```
# Ergebnis
![Scatterplot](https://github.com/JaredBeluzi/Data-Science/blob/main/Bilder/Scatterplot.png)

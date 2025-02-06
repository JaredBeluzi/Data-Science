Code
```
import numpy as np
import matplotlib.pyplot as plt

# generate data
x = np.random.normal(170, 10, 250)

# plot
plt.figure(figsize=(14, 6))
plt.hist(x)
```
Ergebnis
![Histogramm](Bilder/Histogramm.png)

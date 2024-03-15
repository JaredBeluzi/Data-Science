import matplotlib.pyplot as plt
import numpy as np
#from matplotlib.dates import DateFormatter

# generate data
x = np.linspace(0,5,101) # 0, 0.05, 0.1, ..., 4.95, 5
y1 = x**2
y2 = np.sin(x)

# plot
plt.figure(figsize=(14, 6))
plt.plot(x, y1, 'r-', label='f(x)=x^2') # ex. separate index and values
plt.plot(df.index, df['Betrag'], 'g-', label='Betrag') # ex. DataFrame
plt.title('Example Plots')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.ticklabel_format(axis='y', style='plain') # removes scientific notation of y-ticks

# show all x-ticks
#plt.xticks(df.index) # show all x-ticks
#plt.xticks(rotation=45) # make more space for x-ticks

# Set x-axis ticks to show year and month only
#date_format = DateFormatter('%Y-%m')
#plt.gca().xaxis.set_major_formatter(date_format)

plt.legend(loc='upper right', fontsize='large')
plt.show()

import seaborn as sb
import pandas as pd

# output as list
df.isnull().sum()/df.shape[0]*100

# visualization
sb.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap='viridis')

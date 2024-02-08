import seaborn as sb
import pandas as pd

# output as list
df.isnull().sum()/df.shape[0]*100

# visualization
sb.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap='viridis')

# drop useless cols
df.drop(['col1', 'col2'],axis=1,inplace=True)

# drop rows with missing data
df.dropna(inplace=True)

# if you need the cols or rows, you should impute the missing data with realistic fake data

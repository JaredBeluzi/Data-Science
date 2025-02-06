import pandas as pd

# csv to DataFrame
df = pd.read_csv('path\filename.csv')

# DataFrame to csv
df.to_csv('path\filename.csv' encoding='utf-8', index=False)

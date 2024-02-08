import seaborn as sb

sb.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap='viridis')

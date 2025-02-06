df[['col1', 'col2']]  # Spalten filtern
df[df['col1'] > 10]  # Zeilen filtern
df[(df['col1'] > 10) & (df['col2'] == 'A')] # Zeilen filtern mit mehrern Kriterien

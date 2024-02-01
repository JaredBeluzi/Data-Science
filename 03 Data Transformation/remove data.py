# remove cols
df.drop(['col1', 
         'col2', 
         'col3'], axis=1, inplace=True)

# remove after date
cutoff_date = datetime.date(2023, 12, 25)
df = df.truncate(after=cutoff_date, copy=False)

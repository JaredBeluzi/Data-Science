# transform df to x, y
y = df['target_col'].values
n = y.size
x = np.linspace(1, n, n) # creates 1, 2, ..., n

# fit model
model = np.poly1d(np.polyfit(x, y, 4)) # polynom with degree <=4

# make predictions
x_poly = np.linspace(1, n+52, n+52) # creates 1, 2, ..., n+52
y_ploy = model(x_poly)

# plot results
plt.figure(figsize=(14,5))
plt.plot(x, y, label='data')
plt.plot(x_poly, y_poly, label='prediction')
plt.legend()
plt.show()

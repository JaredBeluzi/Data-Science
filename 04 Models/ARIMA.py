# 1. Prepare Data

# set frequency of df
df = df.asfreq('w-mon') # set freq of index of dataframe to weekly and each week starts with monday

# remove trend of df
df_diff = df - df.shift(1) # look at this time series instead of df

# 2 Analyse Data

# Seasonal decomposition
from statsmodels.tsa.seasonal import seasonal_decompose
decomp = seasonal_decompose(df_temp, model='additive', period=52)
decomp.plot()
plt.show()
# If there is a trend, get rid of it, e.g. by looking at the differential time series instead
# If there is a big enough seasonality, use SARIMA instead of ARIMA
# If there is a pattern in the residuals, then analyse the data further. You want the residuals to be random and normal distributed.

# Correlation plots
# If you don't see any Autocorrelation or Partial Autocorrelation, ARIMA is not the method to use on that data.

# Autocorrelation
plot_acf(df_temp, lags=60)
plt.show()
# if you see spikes in this diagram, you should include the corresponding terms in the MA part of ARIMA

# Partial Autocorrelation
plot_pacf(df_temp, lags=60)
plt.show()
# if you see spikes in this diagram, you should include the corresponding terms in the AR part of ARIMA

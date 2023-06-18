# How can I use Python and SciPy to implement an ARIMA model?
// plain

Python and SciPy can be used to implement an ARIMA model. ARIMA stands for Autoregressive Integrated Moving Average and is a popular statistical model for time series forecasting.

## Example code

```
from statsmodels.tsa.arima_model import ARIMA

# fit model
model = ARIMA(ts_data, order=(2,1,0))
model_fit = model.fit(disp=0)

# make prediction
yhat = model_fit.predict()
```

The code above fits the ARIMA model to the time series data in ts_data using an autoregressive order of 2, a differencing order of 1, and a moving average order of 0. The model is then used to make a prediction, which is stored in the variable yhat.

The list below contains parts of the code and a brief explanation of each part:

* `from statsmodels.tsa.arima_model import ARIMA` - imports the ARIMA model from the statsmodels library
* `model = ARIMA(ts_data, order=(2,1,0))` - creates an ARIMA model object with the time series data and the specified order
* `model_fit = model.fit(disp=0)` - fits the model to the data
* `yhat = model_fit.predict()` - makes a prediction using the fitted model

## Helpful links

* [Statsmodels ARIMA Documentation](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima_model.ARIMA.html)
* [Time Series Forecasting with Python](https://towardsdatascience.com/time-series-forecasting-with-python-f19d2b7a2d6a)

onelinerhub: [How can I use Python and SciPy to implement an ARIMA model?](https://onelinerhub.com/python-scipy/how-can-i-use-python-and-scipy-to-implement-an-arima-model)
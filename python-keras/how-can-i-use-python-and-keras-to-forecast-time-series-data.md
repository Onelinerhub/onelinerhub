# How can I use Python and Keras to forecast time series data?
// plain

Using Python and Keras to forecast time series data is a powerful combination of two popular tools for data science. To do this, you will need to use the Keras API to create a model that will take in the time series data and output a prediction.

## Example code

```
import numpy as np
from keras.models import Sequential
from keras.layers import Dense

# Create a model
model = Sequential()
model.add(Dense(32, activation='relu', input_dim=1))
model.add(Dense(1))
model.compile(optimizer='rmsprop', loss='mse')

# Train the model
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
model.fit(X, y, epochs=50, batch_size=1)

# Make a prediction
prediction = model.predict(np.array([11]))
print(prediction)
```
## Output example

```
[[11.000814]]
```

The code above builds a simple model that takes in a single input and predicts the next value in the series. It uses the Keras API to create a Sequential model with two Dense layers. The model is then compiled using the RMSprop optimizer and mean squared error (MSE) loss function. Finally, the model is trained using the given data and the prediction is made on the next value in the series.

## Code explanation


1. `import numpy as np` - imports the NumPy library to use for data manipulation.
2. `from keras.models import Sequential` - imports the Sequential model from Keras for creating the model.
3. `model = Sequential()` - creates a Sequential model object.
4. `model.add(Dense(32, activation='relu', input_dim=1))` - adds a Dense layer to the model with 32 neurons, a ReLU activation function, and an input dimension of 1.
5. `model.add(Dense(1))` - adds a Dense layer to the model with one neuron.
6. `model.compile(optimizer='rmsprop', loss='mse')` - compiles the model with the RMSprop optimizer and mean squared error (MSE) loss function.
7. `model.fit(X, y, epochs=50, batch_size=1)` - trains the model with the given data for 50 epochs and a batch size of 1.
8. `prediction = model.predict(np.array([11]))` - makes a prediction on the next value in the series.
9. `print(prediction)` - prints the prediction.

## Helpful links
- [Keras Documentation](https://keras.io/api/)
- [Time Series Forecasting with Keras](https://machinelearningmastery.com/time-series-forecasting-with-deep-learning-in-python-with-keras/)

onelinerhub: [How can I use Python and Keras to forecast time series data?](https://onelinerhub.com/python-keras/how-can-i-use-python-and-keras-to-forecast-time-series-data)
# How can I use Python Keras to create a neural network with zero hidden layers?
// plain

Using Python Keras to create a neural network with zero hidden layers is possible by creating a model with a single layer that has the same number of neurons as the input and output layers. The following example code creates a model with three inputs and one output.

```
from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
model.add(Dense(1, input_dim=3))
model.compile(optimizer='sgd', loss='mean_squared_error', metrics=['accuracy'])
```

## Code explanation


1. `from keras.models import Sequential` - imports the Sequential model from the Keras library.
2. `from keras.layers import Dense` - imports the Dense layer from the Keras library.
3. `model = Sequential()` - creates a new Sequential model.
4. `model.add(Dense(1, input_dim=3))` - adds a single Dense layer to the model with three inputs and one output.
5. `model.compile(optimizer='sgd', loss='mean_squared_error', metrics=['accuracy'])` - compiles the model with the stochastic gradient descent optimizer, mean squared error loss function, and accuracy metric.

## Helpful links

- [Keras Documentation](https://keras.io/getting-started/sequential-model-guide/)
- [Keras Dense Layer Documentation](https://keras.io/layers/core/#dense)

onelinerhub: [How can I use Python Keras to create a neural network with zero hidden layers?](https://onelinerhub.com/python-keras/how-can-i-use-python-keras-to-create-a-neural-network-with-zero-hidden-layers)
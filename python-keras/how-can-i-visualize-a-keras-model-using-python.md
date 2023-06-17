# How can I visualize a Keras model using Python?
// plain

Visualizing a Keras model using Python is a powerful way to understand the inner workings of a model. To do this, you must first create a model with a summary() function. The summary() function will provide a visualization of the model's layers, weights, and connections.

## Example code

```
from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
model.add(Dense(units=64, activation='relu', input_dim=32))
model.add(Dense(units=2, activation='softmax'))

model.summary()
```

## Output example

```
Model: "sequential_1"
_________________________________________________________________
Layer (type)                 Output Shape              Param #
=================================================================
dense_1 (Dense)              (None, 64)                2080
_________________________________________________________________
dense_2 (Dense)              (None, 2)                 130
=================================================================
Total params: 2,210
Trainable params: 2,210
Non-trainable params: 0
_________________________________________________________________
```

## Code explanation


1. `from keras.models import Sequential` - imports the Sequential model from the Keras library.
2. `from keras.layers import Dense` - imports the Dense layer from the Keras library.
3. `model = Sequential()` - creates a Sequential model object.
4. `model.add(Dense(units=64, activation='relu', input_dim=32))` - adds a Dense layer with 64 units, ReLU activation, and 32 input dimensions to the model.
5. `model.add(Dense(units=2, activation='softmax'))` - adds a Dense layer with 2 units and softmax activation to the model.
6. `model.summary()` - prints a summary of the model's layers, weights, and connections.

## Helpful links

- [Keras Documentation](https://keras.io/getting-started/sequential-model-guide/)
- [Visualizing Neural Network](https://towardsdatascience.com/visualizing-neural-network-architectures-with-python-and-matplotlib-f73a847f2a66)

onelinerhub: [How can I visualize a Keras model using Python?](https://onelinerhub.com/python-keras/how-can-i-visualize-a-keras-model-using-python)
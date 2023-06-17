# How do I create a sequential model in Python using Keras?
// plain

Creating a sequential model in Python using Keras is a simple process.

First, you must import the necessary Keras libraries:
```
from keras.models import Sequential
from keras.layers import Dense
```

Next, you must create an instance of the Sequential model:
```
model = Sequential()
```

You can then add layers to the model:
```
model.add(Dense(units=64, activation='relu', input_dim=100))
model.add(Dense(units=10, activation='softmax'))
```

You must then compile the model, specifying the optimizer and loss function:
```
model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])
```

Finally, you can train the model:
```
model.fit(x_train, y_train, epochs=5, batch_size=32)
```

## Code explanation


1. `from keras.models import Sequential` - This imports the Sequential model from the Keras library.
2. `from keras.layers import Dense` - This imports the Dense layer from the Keras library.
3. `model = Sequential()` - This creates an instance of the Sequential model.
4. `model.add(Dense(units=64, activation='relu', input_dim=100))` - This adds a Dense layer with 64 units, a ReLU activation function, and an input dimension of 100.
5. `model.add(Dense(units=10, activation='softmax'))` - This adds a Dense layer with 10 units and a Softmax activation function.
6. `model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])` - This compiles the model, specifying the loss function, optimizer, and metrics.
7. `model.fit(x_train, y_train, epochs=5, batch_size=32)` - This trains the model on the training data for 5 epochs with a batch size of 32.

## Helpful links

- [Keras Documentation](https://keras.io/)
- [Keras Sequential Model Guide](https://keras.io/getting-started/sequential-model-guide/)

onelinerhub: [How do I create a sequential model in Python using Keras?](https://onelinerhub.com/python-keras/how-do-i-create-a-sequential-model-in-python-using-keras)
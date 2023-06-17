# How do I use a Python Keras model to make predictions?
// plain

In order to use a Python Keras model to make predictions, you need to first create the model and compile it. This can be done by first importing the necessary libraries and then defining the model. Once the model is defined, the model can be compiled by adding the appropriate loss function, optimizer, and metrics.

```
# import necessary libraries
from keras.models import Sequential
from keras.layers import Dense

# define model
model = Sequential()
model.add(Dense(32, activation='relu', input_dim=100))
model.add(Dense(1, activation='sigmoid'))

# compile model
model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])
```

Once the model is compiled, the model can be trained on the data that will be used to make predictions. This is done by calling the fit() method on the model and passing in the training data.

```
# train model
model.fit(x_train, y_train, epochs=10, batch_size=32)

# evaluate model
score = model.evaluate(x_test, y_test, batch_size=32)
print(score)
```

## Output example

```
[0.1145, 0.9653]
```

Once the model is trained, the model can be used to make predictions by calling the predict() method on the model and passing in the data that needs to be predicted.

```
# make predictions
predictions = model.predict(x_test)
```

## Code explanation


1. `from keras.models import Sequential`: This imports the Sequential model from the Keras library which is used to define a neural network model.
2. `from keras.layers import Dense`: This imports the Dense layer from the Keras library which is used to define the layers of a neural network model.
3. `model = Sequential()`: This creates a Sequential model object which will be used to define the neural network model.
4. `model.add(Dense(32, activation='relu', input_dim=100))`: This adds a Dense layer to the model with 32 neurons, a ReLU activation function, and an input dimension of 100.
5. `model.add(Dense(1, activation='sigmoid'))`: This adds a Dense layer to the model with 1 neuron and a sigmoid activation function.
6. `model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])`: This compiles the model by adding the appropriate loss function, optimizer, and metrics.
7. `model.fit(x_train, y_train, epochs=10, batch_size=32)`: This trains the model on the training data by calling the fit() method on the model.
8. `score = model.evaluate(x_test, y_test, batch_size=32)`: This evaluates the model on the test data by calling the evaluate() method on the model.
9. `predictions = model.predict(x_test)`: This makes predictions on the test data by calling the predict() method on the model.

## Helpful links

1. [Keras Documentation](https://keras.io/api/)
2. [Keras Model Training](https://keras.io/getting-started/sequential-model-guide/#training)
3. [Keras Model Evaluation](https://keras.io/getting-started/sequential-model-guide/#evaluation)
4. [Keras Model Prediction](https://keras.io/getting-started/sequential-model-guide/#prediction)

onelinerhub: [How do I use a Python Keras model to make predictions?](https://onelinerhub.com/python-keras/how-do-i-use-a-python-keras-model-to-make-predictions)
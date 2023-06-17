# How do I create a Python Keras example?
// plain

Creating a Python Keras example is relatively straightforward. The following is an example of a basic Keras model:

```python
# import necessary libraries
import keras
from keras.models import Sequential
from keras.layers import Dense

# create model
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# fit model
model.fit(X, y, epochs=150, batch_size=10)

# evaluate model
scores = model.evaluate(X, y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
```

The output would be something like the following:

```
accuracy: 98.00%
```

This code is broken down into the following parts:

1. Import necessary libraries: This imports the necessary libraries for creating a Keras model, including the Sequential and Dense layers.
2. Create model: This creates the model object and adds the layers to it.
3. Compile model: This compiles the model with the appropriate loss and optimizer functions.
4. Fit model: This fits the model to the data with the given batch size and number of epochs.
5. Evaluate model: This evaluates the model on the data and prints out the accuracy.

For more information on creating Keras models, please see the following resources:

* [Keras Documentation](https://keras.io/)
* [Keras Tutorials](https://keras.io/examples/)
* [Keras API Reference](https://keras.io/api/)

onelinerhub: [How do I create a Python Keras example?](https://onelinerhub.com/python-keras/how-do-i-create-a-python-keras-example)
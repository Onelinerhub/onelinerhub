# How can I use Keras with Python to run computations on the CPU?
// plain

Keras is a high-level neural networks API, written in Python and capable of running on top of TensorFlow, CNTK, or Theano. It was developed with a focus on enabling fast experimentation.

Using Keras with Python to run computations on the CPU is straightforward. All you need to do is install the required packages, set up the environment variables, and then import the required libraries.

For example, the following code will import the necessary packages and set up the environment variables for Keras and TensorFlow:

```
import os
import keras

os.environ['KERAS_BACKEND'] = 'tensorflow'
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
```

Then, you can use Keras API to create and compile a model, and run computations on the CPU as follows:

```
from keras.models import Sequential
from keras.layers import Dense

# Create model
model = Sequential()
model.add(Dense(units=64, activation='relu', input_dim=100))
model.add(Dense(units=10, activation='softmax'))

# Compile model
model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])

# Run computation
model.fit(x_train, y_train, epochs=5, batch_size=32)
```

## Output example

```
Epoch 1/5
60000/60000 [==============================] - 2s 33us/step - loss: 0.7125 - accuracy: 0.7662
Epoch 2/5
60000/60000 [==============================] - 2s 32us/step - loss: 0.3782 - accuracy: 0.8918
Epoch 3/5
60000/60000 [==============================] - 2s 34us/step - loss: 0.3175 - accuracy: 0.9077
Epoch 4/5
60000/60000 [==============================] - 2s 33us/step - loss: 0.2843 - accuracy: 0.9166
Epoch 5/5
60000/60000 [==============================] - 2s 33us/step - loss: 0.2578 - accuracy: 0.9239
```

## Code explanation


1. `import os`: imports the `os` module which provides functions for interacting with the operating system.
2. `import keras`: imports the `keras` module which provides access to the Keras API.
3. `os.environ['KERAS_BACKEND'] = 'tensorflow'`: sets the environment variable `KERAS_BACKEND` to `tensorflow`, which tells Keras to use TensorFlow as its backend engine.
4. `os.environ['TF_CPP_MIN_LOG_LEVEL']='2'`: sets the environment variable `TF_CPP_MIN_LOG_LEVEL` to `2`, which tells TensorFlow to suppress all log messages other than errors.
5. `from keras.models import Sequential`: imports the `Sequential` class from the `keras.models` module, which is used to create a linear stack of layers.
6. `from keras.layers import Dense`: imports the `Dense` class from the `keras.layers` module, which is used to create densely-connected layers.
7. `model.add(Dense(units=64, activation='relu', input_dim=100))`: adds a densely-connected layer with 64 units, ReLU activation, and an input dimension of 100.
8. `model.add(Dense(units=10, activation='softmax'))`: adds a densely-connected layer with 10 units and a softmax activation.
9. `model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])`: compiles the model with categorical cross-entropy loss, SGD optimizer, and accuracy metrics.
10. `model.fit(x_train, y_train, epochs=5, batch_size=32)`: runs the computations on the CPU by training the model on the training data for 5 epochs with a batch size of 32.

## Helpful links

- [Keras Documentation](https://keras.io/)
- [TensorFlow Documentation](https://www.tensorflow.org/api_docs)

onelinerhub: [How can I use Keras with Python to run computations on the CPU?](https://onelinerhub.com/python-keras/how-can-i-use-keras-with-python-to-run-computations-on-the-cpu)
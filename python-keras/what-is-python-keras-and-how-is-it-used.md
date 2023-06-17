# What is Python Keras and how is it used?
// plain

Python Keras is a high-level neural networks API, written in Python and capable of running on top of TensorFlow, CNTK, or Theano. It was developed with a focus on enabling fast experimentation. It allows for easy and fast prototyping, supports both convolutional networks and recurrent networks, and runs seamlessly on CPU and GPU.

Keras is used to build deep learning models. It is a high-level API that can be used to quickly build and train deep learning models. It supports both convolutional and recurrent networks and can run on both CPUs and GPUs. It also supports a wide range of different types of layers, including convolutional, pooling, and recurrent layers.

## Example code


```
from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
model.add(Dense(units=64, activation='relu', input_dim=100))
model.add(Dense(units=10, activation='softmax'))
model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])
model.fit(x_train, y_train, epochs=5, batch_size=32)
```

This code creates a simple neural network with two layers. The first layer is a densely connected layer with 64 units, a ReLU activation function, and an input dimension of 100. The second layer is a densely connected layer with 10 units and a softmax activation function. The model is then compiled using the categorical cross-entropy loss function, the SGD optimizer, and accuracy as the metric. Finally, the model is fit to the training data for five epochs with a batch size of 32.

## Code explanation

- `from keras.models import Sequential`: imports the Sequential model from the Keras library
- `from keras.layers import Dense`: imports the Dense layer from the Keras library
- `model = Sequential()`: creates a Sequential model
- `model.add(Dense(units=64, activation='relu', input_dim=100))`: adds a densely connected layer with 64 units, a ReLU activation function, and an input dimension of 100
- `model.add(Dense(units=10, activation='softmax'))`: adds a densely connected layer with 10 units and a softmax activation function
- `model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])`: compiles the model using the categorical cross-entropy loss function, the SGD optimizer, and accuracy as the metric
- `model.fit(x_train, y_train, epochs=5, batch_size=32)`: fits the model to the training data for five epochs with a batch size of 32

## Helpful links
- [Keras Documentation](https://keras.io/)
- [Keras Tutorials](https://keras.io/tutorials/)
- [Keras Examples](https://keras.io/examples/)

onelinerhub: [What is Python Keras and how is it used?](https://onelinerhub.com/python-keras/what-is-python-keras-and-how-is-it-used)
# How do I build a neural network using Python and Keras?
// plain

To build a neural network using Python and Keras, you will need to install Keras and its dependencies. After installation, you can use the following code to create a simple neural network:

```
# import necessary packages
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
model.fit(X, Y, epochs=150, batch_size=10)

# evaluate model
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
```

This code creates a neural network with three layers; an input layer with 8 nodes, a hidden layer with 12 nodes, and an output layer with 1 node. The model is then compiled with a binary cross entropy loss function and an Adam optimizer, and is fit on the data with 150 epochs and a batch size of 10. Finally, the model is evaluated on the data and the accuracy is printed.

Parts of the code:
- `from keras.models import Sequential`: This imports the Sequential model from the Keras library, which is used to create a linear stack of layers.
- `model.add(Dense(12, input_dim=8, activation='relu'))`: This adds a dense layer with 12 nodes and an input dimension of 8 to the model. The activation function used is the Rectified Linear Unit (ReLU).
- `model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])`: This compiles the model with a binary cross entropy loss function and an Adam optimizer.
- `model.fit(X, Y, epochs=150, batch_size=10)`: This fits the model on the data with 150 epochs and a batch size of 10.
- `scores = model.evaluate(X, Y)`: This evaluates the model on the data.
- `print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))`: This prints the accuracy of the model.

## Helpful links
- [Keras Documentation](https://keras.io/)
- [Neural Networks with Keras Tutorial](https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/)

onelinerhub: [How do I build a neural network using Python and Keras?](https://onelinerhub.com/python-keras/how-do-i-build-a-neural-network-using-python-and-keras)
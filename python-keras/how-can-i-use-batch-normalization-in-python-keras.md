# How can I use batch normalization in Python Keras?
// plain

Batch normalization is a technique used to normalize the input layer by adjusting and scaling the activations of the previous layer. It can be used to reduce overfitting and to speed up the training process of a deep neural network.

In Python Keras, batch normalization can be implemented by using the `BatchNormalization` layer. This layer takes an input shape and applies a transformation that maintains the mean output close to 0 and the standard deviation close to 1.

## Example code

```
model = Sequential()
model.add(Dense(64, input_shape=(32,)))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Dense(10))
model.add(Activation('softmax'))
```

The example code above creates a model with a `Dense` layer as the input layer, followed by a `BatchNormalization` layer, an `Activation` layer with `relu` as the activation function, another `Dense` layer as the output layer, and a final `Activation` layer with `softmax` as the activation function.

## Code explanation


- `model = Sequential()`: This line creates a Sequential model object.
- `model.add(Dense(64, input_shape=(32,)))`: This line adds a `Dense` layer with 64 units as the input layer.
- `model.add(BatchNormalization())`: This line adds a `BatchNormalization` layer which will normalize the input layer.
- `model.add(Activation('relu'))`: This line adds an `Activation` layer with `relu` as the activation function.
- `model.add(Dense(10))`: This line adds a `Dense` layer with 10 units as the output layer.
- `model.add(Activation('softmax'))`: This line adds an `Activation` layer with `softmax` as the activation function.

## Helpful links

- [Keras Documentation: Batch Normalization](https://keras.io/layers/normalization/)
- [TensorFlow Tutorial: Batch Normalization](https://www.tensorflow.org/guide/keras/train_and_evaluate#batch_normalization)

onelinerhub: [How can I use batch normalization in Python Keras?](https://onelinerhub.com/python-keras/how-can-i-use-batch-normalization-in-python-keras)
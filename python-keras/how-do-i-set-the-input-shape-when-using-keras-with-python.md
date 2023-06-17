# How do I set the input shape when using Keras with Python?
// plain

When using Keras with Python, the input shape of a model can be set when defining the model. For example, if defining a model with two input layers:

```
model = Sequential()
model.add(Dense(32, input_shape=(784,)))
model.add(Dense(32))
```

The `input_shape` argument of the first layer defines the shape of the input data. In this example, the shape is `(784,)`, which means the input is an array of 784 elements.

If a model has more than one input layer, the shape of each layer must be specified. For example:

```
model = Sequential()
model.add(Dense(32, input_shape=(784,)))
model.add(Dense(32, input_shape=(128,)))
```

The first layer has an input shape of `(784,)` and the second layer has an input shape of `(128,)`.

The `input_shape` argument can also be a tuple of integers, such as `(784, 1)`. This indicates that the input is an array of 784 elements, each element being an array of 1 element.

If the input data is an image, the shape of the input should include the number of channels (e.g. 3 for RGB images). For example:

```
model = Sequential()
model.add(Dense(32, input_shape=(128, 128, 3)))
```

The input shape is `(128, 128, 3)`, which indicates that the input is an array of 128x128 pixels, with 3 channels (RGB).

For more information, see the [Keras documentation](https://keras.io/getting-started/sequential-model-guide/).

onelinerhub: [How do I set the input shape when using Keras with Python?](https://onelinerhub.com/python-keras/how-do-i-set-the-input-shape-when-using-keras-with-python)
# How do I use Python Keras to create an input layer?
// plain

Using Python Keras to create an input layer is a relatively straightforward task. To begin, you need to import the layers module from the Keras library.

```
from keras.layers import Input
```

Next, you need to define the shape of the input layer. This is done by passing a tuple of integers to the `Input()` function, where each integer represents the number of neurons in the layer.

```
input_layer = Input(shape=(10,))
```

The above code creates an input layer with 10 neurons.

You can also specify additional parameters for the layer, such as the name of the layer, the type of data it should expect, and whether or not it should be trainable.

```
input_layer = Input(shape=(10,), name='my_input_layer', dtype='float32', trainable=True)
```

The above code creates an input layer with 10 neurons, named `my_input_layer`, that expects data of type `float32` and is trainable.

Finally, you can print the summary of the layer to verify that it was created correctly.

```
print(input_layer.summary())
```

## Output example

```
Model: "input_1"
_________________________________________________________________
Layer (type)                 Output Shape              Param #
=================================================================
my_input_layer (InputLayer)  (None, 10)                0
=================================================================
Total params: 0
Trainable params: 0
Non-trainable params: 0
_________________________________________________________________
```

The above code prints the summary of the layer, which shows the layer name, output shape, and number of parameters.

## Helpful links
- [Keras Documentation - Input Layers](https://keras.io/api/layers/input_layers/)
- [Keras Documentation - Input Layer Arguments](https://keras.io/api/layers/input_layers/#arguments)

onelinerhub: [How do I use Python Keras to create an input layer?](https://onelinerhub.com/python-keras/how-do-i-use-python-keras-to-create-an-input-layer)
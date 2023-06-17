# layer

How do I create a dense layer in Keras using Python?
// plain

A dense layer is a type of layer in a neural network that is used to compute the output of a given set of inputs. In Keras, a dense layer can be created using the `Dense` class. The following example code creates a dense layer with an input shape of 2 and an output shape of 3:

```
from keras.layers import Dense

dense_layer = Dense(3, input_shape=(2,))
```

The `Dense` class takes two arguments: the number of outputs (in this case, 3) and the input shape (in this case, 2). The output of this layer can then be used as input for another layer or for the model's output.

## Code explanation


* `from keras.layers import Dense`: This imports the `Dense` class from the `keras.layers` module.

* `Dense(3, input_shape=(2,))`: This creates an instance of the `Dense` class with an output shape of 3 and an input shape of 2.

* `dense_layer = Dense(3, input_shape=(2,))`: This assigns the instance of the `Dense` class to the `dense_layer` variable.

## Helpful links

* [Keras Documentation - Dense Layer](https://keras.io/api/layers/core_layers/dense/)

onelinerhub: [layer

How do I create a dense layer in Keras using Python?](https://onelinerhub.com/python-keras/layer--how-do-i-create-a-dense-layer-in-keras-using-python)
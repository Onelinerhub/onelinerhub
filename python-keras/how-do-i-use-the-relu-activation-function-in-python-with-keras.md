# How do I use the ReLU activation function in Python with Keras?
// plain

ReLU (Rectified Linear Unit) is a popular activation function used in neural networks. It is used to add non-linearity to the network and can be used with Keras in Python.

The following example code block shows how to use ReLU with Keras:

```
from keras.layers import Activation

model.add(Activation('relu'))
```

This code adds a ReLU activation layer to the model.

The parts of the code are as follows:

* `from keras.layers import Activation`: This imports the Activation class from the Keras library.

* `model.add(Activation('relu'))`: This adds an activation layer to the model. The string 'relu' is passed as an argument to specify the type of activation layer.

## Helpful links

* [Keras Documentation - Activation Layers](https://keras.io/api/layers/activations/)
* [Understanding Activation Functions in Neural Networks](https://towardsdatascience.com/activation-functions-neural-networks-1cbd9f8d91d6)

onelinerhub: [How do I use the ReLU activation function in Python with Keras?](https://onelinerhub.com/python-keras/how-do-i-use-the-relu-activation-function-in-python-with-keras)
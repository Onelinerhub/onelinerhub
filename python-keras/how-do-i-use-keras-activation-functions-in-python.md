# How do I use Keras activation functions in Python?
// plain

Keras provides a variety of activation functions that can be used in neural networks. Activation functions are used to introduce non-linearity into the network. In Python, you can use Keras activation functions by first importing the Keras library and then calling the activation function on a layer. For example:

```
from keras.layers import Activation

model.add(Activation('relu'))
```

This adds a ReLU activation function to the model. Other activation functions, such as sigmoid, tanh, softmax, etc., can be used in the same way.

The parts of the code are as follows:

1. `from keras.layers import Activation`: imports the Activation class from the Keras library.
2. `model.add(Activation('relu'))`: adds a ReLU activation function to the model.

## Helpful links

- [Keras Activation Functions](https://keras.io/activations/)
- [Understanding Activation Functions in Neural Networks](https://towardsdatascience.com/activation-functions-neural-networks-1cbd9f8d91d6)

onelinerhub: [How do I use Keras activation functions in Python?](https://onelinerhub.com/python-keras/how-do-i-use-keras-activation-functions-in-python)
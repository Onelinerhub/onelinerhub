# How do I use the Softmax activation function with Python and Keras?
// plain

The Softmax activation function can be used in Python and Keras to classify multiple classes of data. It is a generalization of the logistic sigmoid function that "squashes" a K-dimensional vector of arbitrary real values to a K-dimensional vector of real values in the range (0, 1) that add up to 1.

Example code using the Softmax activation function with Python and Keras is as follows:

```
import keras
from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
model.add(Dense(units=4, activation='softmax'))
```

The code above creates a Sequential model with a single Dense layer containing 4 units and a Softmax activation function.

The parts of the code are:

1. **import keras** - Imports the Keras library.
2. **from keras.models import Sequential** - Imports the Sequential model from the Keras library.
3. **from keras.layers import Dense** - Imports the Dense layer from the Keras library.
4. **model = Sequential()** - Creates a new Sequential model.
5. **model.add(Dense(units=4, activation='softmax'))** - Adds a Dense layer with 4 units and a Softmax activation function to the model.

## Helpful links

- [Keras documentation on Softmax activation](https://keras.io/activations/#softmax)
- [Towards Data Science article on Softmax activation](https://towardsdatascience.com/softmax-function-simplified-714068bf8156)

onelinerhub: [How do I use the Softmax activation function with Python and Keras?](https://onelinerhub.com/python-keras/how-do-i-use-the-softmax-activation-function-with-python-and-keras)
# How can I create an input layer in a Keras model using Python?
// plain

Creating an input layer in a Keras model using Python is a simple process.

First, you must import the necessary libraries, such as TensorFlow and Keras:
```
import tensorflow as tf
from tensorflow import keras
```

Next, you must define the shape of the input layer. This is done by creating a tuple with the desired dimensions:
```
input_shape = (28, 28)
```

After that, you must create the input layer itself. This is done by specifying the type of layer, the shape, and the input_shape:
```
input_layer = keras.layers.Input(shape=input_shape)
```

Finally, the input layer needs to be added to the model. This is done by specifying the layer to be added:
```
model.add(input_layer)
```

The following parts of code were used to create an input layer in a Keras model using Python:

1. `import tensorflow as tf`: Imports the TensorFlow library.
2. `from tensorflow import keras`: Imports the Keras library.
3. `input_shape = (28, 28)`: Defines the shape of the input layer.
4. `input_layer = keras.layers.Input(shape=input_shape)`: Creates the input layer.
5. `model.add(input_layer)`: Adds the input layer to the model.

## Helpful links
- [Keras Documentation](https://keras.io/getting-started/sequential-model-guide/)
- [TensorFlow Documentation](https://www.tensorflow.org/guide/keras/overview)

onelinerhub: [How can I create an input layer in a Keras model using Python?](https://onelinerhub.com/python-keras/how-can-i-create-an-input-layer-in-a-keras-model-using-python)
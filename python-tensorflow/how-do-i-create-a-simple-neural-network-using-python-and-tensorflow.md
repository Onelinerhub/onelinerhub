# How do I create a simple neural network using Python and TensorFlow?
// plain

Creating a simple neural network using Python and TensorFlow is relatively straightforward. To begin, you'll need to import the necessary packages:

```
import tensorflow as tf
import numpy as np
```

Next, you'll need to define the model's architecture. This can be done by creating layers of neurons, each of which will have an associated weight and bias value. The following example creates a single layer with three neurons:

```
model = tf.keras.Sequential([
    tf.keras.layers.Dense(3, activation='relu', input_shape=(1,))
])
```

Once the model architecture is defined, you'll need to compile it with an optimizer and a loss function. The following example uses the Adam optimizer and a mean squared error loss function:

```
model.compile(optimizer='adam',
              loss='mean_squared_error',
              metrics=['accuracy'])
```

Finally, you'll need to train the model on a set of data. The following example uses a NumPy array of data to train the model:

```
X = np.array([[1], [2], [3], [4]])
y = np.array([[2], [4], [6], [8]])
model.fit(X, y, epochs=1000)
```

The output of the above code should look something like this:

```
Epoch 1/1000
1/1 [==============================] - 0s 1ms/step - loss: 0.0013 - accuracy: 0.0000e+00
Epoch 1000/1000
1/1 [==============================] - 0s 2ms/step - loss: 2.9585e-05 - accuracy: 0.0000e+00
```

Once the model is trained, you can use it to make predictions on new data.

## Code explanation

- `import tensorflow as tf` - imports the TensorFlow library
- `import numpy as np` - imports the NumPy library
- `tf.keras.Sequential([])` - creates a model architecture with a single layer of neurons
- `tf.keras.layers.Dense(3, activation='relu', input_shape=(1,))` - creates a layer of three neurons with a rectified linear activation function and an input shape of 1
- `model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])` - compiles the model with an Adam optimizer and a mean squared error loss function
- `X = np.array([[1], [2], [3], [4]])` - creates a NumPy array with input data
- `y = np.array([[2], [4], [6], [8]])` - creates a NumPy array with output data
- `model.fit(X, y, epochs=1000)` - trains the model on the input and output data for 1000 epochs

## Helpful links
- [TensorFlow Documentation](https://www.tensorflow.org/docs)
- [Creating a Simple Neural Network in TensorFlow](https://www.tensorflow.org/tutorials/quickstart/beginner)

onelinerhub: [How do I create a simple neural network using Python and TensorFlow?](https://onelinerhub.com/python-tensorflow/how-do-i-create-a-simple-neural-network-using-python-and-tensorflow)
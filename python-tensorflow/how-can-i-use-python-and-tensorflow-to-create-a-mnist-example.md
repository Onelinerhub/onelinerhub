# How can I use Python and TensorFlow to create a MNIST example?
// plain

To use Python and TensorFlow to create a MNIST example, first install the necessary libraries and packages:

```
pip install tensorflow
pip install numpy
pip install matplotlib
```

Then, import the necessary libraries and packages into your Python script:

```
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
```

Next, load the MNIST data set and normalize it:

```
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)
```

After that, create the model architecture, compile it, and fit it to the training data:

```
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=3)
```

Finally, evaluate the model with the test data and print the results:

```
val_loss, val_acc = model.evaluate(x_test, y_test)
print(val_loss, val_acc)
```

```
0.09817703712594568 0.9714
```

## Code explanation


- `pip install tensorflow`: Installs the TensorFlow library.
- `pip install numpy`: Installs the NumPy library.
- `pip install matplotlib`: Installs the Matplotlib library.
- `import tensorflow as tf`: Imports the TensorFlow library into the script.
- `import numpy as np`: Imports the NumPy library into the script.
- `import matplotlib.pyplot as plt`: Imports the Matplotlib library into the script.
- `mnist = tf.keras.datasets.mnist`: Loads the MNIST data set.
- `(x_train, y_train), (x_test, y_test) = mnist.load_data()`: Splits the MNIST data set into training and test sets.
- `x_train = tf.keras.utils.normalize(x_train, axis=1)`: Normalizes the training data.
- `x_test = tf.keras.utils.normalize(x_test, axis=1)`: Normalizes the test data.
- `model = tf.keras.models.Sequential()`: Creates a sequential model.
- `model.add(tf.keras.layers.Flatten())`: Adds a flatten layer to the model.
- `model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))`: Adds a dense layer with 128 neurons and ReLU activation to the model.
- `model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))`: Adds a dense layer with 128 neurons and ReLU activation to the model.
- `model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))`: Adds a dense output layer with 10 neurons and softmax activation to the model.
- `model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])`: Compiles the model with the Adam optimizer, sparse categorical cross-entropy loss, and accuracy metric.
- `model.fit(x_train, y_train, epochs=3)`: Fits the model to the training data for 3 epochs.
- `val_loss, val_acc = model.evaluate(x_test, y_test)`: Evaluates the model with the test data.
- `print(val_loss, val_acc)`: Prints the loss and accuracy of the model.

#### ## Helpful links
- [TensorFlow Documentation](https://www.tensorflow.org/tutorials/quickstart/beginner)
- [NumPy Documentation](https://numpy.org/doc/stable/)
- [Matplotlib Documentation](https://matplotlib.org/3.2.1/contents.html)
- [MNIST Tutorial](https://www.tensorflow.org/tutorials/quickstart/beginner#mnist_dataset)

onelinerhub: [How can I use Python and TensorFlow to create a MNIST example?](https://onelinerhub.com/python-tensorflow/how-can-i-use-python-and-tensorflow-to-create-a-mnist-example)
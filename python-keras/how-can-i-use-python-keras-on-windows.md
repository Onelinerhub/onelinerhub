# How can I use Python Keras on Windows?
// plain

Python Keras can be used on Windows by installing TensorFlow, a deep learning library, as a backend for Keras. To install TensorFlow, open a command prompt and type `pip install tensorflow` or `pip install tensorflow-gpu` to install the GPU version.

Once TensorFlow has been installed, you can import it into your Python environment by typing `import tensorflow as tf`.

You can then use Keras to build neural networks by importing the `keras` module and then using the `Sequential` model to define the layers of your neural network. For example:

```
from keras.models import Sequential

model = Sequential()
model.add(Dense(128, activation='relu', input_shape=(784,)))
model.add(Dropout(0.2))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(10, activation='softmax'))
```

You can then compile the model using `model.compile()` and fit the model to the data using `model.fit()`.

To learn more about using Keras on Windows, check out the [Keras documentation](https://keras.io/getting-started/faq/#how-can-i-run-keras-on-gpu).

onelinerhub: [How can I use Python Keras on Windows?](https://onelinerhub.com/python-keras/how-can-i-use-python-keras-on-windows)
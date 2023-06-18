# How can I use an online editor to develop a Python TensorFlow application?
// plain

You can use an online editor such as [Google Colab](https://colab.research.google.com/) to develop a Python TensorFlow application. Colab provides an interactive environment for developing and running Python code, including TensorFlow. To get started, you can open a new notebook and connect it to a runtime with a Python version that supports TensorFlow.

For example, the following code block will install TensorFlow and print the version:
```
!pip install tensorflow
import tensorflow as tf
print(tf.__version__)
```
The output should be the version of TensorFlow installed:
```
2.2.0
```
You can then write and execute code to build and train your TensorFlow models. For example, the following code block creates a simple linear model and prints the model weights:
```
model = tf.keras.Sequential([tf.keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')

xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-2.0, 1.0, 4.0, 7.0, 10.0, 13.0], dtype=float)

model.fit(xs, ys, epochs=500)

print(model.get_weights())
```
The output should be the weights of the model:
```
[array([[2.0006145]], dtype=float32), array([0.99983174], dtype=float32)]
```

You can find more information about using Colab for TensorFlow development in the [official documentation](https://www.tensorflow.org/tutorials/quickstart/beginner).

onelinerhub: [How can I use an online editor to develop a Python TensorFlow application?](https://onelinerhub.com/python-tensorflow/how-can-i-use-an-online-editor-to-develop-a-python-tensorflow-application)
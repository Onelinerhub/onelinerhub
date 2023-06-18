# How can I use Python and TensorFlow to run computations on the CPU?
// plain

Python and TensorFlow can be used together to run computations on the CPU. To do this, first install the TensorFlow library:

```
pip install tensorflow
```

Then, create a TensorFlow constant and run an operation on it:

```
import tensorflow as tf

a = tf.constant(1.0)
b = tf.constant(2.0)
c = a + b

print(c)
```

## Output example

```
tf.Tensor(3.0, shape=(), dtype=float32)
```

The following parts are included in the code:
1. `import tensorflow as tf` imports the TensorFlow library.
2. `a = tf.constant(1.0)` and `b = tf.constant(2.0)` create two TensorFlow constants.
3. `c = a + b` adds the two constants together.
4. `print(c)` prints the result of the addition operation.

For more information, see the TensorFlow [documentation](https://www.tensorflow.org/guide/).

onelinerhub: [How can I use Python and TensorFlow to run computations on the CPU?](https://onelinerhub.com/python-tensorflow/how-can-i-use-python-and-tensorflow-to-run-computations-on-the-cpu)
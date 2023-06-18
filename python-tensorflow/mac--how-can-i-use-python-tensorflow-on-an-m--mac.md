# mac

How can I use Python TensorFlow on an M1 Mac?
// plain

Python TensorFlow can be used on an M1 Mac by first installing the TensorFlow Python package. This can be done with the following command:
```
pip install tensorflow
```

Once TensorFlow is installed, you can use it in your Python code. For example, the following code creates a simple TensorFlow graph:
```
import tensorflow as tf

a = tf.constant(2)
b = tf.constant(3)
c = a + b

with tf.Session() as sess:
    print(sess.run(c))
```
## Output example

```
5
```

The code consists of the following parts:

1. `import tensorflow as tf`: This imports the TensorFlow library, allowing us to use its functions in our code.

2. `a = tf.constant(2)`: This creates a constant tensor with the value 2.

3. `b = tf.constant(3)`: This creates a constant tensor with the value 3.

4. `c = a + b`: This creates a tensor with the result of adding the two constants, which is 5.

5. `with tf.Session() as sess:`: This creates a TensorFlow session, which is used to evaluate tensors.

6. `print(sess.run(c))`: This runs the session and prints the value of the tensor c, which is 5.

For more information on using TensorFlow with an M1 Mac, see the following links:

- https://www.tensorflow.org/install/source#macos
- https://www.tensorflow.org/install/pip#macos

onelinerhub: [mac

How can I use Python TensorFlow on an M1 Mac?](https://onelinerhub.com/python-tensorflow/mac--how-can-i-use-python-tensorflow-on-an-m--mac)
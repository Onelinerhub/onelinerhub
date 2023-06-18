# How can I use a GPU with Python TensorFlow?
// plain

Using a GPU with Python TensorFlow is relatively straightforward. First, you'll need to install the GPU version of TensorFlow. You can do this using `pip install tensorflow-gpu`. Once installed, you can use the GPU with TensorFlow by adding the following code block to the start of your code:

```
import tensorflow as tf

# Tell TensorFlow that you want to use the GPU
with tf.device('/gpu:0'):
    # Define your operations and TensorFlow will automatically use the GPU
    a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
    b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
    c = tf.matmul(a, b)

# Creates a session with log_device_placement set to True.
sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))

# Runs the op.
print(sess.run(c))
```

The output of this code should be:
```
[[22. 28.]
 [49. 64.]]
```

The code consists of the following parts:
1. `import tensorflow as tf` - imports the TensorFlow library.
2. `with tf.device('/gpu:0')` - tells TensorFlow to use the GPU.
3. `a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')` - creates a constant TensorFlow operation with the given values.
4. `b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')` - creates a second constant TensorFlow operation with the given values.
5. `c = tf.matmul(a, b)` - creates a TensorFlow operation that multiplies `a` and `b`.
6. `sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))` - creates a session with log_device_placement set to True.
7. `print(sess.run(c))` - runs the operation and prints the result.

For more information, see the [TensorFlow documentation](https://www.tensorflow.org/guide/using_gpu).

onelinerhub: [How can I use a GPU with Python TensorFlow?](https://onelinerhub.com/python-tensorflow/how-can-i-use-a-gpu-with-python-tensorflow-1687077729)
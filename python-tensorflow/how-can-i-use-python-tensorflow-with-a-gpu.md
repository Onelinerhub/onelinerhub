# How can I use Python TensorFlow with a GPU?
// plain

Using Python TensorFlow with a GPU is a great way to increase the speed of your machine learning algorithms. The following example code block shows how to set up a TensorFlow session to use a GPU:

```
import tensorflow as tf

# Creates a graph.
with tf.device('/gpu:0'):
  a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
  b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
  c = tf.matmul(a, b)

# Creates a session with log_device_placement set to True.
sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))

# Runs the op.
print(sess.run(c))
```

## Output example

```
[[22. 28.]
 [49. 64.]]
```

The code above does the following:
1. Imports the TensorFlow library.
2. Creates a graph with a multiplication operation using two constants.
3. Creates a session with the log_device_placement set to True.
4. Runs the operation and prints the output.

This example code shows how to set up a TensorFlow session to use a GPU, but there are many more parameters and options to consider when using a GPU with TensorFlow. For more information, see the following links:

- [TensorFlow GPU Guide](https://www.tensorflow.org/guide/gpu)
- [Using GPUs](https://www.tensorflow.org/guide/using_gpu)
- [TensorFlow Performance Guide](https://www.tensorflow.org/guide/performance/overview)

onelinerhub: [How can I use Python TensorFlow with a GPU?](https://onelinerhub.com/python-tensorflow/how-can-i-use-python-tensorflow-with-a-gpu)
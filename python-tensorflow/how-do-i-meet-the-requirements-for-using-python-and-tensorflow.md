# How do I meet the requirements for using Python and TensorFlow?
// plain

To use Python and TensorFlow, you need to install both packages on your computer. Python can be downloaded from [Python's official website](https://www.python.org/). TensorFlow can be installed through `pip`, Python's package manager.

For example, to install TensorFlow for Python 3.6, you can use the following command:

```
pip install tensorflow
```

You may also need to install other packages that are used by TensorFlow, such as NumPy and SciPy. These can be installed using `pip` as well.

Once you have installed Python and TensorFlow, you can start writing code using them. Here is a simple example of how to create a TensorFlow graph and run it:

```
import tensorflow as tf

# Create TensorFlow object called tensor
hello_constant = tf.constant('Hello World!')

with tf.Session() as sess:
    # Run the tf.constant operation in the session
    output = sess.run(hello_constant)
    print(output)

# Output: b'Hello World!'
```

For more information on using Python and TensorFlow, see the [TensorFlow tutorials](https://www.tensorflow.org/tutorials/).

onelinerhub: [How do I meet the requirements for using Python and TensorFlow?](https://onelinerhub.com/python-tensorflow/how-do-i-meet-the-requirements-for-using-python-and-tensorflow)
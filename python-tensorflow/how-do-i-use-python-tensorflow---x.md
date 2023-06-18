# How do I use Python TensorFlow 1.x?
// plain

Using Python TensorFlow 1.x is a great way to create and implement deep learning models. TensorFlow 1.x is an open source library that provides a suite of powerful machine learning tools. Here is an example of how to use it:

```
import tensorflow as tf

# Create TensorFlow object called hello_constant
hello_constant = tf.constant('Hello World!')

with tf.Session() as sess:
    # Run the tf.constant operation in the session
    output = sess.run(hello_constant)
    print(output)
```

## Output example

```
b'Hello World!'
```

The code above creates a TensorFlow object called hello_constant using the tf.constant operation. Then, a session is created using the with tf.Session() as sess line of code. This allows the code to run the tf.constant operation in the session. Finally, the session is run and the output is printed.

## Code explanation


1. `import tensorflow as tf`: This imports the TensorFlow library into the program.
2. `hello_constant = tf.constant('Hello World!')`: This creates a TensorFlow object called hello_constant.
3. `with tf.Session() as sess`: This creates a session using the with tf.Session() as sess line of code.
4. `output = sess.run(hello_constant)`: This runs the tf.constant operation in the session.
5. `print(output)`: This prints the output of the session.

## Helpful links

- [TensorFlow 1.x Documentation](https://www.tensorflow.org/guide/version_compat)
- [Getting Started with TensorFlow 1.x](https://www.tensorflow.org/get_started/get_started_v1)

onelinerhub: [How do I use Python TensorFlow 1.x?](https://onelinerhub.com/python-tensorflow/how-do-i-use-python-tensorflow---x)
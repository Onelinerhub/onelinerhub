# How do I use TensorFlow 1.x with Python?
// plain

TensorFlow 1.x is a library for numerical computation using data flow graphs. It is used for machine learning applications such as neural networks. TensorFlow 1.x can be used with Python by installing the library.

To install TensorFlow 1.x with Python, use the following command:

```pip install tensorflow==1.x```

Once installed, you can import TensorFlow into your Python program by using the following code:

```import tensorflow as tf```

This will allow you to use TensorFlow functions and classes in your Python program.

To use TensorFlow 1.x with Python, you can create a data flow graph using the TensorFlow API. This graph is composed of nodes, which represent mathematical operations, and edges, which represent the data flowing between nodes.

For example, the following code creates a constant node in the graph with the value of 10:

```
node1 = tf.constant(10)
```

Once the graph is constructed, it can be executed by creating a session and running the graph.

```
sess = tf.Session()
output = sess.run(node1)
```

The output of the above code is:

```
10
```

TensorFlow 1.x can be used with Python to create and execute data flow graphs for machine learning applications.

## Helpful links

- [TensorFlow Installation Guide](https://www.tensorflow.org/install)
- [TensorFlow Tutorials](https://www.tensorflow.org/tutorials)

onelinerhub: [How do I use TensorFlow 1.x with Python?](https://onelinerhub.com/python-tensorflow/how-do-i-use-tensorflow---x-with-python)
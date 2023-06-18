# What is TensorFlow in Python?
// plain

TensorFlow is an open-source library for numerical computation and machine learning using data flow graphs in Python. It is used for a variety of tasks such as classification, regression, and clustering. It has a comprehensive, flexible ecosystem of tools, libraries, and community resources that lets researchers push the state-of-the-art in ML and developers easily build and deploy ML powered applications.

## Example code

```
import tensorflow as tf

# Create a Constant op that produces a 1x2 matrix.
# The op is added as a node to the default graph.
#
# The value returned by the constructor represents the output
# of the Constant op.
matrix1 = tf.constant([[3., 3.]])

# Create another Constant that produces a 2x1 matrix.
matrix2 = tf.constant([[2.],[2.]])

# Create a Matmul op that takes 'matrix1' and 'matrix2' as inputs.
# The returned value, 'product', represents the result of the matrix
# multiplication.
product = tf.matmul(matrix1, matrix2)

# Launch the default graph.
sess = tf.Session()

# To run the matmul op we call the session 'run()' method, passing 'product'
# which represents the output of the matmul op.  This indicates to the call
# that we want to get the output of the matmul op back.
#
# All inputs needed by the op are run automatically by the session.  They
# typically are run in parallel.
#
# The call 'run(product)' thus causes the execution of three ops in the
# graph: the two constants and matmul.
#
# The output of the op is returned in 'result' as a numpy `ndarray` object.
result = sess.run(product)
print(result)
# ==> [[ 12.]]
```

## Output example

```
[[12.]]
```

## Code explanation


1. `import tensorflow as tf` - imports the TensorFlow library as the `tf` module.
2. `matrix1 = tf.constant([[3., 3.]])` - creates a constant op that produces a 1x2 matrix.
3. `matrix2 = tf.constant([[2.],[2.]])` - creates a constant op that produces a 2x1 matrix.
4. `product = tf.matmul(matrix1, matrix2)` - creates a Matmul op that takes `matrix1` and `matrix2` as inputs and returns the result of the matrix multiplication as `product`.
5. `sess = tf.Session()` - launches the default graph.
6. `result = sess.run(product)` - runs the matmul op and returns the output in `result` as a numpy `ndarray` object.
7. `print(result)` - prints the output.

## Helpful links

1. [TensorFlow Official Website](https://www.tensorflow.org/)
2. [TensorFlow Tutorials](https://www.tensorflow.org/tutorials)
3. [TensorFlow Documentation](https://www.tensorflow.org/api_docs)

onelinerhub: [What is TensorFlow in Python?](https://onelinerhub.com/python-tensorflow/what-is-tensorflow-in-python)
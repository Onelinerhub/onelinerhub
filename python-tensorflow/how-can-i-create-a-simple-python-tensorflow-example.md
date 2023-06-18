# How can I create a simple Python TensorFlow example?
// plain

This is an example of a simple Python TensorFlow example.

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

# Close the Session when we're done.
sess.close()
```

## Output example

```
[[12.]]
```

This example consists of the following parts:
1. Import TensorFlow as tf.
2. Create two Constant ops that produce 1x2 and 2x1 matrices.
3. Create a Matmul op that takes the two matrices as inputs.
4. Launch the default graph.
5. Run the matmul op using the session's `run()` method, passing the output of the matmul op as an argument.
6. Close the session.

## Helpful links
- [TensorFlow Tutorial](https://www.tensorflow.org/tutorials/)
- [TensorFlow Basics](https://www.tensorflow.org/tutorials/quickstart/beginner)

onelinerhub: [How can I create a simple Python TensorFlow example?](https://onelinerhub.com/python-tensorflow/how-can-i-create-a-simple-python-tensorflow-example)
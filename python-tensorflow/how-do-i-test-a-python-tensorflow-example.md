# How do I test a Python TensorFlow example?
// plain

Testing a Python TensorFlow example can be done in several ways.

1. To ensure the example code is running correctly, it can be run in a Python interpreter. For example, the following code can be used to test a simple TensorFlow example:

```
import tensorflow as tf

# Create a Constant op that produces a 1x2 matrix.
matrix1 = tf.constant([[3., 3.]])

# Create another Constant that produces a 2x1 matrix.
matrix2 = tf.constant([[2.],[2.]])

# Create a Matmul op that takes 'matrix1' and 'matrix2' as inputs.
# The returned value, 'product', represents the result of the matrix
# multiplication.
product = tf.matmul(matrix1, matrix2)

# To run the matmul op we call the session 'sess' on 'product'
with tf.Session() as sess:
    result = sess.run(product)
    print(result)
```
## Output example

```
[[12.]]
```

2. Unit tests can also be used to test a TensorFlow example. For example, the following code can be used to test the same simple TensorFlow example:

```
import unittest
import tensorflow as tf

class TensorFlowTest(unittest.TestCase):

    def test_matmul(self):
        matrix1 = tf.constant([[3., 3.]])
        matrix2 = tf.constant([[2.],[2.]])
        product = tf.matmul(matrix1, matrix2)
        with tf.Session() as sess:
            result = sess.run(product)
            self.assertEqual(result.all(), [[12.]].all())

if __name__ == '__main__':
    unittest.main()
```

## Output example

```
..
----------------------------------------------------------------------
Ran 2 tests in 0.002s

OK
```

3. A debugger can also be used to step through the example code and verify that the expected output is being produced.

## Helpful links
1. https://www.tensorflow.org/tutorials/quickstart/beginner
2. https://www.tensorflow.org/guide/effective_tf2#debugging

onelinerhub: [How do I test a Python TensorFlow example?](https://onelinerhub.com/python-tensorflow/how-do-i-test-a-python-tensorflow-example)
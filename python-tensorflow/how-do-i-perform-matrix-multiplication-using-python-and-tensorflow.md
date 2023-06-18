# How do I perform matrix multiplication using Python and TensorFlow?
// plain

Matrix multiplication can be performed using Python and TensorFlow using the `tf.matmul` function. This function takes two matrices as arguments and performs the multiplication operation.

For example:
```
import tensorflow as tf

# create two matrices
matrix1 = tf.constant([[1,2], [3,4]])
matrix2 = tf.constant([[5,6], [7,8]])

# perform matrix multiplication
matrix_multiply = tf.matmul(matrix1, matrix2)

# print result
with tf.Session() as sess:
    result = sess.run(matrix_multiply)
    print(result)
```

## Output example

```
[[19 22]
 [43 50]]
```

The code above:
- Imports the TensorFlow library (`import tensorflow as tf`)
- Creates two matrices (`matrix1` and `matrix2`)
- Performs the matrix multiplication operation using the `tf.matmul` function (`matrix_multiply = tf.matmul(matrix1, matrix2)`)
- Prints the result of the operation (`result = sess.run(matrix_multiply)` and `print(result)`)

## Helpful links
- TensorFlow Documentation: [tf.matmul](https://www.tensorflow.org/api_docs/python/tf/matmul)

onelinerhub: [How do I perform matrix multiplication using Python and TensorFlow?](https://onelinerhub.com/python-tensorflow/how-do-i-perform-matrix-multiplication-using-python-and-tensorflow)
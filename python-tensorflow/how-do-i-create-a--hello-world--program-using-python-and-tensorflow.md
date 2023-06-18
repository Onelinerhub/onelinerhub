# How do I create a "Hello World" program using Python and TensorFlow?
// plain

This "Hello World" program using Python and TensorFlow will print "Hello World" to the console.

```
import tensorflow as tf

hello = tf.constant('Hello, World!')
sess = tf.Session()
print(sess.run(hello))
```
## Output example
 `b'Hello, World!'`

The code consists of the following parts:
1. Import TensorFlow as `tf`: This is done using `import tensorflow as tf`.
2. Create a constant string `hello` with value `Hello, World!`: This is done using `hello = tf.constant('Hello, World!')`.
3. Create a session `sess`: This is done using `sess = tf.Session()`.
4. Print `hello` to the console: This is done using `print(sess.run(hello))`.

## Helpful links
- [TensorFlow Tutorials](https://www.tensorflow.org/tutorials/)
- [Getting Started with TensorFlow](https://www.tensorflow.org/get_started/)

onelinerhub: [How do I create a "Hello World" program using Python and TensorFlow?](https://onelinerhub.com/python-tensorflow/how-do-i-create-a--hello-world--program-using-python-and-tensorflow)
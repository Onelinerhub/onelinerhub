# How do I use Python and TensorFlow Placeholders?
// plain

Python and TensorFlow Placeholders are used to feed data into a TensorFlow graph. A placeholder is a variable that we can assign data to at a later point. It allows us to create our operations and build our computation graph, without needing the data.

## Example code

```
import tensorflow as tf

# Create a placeholder of type float 32-bit, shape is a vector of 3 elements
a = tf.placeholder(tf.float32, shape=[3])

# Create a constant of type float 32-bit, shape is a vector of 3 elements
b = tf.constant([5, 5, 5], tf.float32)

# Use the placeholder as you would a constant
c = a + b  # Short for tf.add(a, b)

with tf.Session() as sess:
    # Feed [1, 2, 3] to placeholder a via the dict {a: [1, 2, 3]}
    # fetch value of c
    print(sess.run(c, {a: [1, 2, 3]}))
```

## Output example

```
[6. 7. 8.]
```

The code above consists of the following parts:
- `import tensorflow as tf` imports the TensorFlow library.
- `a = tf.placeholder(tf.float32, shape=[3])` creates a placeholder of type float 32-bit, shape is a vector of 3 elements.
- `b = tf.constant([5, 5, 5], tf.float32)` creates a constant of type float 32-bit, shape is a vector of 3 elements.
- `c = a + b` uses the placeholder as you would a constant.
- `print(sess.run(c, {a: [1, 2, 3]}))` feeds [1, 2, 3] to placeholder a via the dict {a: [1, 2, 3]} and fetches the value of c.

## Helpful links
- [TensorFlow Placeholders](https://www.tensorflow.org/api_docs/python/tf/placeholder)
- [TensorFlow Tutorial](https://www.tensorflow.org/tutorials/).

onelinerhub: [How do I use Python and TensorFlow Placeholders?](https://onelinerhub.com/python-tensorflow/how-do-i-use-python-and-tensorflow-placeholders)
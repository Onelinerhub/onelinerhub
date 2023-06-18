# How do I resolve a SymbolAlreadyExposedError when the symbol "zeros" is already exposed as () in TensorFlow Python util tf_export?
// plain

The `SymbolAlreadyExposedError` is a common error when using TensorFlow Python util `tf_export` and occurs when the symbol "zeros" is already exposed as () in TensorFlow Python util `tf_export`.

To resolve this error, you can use the `tf.get_variable` function to get the variable and use the `tf.zeros` function to initialize the variable.

For example:

```
import tensorflow as tf

x = tf.get_variable('x', shape=[2,2], initializer=tf.zeros)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(x))

# Output
[[0. 0.]
 [0. 0.]]
```

The code above consists of the following parts:

1. `import tensorflow as tf` - imports the TensorFlow library.
2. `x = tf.get_variable('x', shape=[2,2], initializer=tf.zeros)` - creates the variable `x` and initializes it with the `tf.zeros` function.
3. `with tf.Session() as sess:` - creates a TensorFlow session.
4. `sess.run(tf.global_variables_initializer())` - initializes all the global variables.
5. `print(sess.run(x))` - prints the variable `x`.

By using the `tf.get_variable` and `tf.zeros` functions, the `SymbolAlreadyExposedError` can be resolved.

## Helpful links

- [TensorFlow get_variable](https://www.tensorflow.org/api_docs/python/tf/get_variable)
- [TensorFlow zeros](https://www.tensorflow.org/api_docs/python/tf/zeros)

onelinerhub: [How do I resolve a SymbolAlreadyExposedError when the symbol "zeros" is already exposed as () in TensorFlow Python util tf_export?](https://onelinerhub.com/python-tensorflow/how-do-i-resolve-a-symbolalreadyexposederror-when-the-symbol--zeros--is-already-exposed-as----in-tensorflow-python-util-tf-export)
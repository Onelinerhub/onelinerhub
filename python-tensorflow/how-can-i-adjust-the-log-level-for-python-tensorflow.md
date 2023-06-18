# How can I adjust the log level for Python TensorFlow?
// plain

To adjust the log level for Python TensorFlow, you can use the `tf.compat.v1.logging.set_verbosity()` function. This function takes an argument specifying the desired log level, which can be one of the following:

- `tf.compat.v1.logging.ERROR`
- `tf.compat.v1.logging.WARNING`
- `tf.compat.v1.logging.INFO`
- `tf.compat.v1.logging.DEBUG`

For example, to set the log level to `tf.compat.v1.logging.INFO`, you can use the following code:

```
import tensorflow as tf
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.INFO)
```

The output of this code will be `None`.

Further information can be found in the [TensorFlow documentation](https://www.tensorflow.org/api_docs/python/tf/compat/v1/logging/set_verbosity).

onelinerhub: [How can I adjust the log level for Python TensorFlow?](https://onelinerhub.com/python-tensorflow/how-can-i-adjust-the-log-level-for-python-tensorflow)
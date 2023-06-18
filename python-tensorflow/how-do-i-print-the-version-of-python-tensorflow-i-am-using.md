# How do I print the version of Python Tensorflow I am using?
// plain

The version of TensorFlow that you are using can be determined by printing the version number of the TensorFlow package. This can be done by using the `tf.version` module.

## Example code

```
import tensorflow as tf
print(tf.version)
```

## Output example

```
<module 'tensorflow_core._api.v2.version' from '/usr/local/lib/python3.6/dist-packages/tensorflow_core/_api/v2/version/__init__.py'>
```

The version number of the TensorFlow package can be accessed by using the `__version__` attribute of the `tf.version` module.

## Example code

```
import tensorflow as tf
print(tf.version.__version__)
```

## Output example

```
2.2.0
```

In summary, the version of TensorFlow that you are using can be determined by printing the version number of the TensorFlow package using the `tf.version.__version__` attribute.

## Helpful links
- [TensorFlow version](https://www.tensorflow.org/guide/version_compat#tensorflow_version)
- [tf.version](https://www.tensorflow.org/api_docs/python/tf/version)

onelinerhub: [How do I print the version of Python Tensorflow I am using?](https://onelinerhub.com/python-tensorflow/how-do-i-print-the-version-of-python-tensorflow-i-am-using)
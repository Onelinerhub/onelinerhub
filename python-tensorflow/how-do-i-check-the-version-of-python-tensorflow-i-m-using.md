# How do I check the version of Python Tensorflow I'm using?
// plain

To check the version of Python Tensorflow you are using, you can use the `tf.version` module. This module provides a version string of the form major.minor.patch, which can be used to check the version of TensorFlow.

## Example


```
import tensorflow as tf

print(tf.version.VERSION)
```

## Output example

```
2.2.0
```

The code above imports the `tensorflow` module and prints out the version of TensorFlow using the `tf.version.VERSION` attribute.

The `tf.version` module also provides other attributes, such as `tf.version.COMPILER_VERSION` which can be used to check the version of the compiler used to compile TensorFlow.

## Helpful links

- https://www.tensorflow.org/api_docs/python/tf/version
- https://www.tensorflow.org/install/source#git_version_select

onelinerhub: [How do I check the version of Python Tensorflow I'm using?](https://onelinerhub.com/python-tensorflow/how-do-i-check-the-version-of-python-tensorflow-i-m-using)
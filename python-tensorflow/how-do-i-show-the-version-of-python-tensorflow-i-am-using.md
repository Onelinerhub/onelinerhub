# How do I show the version of Python TensorFlow I am using?
// plain

To show the version of Python TensorFlow you are using, you can use the `tf.version` module. This module provides access to the TensorFlow version information as a named tuple of Python strings.

## Example code

```
import tensorflow as tf
print(tf.version)
```

## Output example

```
<module 'tensorflow_core._api.v2.version' from '/usr/local/lib/python3.6/dist-packages/tensorflow_core/_api/v2/version/__init__.py'>
```

The version information is stored as a tuple of strings, which can be accessed using the following code:

```
from tensorflow.version import VERSION
print(VERSION)
```

## Output example

```
2.1.0
```

The `tf.version` module provides access to the following information:

- `VERSION`: A string containing the version of TensorFlow, e.g. "2.1.0"
- `GIT_VERSION`: A string containing the git commit hash of the TensorFlow repository
- `COMPILER_VERSION`: A string containing the version of the compiler used to compile TensorFlow
- `BUILD_INFO`: A string containing the build information of TensorFlow

You can find more information about the `tf.version` module in the [TensorFlow documentation](https://www.tensorflow.org/api_docs/python/tf/version).

onelinerhub: [How do I show the version of Python TensorFlow I am using?](https://onelinerhub.com/python-tensorflow/how-do-i-show-the-version-of-python-tensorflow-i-am-using)
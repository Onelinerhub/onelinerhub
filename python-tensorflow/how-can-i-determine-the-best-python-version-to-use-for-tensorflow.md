# How can I determine the best Python version to use for TensorFlow?
// plain

The best Python version to use for TensorFlow depends on the version of TensorFlow you are using. Generally speaking, Python 3.5 or higher is recommended for use with the latest version of TensorFlow.

For example, if you are using TensorFlow 2.0, you should use Python 3.5 or higher.
```
import tensorflow as tf
print(tf.__version__)

2.0.0
```

To check the version of Python you are using, you can use the following code snippet:
```
import sys
print(sys.version)

3.7.4 (default, Aug  9 2019, 18:34:13) [MSC v.1915 64 bit (AMD64)]
```

If you are using an earlier version of TensorFlow, you may need to use a different version of Python. For example, TensorFlow 1.14 requires Python 3.4 or higher.

The following list provides more information about the compatibility of different versions of Python and TensorFlow:

- [TensorFlow Python version support](https://www.tensorflow.org/install/lang_python)
- [Python version support](https://docs.python.org/3/whatsnew/3.0.html)
- [Python 3.5 release notes](https://docs.python.org/3/whatsnew/3.5.html)
- [Python 3.6 release notes](https://docs.python.org/3/whatsnew/3.6.html)
- [Python 3.7 release notes](https://docs.python.org/3/whatsnew/3.7.html)

onelinerhub: [How can I determine the best Python version to use for TensorFlow?](https://onelinerhub.com/python-tensorflow/how-can-i-determine-the-best-python-version-to-use-for-tensorflow)
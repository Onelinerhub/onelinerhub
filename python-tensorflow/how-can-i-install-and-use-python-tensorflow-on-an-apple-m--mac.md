# How can I install and use Python TensorFlow on an Apple M1 Mac?
// plain

To install and use Python TensorFlow on an Apple M1 Mac, you need to use the [Apple Silicon version of TensorFlow](https://github.com/apple/tensorflow_macos).

1. Download the latest version of [Python 3.8.5](https://www.python.org/downloads/release/python-385/).
2. Install the version of Python 3.8.5 using the downloaded installer.
3. Install the TensorFlow package with the command `pip3 install tensorflow==2.4.0-rc1`
4. Verify that TensorFlow is installed correctly by running the following code:

```
import tensorflow as tf
print(tf.version)
```

## Output example

```
2.4.0-rc1
```

5. Check the [TensorFlow documentation](https://www.tensorflow.org/api_docs/python/tf) for more information on how to use TensorFlow.
6. Follow the [Apple Silicon-specific instructions](https://github.com/apple/tensorflow_macos) for using TensorFlow on an M1 Mac.
7. Test out your TensorFlow code on your Apple M1 Mac.

onelinerhub: [How can I install and use Python TensorFlow on an Apple M1 Mac?](https://onelinerhub.com/python-tensorflow/how-can-i-install-and-use-python-tensorflow-on-an-apple-m--mac)
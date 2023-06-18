# How can I use Tensorflow 1.x with Python 3.8?
// plain

TensorFlow 1.x can be used with Python 3.8 by installing the compatible version of TensorFlow. The latest version of TensorFlow 1.x that is compatible with Python 3.8 is TensorFlow 1.15.0.

To install TensorFlow 1.15.0 with Python 3.8, use the following command:

```
pip install tensorflow==1.15.0
```

The output of the command should be something like this:

```
Collecting tensorflow==1.15.0
  Downloading https://files.pythonhosted.org/packages/3f/98/5a99af92fb911d7a88a0005ad55005f35b4c1ba8d75fba02df726cd936e6/tensorflow-1.15.0-cp38-cp38-manylinux2010_x86_64.whl (412.3MB)
    |████████████████████████████████| 412.3MB 1.5kB/s
Installing collected packages: tensorflow
Successfully installed tensorflow-1.15.0
```

Once TensorFlow 1.15.0 is installed, it can be imported in Python 3.8 with the following code:

```
import tensorflow as tf
print(tf.__version__)
```

The output of the code should be:

```
1.15.0
```

## Helpful links

- Installing TensorFlow: https://www.tensorflow.org/install/
- TensorFlow Release Notes: https://github.com/tensorflow/tensorflow/releases

onelinerhub: [How can I use Tensorflow 1.x with Python 3.8?](https://onelinerhub.com/python-tensorflow/how-can-i-use-tensorflow---x-with-python----)
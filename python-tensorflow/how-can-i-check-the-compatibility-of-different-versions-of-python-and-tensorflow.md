# How can I check the compatibility of different versions of Python and TensorFlow?
// plain

The compatibility of different versions of Python and TensorFlow can be checked using the TensorFlow version compatibility matrix. This matrix provides detailed information about which versions of Python and TensorFlow are compatible with each other.

For example, to check the compatibility of Python 3.6 and TensorFlow 2.1, we can run the following code:
```
import tensorflow as tf
print(tf.__version__)
```
The output of the code will be:
```
2.1.0
```

The compatibility matrix can be found at the following link:
https://www.tensorflow.org/install/source#tested_build_configurations

The matrix consists of the following parts:

1. **TensorFlow Version:** This lists the version of TensorFlow that is being tested.

2. **Python Version:** This lists the version of Python that is being tested.

3. **Compiler:** This lists the compiler that is being used to build the TensorFlow package.

4. **Build Status:** This indicates whether the build was successful or not.

5. **OS:** This indicates the operating system that the build was tested on.

By using this matrix, users can easily check the compatibility of different versions of Python and TensorFlow.

onelinerhub: [How can I check the compatibility of different versions of Python and TensorFlow?](https://onelinerhub.com/python-tensorflow/how-can-i-check-the-compatibility-of-different-versions-of-python-and-tensorflow)
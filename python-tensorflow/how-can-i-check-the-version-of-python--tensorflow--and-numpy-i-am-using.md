# How can I check the version of Python, Tensorflow, and Numpy I am using?
// plain

To check the version of Python, Tensorflow, and Numpy you are using, you can use the following code:

```
import sys
import tensorflow as tf
import numpy as np

print("Python version:", sys.version)
print("Tensorflow version:", tf.__version__)
print("Numpy version:", np.__version__)
```

## Output example

```
Python version: 3.7.6 (default, Jan  8 2020, 19:59:22)
[GCC 7.3.0]
Tensorflow version: 2.1.0
Numpy version: 1.18.1
```

The code consists of three parts:
1. `import sys` imports the `sys` module, which contains system-specific parameters and functions.
2. `import tensorflow as tf` imports the Tensorflow library and assigns it to the `tf` alias.
3. `import numpy as np` imports the Numpy library and assigns it to the `np` alias.

The following three lines print the version of Python, Tensorflow, and Numpy respectively:

`print("Python version:", sys.version)`
`print("Tensorflow version:", tf.__version__)`
`print("Numpy version:", np.__version__)`

For more information on how to check the version of Python, Tensorflow, and Numpy, please refer to [this page](https://www.tensorflow.org/install/pip#check_your_tensorflow_version).

onelinerhub: [How can I check the version of Python, Tensorflow, and Numpy I am using?](https://onelinerhub.com/python-tensorflow/how-can-i-check-the-version-of-python--tensorflow--and-numpy-i-am-using)
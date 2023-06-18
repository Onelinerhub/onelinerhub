# How can I use a GPU with Python and TensorFlow?
// plain

Using a GPU with Python and TensorFlow is relatively straightforward.

First, you need to make sure that your system has a compatible GPU. You can check this by running the following code:
```
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())
```
This should print a list of devices connected to your system. If you see a GPU listed, then you can proceed.

Next, you need to install the GPU version of TensorFlow. This can be done using either `pip` or `conda`:
```
# Using pip
pip install tensorflow-gpu

# Using conda
conda install tensorflow-gpu
```

Once the installation is complete, you can check if TensorFlow is using the GPU by running the following code:
```
import tensorflow as tf
sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
```
This should print a log of the devices that TensorFlow is using. If you see your GPU listed, then you know that TensorFlow is using it.

Finally, you can start using your GPU with TensorFlow. Here is a simple example of a TensorFlow program that uses a GPU:
```
import tensorflow as tf

# Create two constants
a = tf.constant([1.0, 2.0, 3.0], shape=[3], name='a')
b = tf.constant([1.0, 2.0, 3.0], shape=[3], name='b')

# Create a graph
c = a + b

# Create a session
sess = tf.Session()

# Execute the graph
print(sess.run(c))
```

The output of this code should be:
```
[ 2.  4.  6.]
```

This example shows how to use a GPU with Python and TensorFlow.

## Helpful links

- [TensorFlow GPU Guide](https://www.tensorflow.org/install/gpu)
- [TensorFlow Device List](https://www.tensorflow.org/api_docs/python/tf/device)

onelinerhub: [How can I use a GPU with Python and TensorFlow?](https://onelinerhub.com/python-tensorflow/how-can-i-use-a-gpu-with-python-and-tensorflow)
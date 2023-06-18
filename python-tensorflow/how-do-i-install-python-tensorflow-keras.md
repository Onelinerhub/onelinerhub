# How do I install Python TensorFlow Keras?
// plain

1. First, you need to install Python. You can do this by downloading the latest version from the [Python website](https://www.python.org/downloads/).
2. Next, you need to install TensorFlow. You can do this by running the following command in your terminal:
```
pip install tensorflow
```
3. After that, you need to install Keras. You can do this by running the following command in your terminal:
```
pip install keras
```
4. To check if the installation was successful, you can run the following code:
```
import tensorflow as tf
import keras

print(tf.__version__)
print(keras.__version__)
```
The output should look like this:
```
2.2.0
2.3.1
```
5. To make sure that the GPU is being used for processing, you can run the following code:
```
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())
```
The output should look like this:
```
[name: "/device:CPU:0"
device_type: "CPU"
memory_limit: 268435456
locality {
}
incarnation: 7041636451142901116
, name: "/device:XLA_CPU:0"
device_type: "XLA_CPU"
memory_limit: 17179869184
locality {
}
incarnation: 12451820862490267539
physical_device_desc: "device: XLA_CPU device"
]
```
6. You can also use the [TensorFlow website](https://www.tensorflow.org/install) for more detailed instructions and information on installation.
7. You can also find a lot of helpful tutorials and resources on the [Keras website](https://keras.io/).

onelinerhub: [How do I install Python TensorFlow Keras?](https://onelinerhub.com/python-tensorflow/how-do-i-install-python-tensorflow-keras)
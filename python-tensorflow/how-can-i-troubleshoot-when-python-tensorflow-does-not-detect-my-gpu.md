# How can I troubleshoot when Python TensorFlow does not detect my GPU?
// plain

1. Make sure your GPU is compatible with TensorFlow by checking the [list of supported GPUs](https://www.tensorflow.org/install/gpu#hardware_requirements).

2. Check if your GPU is visible to TensorFlow by running the following code:

```
import tensorflow as tf
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
```
The output should be `Num GPUs Available: 1` if your GPU is detected.

3. Make sure you have the latest version of TensorFlow installed.

4. Check your driver version by running the following code:

```
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())
```

The output should include a line like `name: "/device:GPU:0"` if your GPU is detected.

5. Check the logs for any errors related to the GPU.

6. Make sure your GPU is enabled in your BIOS settings.

7. Make sure you have the latest version of the GPU driver installed.

onelinerhub: [How can I troubleshoot when Python TensorFlow does not detect my GPU?](https://onelinerhub.com/python-tensorflow/how-can-i-troubleshoot-when-python-tensorflow-does-not-detect-my-gpu)
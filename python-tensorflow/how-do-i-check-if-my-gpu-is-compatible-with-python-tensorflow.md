# How do I check if my GPU is compatible with Python TensorFlow?
// plain

To check if your GPU is compatible with Python TensorFlow, you can use the `tf.test.is_gpu_available()` method. This method returns a boolean value indicating whether TensorFlow can access a GPU.

## Example code


```
import tensorflow as tf
tf.test.is_gpu_available()
```

Example output:

```
True
```

This example code imports the TensorFlow library and uses the `tf.test.is_gpu_available()` method to check if a GPU is available. If a GPU is available, the method will return `True`.

If you want to check which GPUs are available, you can use the `tf.config.list_physical_devices('GPU')` method.

## Example code


```
import tensorflow as tf
tf.config.list_physical_devices('GPU')
```

Example output:

```
[PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU')]
```

This example code imports the TensorFlow library and uses the `tf.config.list_physical_devices('GPU')` method to list the available GPUs. The output shows the name of the physical device and its type.

## Helpful links

- [TensorFlow GPU support](https://www.tensorflow.org/install/gpu)
- [tf.test.is_gpu_available()](https://www.tensorflow.org/api_docs/python/tf/test/is_gpu_available)
- [tf.config.list_physical_devices()](https://www.tensorflow.org/api_docs/python/tf/config/list_physical_devices)

onelinerhub: [How do I check if my GPU is compatible with Python TensorFlow?](https://onelinerhub.com/python-tensorflow/how-do-i-check-if-my-gpu-is-compatible-with-python-tensorflow)
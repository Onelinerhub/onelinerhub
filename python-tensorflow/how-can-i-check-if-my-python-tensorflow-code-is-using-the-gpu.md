# How can I check if my Python TensorFlow code is using the GPU?
// plain

To check if your Python TensorFlow code is using the GPU, you can use the `tf.test.is_gpu_available()` method. This will return `True` if a GPU is available and `False` if it isn't.

## Example

```
import tensorflow as tf

tf.test.is_gpu_available()
```
## Output example

```
True
```

You can also use the `tf.config.list_physical_devices('GPU')` method to list the physical GPUs available.

## Example

```
import tensorflow as tf

tf.config.list_physical_devices('GPU')
```
## Output example

```
[PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU')]
```

You can also use the `tf.config.experimental.list_physical_devices('GPU')` method to list the physical GPUs available.

## Example

```
import tensorflow as tf

tf.config.experimental.list_physical_devices('GPU')
```
## Output example

```
[PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU')]
```

If you want to check which device your code is running on, you can use the `tf.config.list_logical_devices()` method. This will list the available devices, including CPUs and GPUs.

## Example

```
import tensorflow as tf

tf.config.list_logical_devices()
```
## Output example

```
[LogicalDevice(name='/device:CPU:0', device_type='CPU'), LogicalDevice(name='/device:GPU:0', device_type='GPU')]
```

## Helpful links
* [TensorFlow Documentation - Testing for GPU Availability](https://www.tensorflow.org/guide/gpu#testing_for_gpu_availability)
* [TensorFlow Documentation - Listing Physical and Logical Devices](https://www.tensorflow.org/guide/gpu#listing_physical_and_logical_devices)

onelinerhub: [How can I check if my Python TensorFlow code is using the GPU?](https://onelinerhub.com/python-tensorflow/how-can-i-check-if-my-python-tensorflow-code-is-using-the-gpu)
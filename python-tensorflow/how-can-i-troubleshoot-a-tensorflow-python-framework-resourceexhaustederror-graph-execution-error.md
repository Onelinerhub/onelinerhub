# How can I troubleshoot a TensorFlow Python Framework ResourceExhaustedError graph execution error?
// plain

1. First, understand the cause of the error. The ResourceExhaustedError graph execution error occurs when the TensorFlow runtime is unable to allocate memory resources.

2. Next, use the `tf.debugging.set_log_device_placement(True)` command to log the device placement of the operations in the graph. This will help identify which operations are using the most resources.

3. Try reducing the size of the graph by removing unnecessary operations.

4. Use the `tf.config.experimental.set_virtual_device_configuration` command to configure the memory usage of the virtual devices.

5. Increase the amount of memory available to the TensorFlow runtime by using the `tf.config.experimental.set_memory_growth` command.

6. Use the `tf.config.experimental.set_soft_device_placement` command to enable soft device placement. This will allow TensorFlow to choose the best device for each operation.

7. If all else fails, try using a different version of TensorFlow or a different platform.

## Example code

```
import tensorflow as tf

tf.debugging.set_log_device_placement(True)
tf.config.experimental.set_virtual_device_configuration(
    [tf.config.experimental.VirtualDeviceConfiguration()])
tf.config.experimental.set_memory_growth(True)
tf.config.experimental.set_soft_device_placement(True)
```

## Output example

```
Device mapping:
/job:localhost/replica:0/task:0/device:XLA_CPU:0 -> device: XLA_CPU device
```

onelinerhub: [How can I troubleshoot a TensorFlow Python Framework ResourceExhaustedError graph execution error?](https://onelinerhub.com/python-tensorflow/how-can-i-troubleshoot-a-tensorflow-python-framework-resourceexhaustederror-graph-execution-error)
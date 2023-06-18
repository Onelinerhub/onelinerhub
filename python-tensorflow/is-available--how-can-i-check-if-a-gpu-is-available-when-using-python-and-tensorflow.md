# is available

How can I check if a GPU is available when using Python and TensorFlow?
// plain

Checking if a GPU is available when using Python and TensorFlow can be done using the following code:
```
import tensorflow as tf
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
```
This code will output the number of GPUs available. For example, if two GPUs are available, the output will be `Num GPUs Available: 2`.

The code consists of the following parts:
- `import tensorflow as tf`: This imports the TensorFlow library into the current program.
- `print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))`: This prints out the number of GPUs available.

For more information, please refer to the following links:
- [TensorFlow GPU Guide](https://www.tensorflow.org/guide/gpu)
- [Check if a GPU is available in TensorFlow](https://stackoverflow.com/questions/38559755/how-to-get-current-available-gpus-in-tensorflow)

onelinerhub: [is available

How can I check if a GPU is available when using Python and TensorFlow?](https://onelinerhub.com/python-tensorflow/is-available--how-can-i-check-if-a-gpu-is-available-when-using-python-and-tensorflow)
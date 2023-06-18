# How can I use a GPU with Python Tensorflow?
// plain

You can use a GPU with Python Tensorflow to speed up your machine learning tasks. Here is an example of how to do this:

```
import tensorflow as tf

# Check the available devices
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))

# Set the device
tf.config.experimental.set_visible_devices([], 'GPU')

# Check if the device is set
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
```
## Output example


```
Num GPUs Available:  1
Num GPUs Available:  0
```

The code above first prints the number of available GPUs, and then sets the device to GPU. The second print statement confirms that the device is set.

To use the GPU with Tensorflow, you need to:

1. Import the `tensorflow` module
2. Check the available devices
3. Set the device to GPU

You can find more information on using GPUs with Tensorflow in the [official documentation](https://www.tensorflow.org/guide/gpu).

onelinerhub: [How can I use a GPU with Python Tensorflow?](https://onelinerhub.com/python-tensorflow/how-can-i-use-a-gpu-with-python-tensorflow)
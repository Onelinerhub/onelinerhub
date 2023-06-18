# How can I test a Python TensorFlow GPU?
// plain

1. Install [TensorFlow GPU](https://www.tensorflow.org/install/gpu) on your local machine.
2. Verify that your system has a compatible GPU with the [Nvidia GPU-Driver](https://www.nvidia.com/Download/index.aspx).
3. Create a virtual environment with `python -m venv <env_name>` and activate it with `source <env_name>/bin/activate`.
4. Install the TensorFlow GPU version: `pip install --upgrade tensorflow-gpu`.
5. Run the following code snippet to check if the installation was successful:
```
import tensorflow as tf

tf.test.is_gpu_available()
```
## Output example
 `True`
6. To further test the installation, you can run the following code snippet:
```
import tensorflow as tf

tf.test.gpu_device_name()
```
## Output example
 `/device:GPU:0`
7. You can also use the [TensorFlow GPU Test](https://www.tensorflow.org/guide/gpu#test_the_tensorflow_gpu_installation) to check the installation.

onelinerhub: [How can I test a Python TensorFlow GPU?](https://onelinerhub.com/python-tensorflow/how-can-i-test-a-python-tensorflow-gpu)
# How do I install CUDA for Python TensorFlow?
// plain

1. Before installing CUDA for Python TensorFlow, you must first install the NVIDIA GPU drivers and CUDA Toolkit. The drivers can be found on the [NVIDIA website](https://www.nvidia.com/Download/index.aspx) and the CUDA Toolkit can be found on the [NVIDIA Developer website](https://developer.nvidia.com/cuda-downloads).

2. After the drivers and CUDA Toolkit have been installed, you can install the CUDA for Python TensorFlow package. To do this, use the following command in the command line:

```
pip install tensorflow-gpu
```

3. Once the package has been installed, you can then verify that the CUDA is properly installed by running the following example code:

```
import tensorflow as tf

print(tf.test.is_built_with_cuda())
```

The output should be `True` if CUDA is installed correctly.

4. To check the version of the CUDA installed, you can run the following command:

```
nvcc --version
```

This will display the version of the CUDA installed.

5. To check if your GPU is being used by TensorFlow, you can run the following code:

```
from tensorflow.python.client import device_lib

print(device_lib.list_local_devices())
```

This will output a list of devices that TensorFlow is using, and will include the GPU if it is being used.

6. Finally, to ensure that your installation is working correctly, you can run the [TensorFlow “Hello World” example](https://www.tensorflow.org/tutorials/quickstart/beginner).

7. For more information on installing CUDA for Python TensorFlow, please refer to the [TensorFlow installation guide](https://www.tensorflow.org/install).

onelinerhub: [How do I install CUDA for Python TensorFlow?](https://onelinerhub.com/python-tensorflow/how-do-i-install-cuda-for-python-tensorflow)
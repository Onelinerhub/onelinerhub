# How can I set up a Python TensorFlow environment using an AMD GPU?
// plain

1. Install the latest version of Python 3.x from [here](https://www.python.org/downloads/).
2. Install the latest version of TensorFlow for AMD GPU from [here](https://www.tensorflow.org/install/gpu).
3. Install the AMD GPU driver from [here](https://www.amd.com/en/support).
4. Install the latest version of CUDA Toolkit from [here](https://developer.nvidia.com/cuda-downloads).
5. Install the latest version of cuDNN from [here](https://developer.nvidia.com/cudnn).
6. Install the latest version of Anaconda from [here](https://www.anaconda.com/distribution/).
7. Create a virtual environment with `conda create -n myenv python=3.6` and activate it with `conda activate myenv`.

```python
import tensorflow as tf

# Check if GPU is available
print(tf.test.is_gpu_available())
```

## Output example
 `True`

onelinerhub: [How can I set up a Python TensorFlow environment using an AMD GPU?](https://onelinerhub.com/python-tensorflow/how-can-i-set-up-a-python-tensorflow-environment-using-an-amd-gpu)
# How to install TensorFlow with GPU support on Windows 10 using Python?
// plain

1. Install the CUDA Toolkit 10.1 and the corresponding cuDNN library.
2. Install the Visual C++ Build Tools.
3. Create a conda environment with Python 3.7 and activate it.
4. Install the GPU version of TensorFlow:
   ```
   pip install --upgrade tensorflow-gpu
   ```
5. Check if the installation is successful:
   ```
   python
   import tensorflow as tf
   tf.test.is_built_with_cuda()
   >> True
   ```
6. Install additional libraries for TensorFlow (optional):
   ```
   pip install Pillow
   pip install scipy
   ```
7. Verify the installation by running some basic TensorFlow operations.

## Helpful links
- https://www.tensorflow.org/install/gpu
- https://www.tensorflow.org/install/pip

onelinerhub: [How to install TensorFlow with GPU support on Windows 10 using Python?](https://onelinerhub.com/python-tensorflow/how-to-install-tensorflow-with-gpu-support-on-windows----using-python)
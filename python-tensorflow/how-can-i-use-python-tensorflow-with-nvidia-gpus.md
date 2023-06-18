# How can I use Python TensorFlow with Nvidia GPUs?
// plain

**Using Python TensorFlow with Nvidia GPUs**

1. Install the latest version of TensorFlow with GPU support: `pip install tensorflow-gpu`.
2. Install the latest Nvidia GPU drivers and CUDA Toolkit.
3. Verify your system has a compatible GPU.
4. Configure the GPU environment variables:
```
export CUDA_VISIBLE_DEVICES=0
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/local/cuda/lib64:/usr/local/cuda/extras/CUPTI/lib64"
```
5. Run Python code with TensorFlow-GPU:
```
import tensorflow as tf
tf.test.is_gpu_available()

# Output
True
```
6. Train and evaluate models on the GPU.
7. Monitor the GPU usage with the `nvidia-smi` command line tool.

## Helpful links
- [TensorFlow GPU Support](https://www.tensorflow.org/install/gpu)
- [Nvidia Drivers Download](https://www.nvidia.com/Download/index.aspx)
- [CUDA Toolkit Download](https://developer.nvidia.com/cuda-downloads)

onelinerhub: [How can I use Python TensorFlow with Nvidia GPUs?](https://onelinerhub.com/python-tensorflow/how-can-i-use-python-tensorflow-with-nvidia-gpus)
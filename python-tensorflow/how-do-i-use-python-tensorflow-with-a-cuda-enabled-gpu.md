# How do I use Python TensorFlow with a CUDA-enabled GPU?
// plain

Using Python TensorFlow with a CUDA-enabled GPU requires several steps:

1. Install the CUDA Toolkit, which includes the CUDA Driver and other tools.
2. Install the NVIDIA CUDA Deep Neural Network library (cuDNN).
3. Install the Python development environment.
4. Install TensorFlow using `pip install tensorflow-gpu`.
5. Check if GPU is detected by running the following code:
```
import tensorflow as tf

tf.test.is_gpu_available()
```
## Output example
 `True`
6. Now you can use TensorFlow with a CUDA-enabled GPU. For example:
```
import tensorflow as tf

a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
c = tf.matmul(a, b)

sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))

print(sess.run(c))
```
## Output example

```
[[22. 28.]
 [49. 64.]]
```

## Helpful links
- [TensorFlow Documentation: Installing TensorFlow with GPU support](https://www.tensorflow.org/install/gpu)
- [NVIDIA CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit)
- [NVIDIA cuDNN](https://developer.nvidia.com/cudnn)

onelinerhub: [How do I use Python TensorFlow with a CUDA-enabled GPU?](https://onelinerhub.com/python-tensorflow/how-do-i-use-python-tensorflow-with-a-cuda-enabled-gpu)
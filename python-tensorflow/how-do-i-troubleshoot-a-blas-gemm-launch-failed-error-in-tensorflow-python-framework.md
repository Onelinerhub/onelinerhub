# How do I troubleshoot a BLAS GEMM Launch Failed error in TensorFlow Python Framework?
// plain

To troubleshoot a BLAS GEMM Launch Failed error in TensorFlow Python Framework, the following steps should be taken:

1. Check the system requirements: TensorFlow requires a 64-bit version of Python 3.5 or higher.

2. Make sure the correct version of TensorFlow is installed.

3. Check if the system is using the right BLAS library.

```
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
tf.test.is_gpu_available(
    cuda_only=False,
    min_cuda_compute_capability=None
)
```

## Output example


```
2020-08-12 10:12:45.378621: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
2020-08-12 10:12:45.390973: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library libcudart.so.10.1
2020-08-12 10:12:47.086779: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library libcublas.so.10
2020-08-12 10:12:47.090041: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library libblas.so.3
2020-08-12 10:12:47.091796: W tensorflow/stream_executor/blas/blas_utils.cc:37] No GPU devices available on machine.
True
```

From the output, we can see that the system is using the correct BLAS library (libblas.so.3).

4. Make sure the environment variables are set correctly.

5. Check if the system is using the right CUDA version.

6. Check if the system is using the right cuDNN version.

7. If all of the above steps have been taken, try reinstalling TensorFlow.

## Helpful links

- [TensorFlow System Requirements](https://www.tensorflow.org/install/source#system_requirements)
- [Installing TensorFlow](https://www.tensorflow.org/install/pip)
- [Troubleshooting Guide](https://www.tensorflow.org/install/troubleshoot)

onelinerhub: [How do I troubleshoot a BLAS GEMM Launch Failed error in TensorFlow Python Framework?](https://onelinerhub.com/python-tensorflow/how-do-i-troubleshoot-a-blas-gemm-launch-failed-error-in-tensorflow-python-framework)
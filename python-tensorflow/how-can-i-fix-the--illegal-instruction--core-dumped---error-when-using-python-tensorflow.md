# How can I fix the "illegal instruction (core dumped)" error when using Python Tensorflow?
// plain

The "illegal instruction (core dumped)" error is an indication that the CPU is attempting to execute an instruction that is not a valid operation. This can occur when using Python Tensorflow due to a mismatch between the version of Tensorflow installed and the version of the CPU instruction set.

To fix this issue, you should first check the version of Tensorflow installed and ensure it is compatible with your CPU instruction set. For example, if you are running Tensorflow on an Intel processor, you should check the Intel MKL-DNN version compatibility page to ensure you have the correct version of Tensorflow installed.

Once you have verified the version of Tensorflow is compatible with your CPU instruction set, you can try running the following code to test if the issue is resolved:

```
import tensorflow as tf
tf.test.is_gpu_available()
```

If the code runs without error, then the issue should be resolved.

**Parts of the Code and Explanation:**
- `import tensorflow as tf`: This imports the Tensorflow library into the current Python environment.
- `tf.test.is_gpu_available()`: This function checks if a GPU is available for use with Tensorflow.

**## Helpful links**
- Intel MKL-DNN version compatibility page: https://software.intel.com/content/www/us/en/develop/articles/intel-mkl-dnn-version-list.html

onelinerhub: [How can I fix the "illegal instruction (core dumped)" error when using Python Tensorflow?](https://onelinerhub.com/python-tensorflow/how-can-i-fix-the--illegal-instruction--core-dumped---error-when-using-python-tensorflow)
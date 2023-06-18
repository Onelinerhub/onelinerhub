# How can I use Anaconda to install TensorFlow in Python?
// plain

Anaconda is a free and open source distribution of Python that includes many popular data science and machine learning packages. It is an easy way to install TensorFlow in Python. To install TensorFlow using Anaconda, follow these steps:

1. Open the Anaconda Prompt.
2. Run the following command to create a virtual environment for TensorFlow:
```
conda create -n tensorflow_env tensorflow
```
3. Activate the virtual environment:
```
conda activate tensorflow_env
```
4. Install TensorFlow:
```
pip install --ignore-installed --upgrade tensorflow
```
5. Verify the installation:
```
python -c "import tensorflow as tf;print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
```

## Output example

```
tf.Tensor(-14.335083, shape=(), dtype=float32)
```

For more information, please refer to the official TensorFlow documentation:
https://www.tensorflow.org/install/pip

onelinerhub: [How can I use Anaconda to install TensorFlow in Python?](https://onelinerhub.com/python-tensorflow/how-can-i-use-anaconda-to-install-tensorflow-in-python)
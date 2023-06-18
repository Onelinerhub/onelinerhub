# How do I install TensorFlow using Conda in Python?
// plain

To install TensorFlow using Conda in Python, you can use the following steps:

1. Create a Conda environment with Python 3.7 or higher:
```
conda create -n myenv python=3.7
```

2. Activate the environment:
```
conda activate myenv
```

3. Install TensorFlow inside the environment:
```
conda install tensorflow
```

4. Verify that TensorFlow is installed correctly:
```
python -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
```
## Output example

```
tf.Tensor(-7.054118, shape=(), dtype=float32)
```

5. Deactivate the environment:
```
conda deactivate
```

You can find more information about installing TensorFlow using Conda in the [official TensorFlow documentation](https://www.tensorflow.org/install/conda).

onelinerhub: [How do I install TensorFlow using Conda in Python?](https://onelinerhub.com/python-tensorflow/how-do-i-install-tensorflow-using-conda-in-python)
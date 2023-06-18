# How can I use Python TensorFlow with Conda?
// plain

To use Python TensorFlow with Conda, you need to install Conda and create a Conda environment.

In the Conda environment, you can use the following command to install TensorFlow:

```
conda install -c conda-forge tensorflow
```

This command will install the latest version of TensorFlow and its dependencies.

Once TensorFlow is installed, you can use it in your Python programs. For example, you can use the following code to check if TensorFlow is installed correctly:

```
import tensorflow as tf

print(tf.__version__)
```

The output should be something like `2.2.0`.

You can also use Conda to create virtual environments for different versions of TensorFlow. For example, you can use the following command to create a virtual environment with TensorFlow version 2.0:

```
conda create -n tf20 python=3.7 tensorflow=2.0
```

Once the virtual environment is created, you can activate it and use TensorFlow version 2.0.

## Helpful links

- [Installing TensorFlow with Conda](https://www.tensorflow.org/install/conda)
- [Creating virtual environments with Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands)

onelinerhub: [How can I use Python TensorFlow with Conda?](https://onelinerhub.com/python-tensorflow/how-can-i-use-python-tensorflow-with-conda)
# How do I update my Python TensorFlow library?
// plain

Updating your Python TensorFlow library is easy and can be done in a few steps.

1. First, you need to install the latest version of pip, the Python package manager.
```
python -m pip install --upgrade pip
```
2. After that, you can use pip to upgrade your TensorFlow library.
```
pip install --upgrade tensorflow
```
3. You can also specify a particular version of TensorFlow to install.
```
pip install tensorflow==2.2.0
```

Once the installation is complete, you can verify the version of TensorFlow installed by running the following command:

```
python -c "import tensorflow as tf; print(tf.__version__)"
```
## Output example

```
2.2.0
```

You can also check the version of TensorFlow available for installation by running the following command:

```
pip install --upgrade --pre tensorflow
```

This will list the available versions of TensorFlow and you can install the one you need.

## Helpful links
* [Installing TensorFlow](https://www.tensorflow.org/install)
* [Upgrading TensorFlow](https://www.tensorflow.org/install/upgrade)

onelinerhub: [How do I update my Python TensorFlow library?](https://onelinerhub.com/python-tensorflow/how-do-i-update-my-python-tensorflow-library)
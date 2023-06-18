# How can I install a Python TensorFlow wheel?
// plain

1. To install a Python TensorFlow wheel, first you need to download the appropriate wheel file for your platform from the [TensorFlow website](https://www.tensorflow.org/install/pip).
2. After downloading the wheel file, you can install it using the `pip` command. For example, if you have downloaded the `tensorflow-1.14.0-cp37-cp37m-win_amd64.whl` file:

```
pip install tensorflow-1.14.0-cp37-cp37m-win_amd64.whl
```

3. This will install the TensorFlow wheel in your Python environment. You can check if the installation was successful by running the following command:

```
python -c "import tensorflow as tf;print(tf.__version__)"
```

## Output example


```
1.14.0
```

4. You can also install the TensorFlow wheel directly from PyPI using the following command:

```
pip install tensorflow
```

5. This will download and install the latest version of TensorFlow from PyPI.
6. If you need to install a specific version of TensorFlow, you can specify the version number when installing it with `pip`:

```
pip install tensorflow==1.14.0
```

7. This will install the specified version of TensorFlow.

onelinerhub: [How can I install a Python TensorFlow wheel?](https://onelinerhub.com/python-tensorflow/how-can-i-install-a-python-tensorflow-wheel)
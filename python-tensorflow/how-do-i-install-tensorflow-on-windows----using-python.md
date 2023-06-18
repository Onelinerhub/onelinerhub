# How do I install TensorFlow on Windows 10 using Python?
// plain

To install TensorFlow on Windows 10 using Python, you need to have Python 3.5 or higher installed. You can check the version of Python installed by running the following command in the command prompt:

```
python --version
```

The output should look something like this:

```
Python 3.7.3
```

Once you have verified that the correct version of Python is installed, you can use pip to install TensorFlow. To install TensorFlow, run the following command in the command prompt:

```
pip install tensorflow
```

This will install the latest version of TensorFlow for Python 3.7.

If you need to install a different version of TensorFlow, you can specify the version number by running the following command:

```
pip install tensorflow==2.2.0
```

This will install version 2.2.0 of TensorFlow for Python 3.7.

Once TensorFlow is installed, you can verify the installation by running the following command in the command prompt:

```
python -c "import tensorflow as tf;print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
```

The output should look something like this:

```
-7.08619
```

This indicates that TensorFlow has been successfully installed.

## Code explanation
**

1. `python --version`: This command is used to check the version of Python installed on the system.
2. `pip install tensorflow`: This command is used to install the latest version of TensorFlow for Python 3.7.
3. `pip install tensorflow==2.2.0`: This command is used to install a specific version of TensorFlow for Python 3.7.
4. `python -c "import tensorflow as tf;print(tf.reduce_sum(tf.random.normal([1000, 1000])))"`: This command is used to verify that TensorFlow has been successfully installed.

**## Helpful links**

- [Installing TensorFlow on Windows](https://www.tensorflow.org/install/pip#windows_steps)
- [Python 3.7 Documentation](https://docs.python.org/3.7/)

onelinerhub: [How do I install TensorFlow on Windows 10 using Python?](https://onelinerhub.com/python-tensorflow/how-do-i-install-tensorflow-on-windows----using-python)
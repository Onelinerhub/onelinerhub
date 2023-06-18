# How do I install TensorFlow for Python on a Jetson Nano?
// plain

To install TensorFlow for Python on a Jetson Nano, first you will need to install Python 3.6. This can be done by running the following command in a terminal:
```
sudo apt-get install python3.6
```

Once Python is installed, you will need to install pip, the package manager for Python, using the following command:
```
sudo apt-get install python3-pip
```

Next, you will need to install TensorFlow itself. This can be done using the pip command, as shown below:
```
pip3 install --user --upgrade tensorflow
```

You will also need to install the TensorFlow GPU package if you wish to use the GPU for TensorFlow operations. This can be done using the following command:
```
pip3 install --user --upgrade tensorflow-gpu
```

Finally, you can verify that TensorFlow has been installed correctly by running a simple test script, as shown below:
```
python3 -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
```

This should output a random number, indicating that TensorFlow is installed and working correctly.

## Code explanation
**

1. `sudo apt-get install python3.6`: This command will install Python 3.6 on the Jetson Nano.
2. `sudo apt-get install python3-pip`: This command will install the Python package manager, pip.
3. `pip3 install --user --upgrade tensorflow`: This command will install the TensorFlow package.
4. `pip3 install --user --upgrade tensorflow-gpu`: This command will install the TensorFlow GPU package.
5. `python3 -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"`: This command will run a simple test script to verify that TensorFlow is installed and working correctly.

**## Helpful links**

- [TensorFlow Installation Guide](https://www.tensorflow.org/install)
- [Installing Python 3 on Jetson Nano](https://www.jetsonhacks.com/2019/07/30/install-python-3-on-nvidia-jetson-nano/)

onelinerhub: [How do I install TensorFlow for Python on a Jetson Nano?](https://onelinerhub.com/python-tensorflow/how-do-i-install-tensorflow-for-python-on-a-jetson-nano)
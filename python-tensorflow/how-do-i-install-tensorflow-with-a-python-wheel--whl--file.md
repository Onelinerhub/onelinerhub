# How do I install Tensorflow with a Python wheel (whl) file?
// plain

Installing Tensorflow with a Python wheel (whl) file is a simple process. First, download the appropriate whl file for your system from the [Tensorflow website](https://www.tensorflow.org/install/pip). Then, open a terminal and navigate to the directory containing the whl file. Finally, use the following command to install Tensorflow:

```
pip install <whl file name>
```

For example, if the whl file is named `tensorflow-2.1.0-cp37-cp37m-win_amd64.whl`, then the command to install Tensorflow is:

```
pip install tensorflow-2.1.0-cp37-cp37m-win_amd64.whl
```

This will install Tensorflow in the current Python environment. To verify the installation, you can import Tensorflow in a Python script and check the version:

```
import tensorflow as tf
print(tf.__version__)
```

## Output example

```
2.1.0
```

If you encounter any errors during the installation, you can refer to the [Tensorflow installation guide](https://www.tensorflow.org/install/pip) for help.

onelinerhub: [How do I install Tensorflow with a Python wheel (whl) file?](https://onelinerhub.com/python-tensorflow/how-do-i-install-tensorflow-with-a-python-wheel--whl--file)
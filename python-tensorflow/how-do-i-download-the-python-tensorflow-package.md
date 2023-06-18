# How do I download the Python TensorFlow package?
// plain

1. The Python TensorFlow package can be downloaded from the official [TensorFlow website](https://www.tensorflow.org/install/pip).
2. You can install TensorFlow either with Python's pip package manager or with a virtual environment.
3. To install with pip, use the following command:
```
pip install tensorflow
```
4. To install with a virtual environment, use the following commands:
```
# Create a virtual environment
python3 -m venv env

# Activate the virtual environment
source env/bin/activate

# Install TensorFlow
pip install tensorflow
```
5. Once the installation is complete, you can check the version of TensorFlow installed with the following command:
```
python -c 'import tensorflow as tf; print(tf.__version__)'
```
6. Output:
```
2.2.0
```
7. You can also find more detailed instructions on the [TensorFlow installation page](https://www.tensorflow.org/install).

onelinerhub: [How do I download the Python TensorFlow package?](https://onelinerhub.com/python-tensorflow/how-do-i-download-the-python-tensorflow-package)
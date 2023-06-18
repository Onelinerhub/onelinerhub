# How do I install Python TensorFlow on Windows?
// plain

1. Install [Python](https://www.python.org/downloads/) on your Windows machine.
2. Install [pip](https://pip.pypa.io/en/stable/installing/) package manager.
3. Run the following command in the command prompt to install TensorFlow:
```
pip install tensorflow
```
4. To check the version of TensorFlow installed, run the following command in the command prompt:
```
python -c "import tensorflow as tf; print(tf.__version__)"
```
## Output example

```
2.3.0
```
5. To use TensorFlow in your Python project, include the following code in your project:
```
import tensorflow as tf
```
6. To create a TensorFlow session, use the following code:
```
sess = tf.Session()
```
7. To close the session, use the following code:
```
sess.close()
```

## Helpful links

- [TensorFlow Installation Guide](https://www.tensorflow.org/install)
- [Installing TensorFlow on Windows](https://www.tensorflow.org/install/pip#windows_steps)

onelinerhub: [How do I install Python TensorFlow on Windows?](https://onelinerhub.com/python-tensorflow/how-do-i-install-python-tensorflow-on-windows)
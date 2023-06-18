# How do I install TensorFlow for Python?
// plain

Installing TensorFlow for Python can be done in a few simple steps.

1. Install the latest version of Python.
2. Download and install TensorFlow from the official website.
3. Create a virtual environment and activate it.

```
python -m venv env
source env/bin/activate
```

4. Install the TensorFlow package inside the virtual environment.

```
pip install --upgrade tensorflow
```

5. Confirm that the installation was successful by importing the TensorFlow library.

```
python
import tensorflow as tf
print(tf.__version__)
```
## Output example
 2.2.0

6. Test a simple TensorFlow program.

```
import tensorflow as tf

# Create a constant op
# This op is added as a node to the default graph
hello = tf.constant("Hello, TensorFlow!")

# start a TF session
sess = tf.Session()

# run the op and get result
print(sess.run(hello))
```

## Output example
 b'Hello, TensorFlow!'

## Helpful links
- [Python Download](https://www.python.org/downloads/)
- [TensorFlow Download](https://www.tensorflow.org/install)
- [Creating Virtual Environments](https://docs.python.org/3/tutorial/venv.html)

onelinerhub: [How do I install TensorFlow for Python?](https://onelinerhub.com/python-tensorflow/how-do-i-install-tensorflow-for-python)
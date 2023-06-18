# How do I use TensorFlow 1.15 with Python?
// plain

TensorFlow is an open source library for machine learning and deep learning. It is available for Python, C++, and JavaScript. To use TensorFlow 1.15 with Python, the following steps should be taken:

1. Install Python 3.5 or above on your system.
2. Install TensorFlow 1.15 with `pip install tensorflow==1.15`
3. Create a Python script, for example:

```
import tensorflow as tf

hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))
```

The output will be:

```
b'Hello, TensorFlow!'
```

4. Run the script with `python <script_name>.py`
5. Verify the installation with `pip list | grep tensorflow`

The output should be:

```
tensorflow            1.15.0
```

For further information, please refer to the [TensorFlow documentation](https://www.tensorflow.org/install/pip).

onelinerhub: [How do I use TensorFlow 1.15 with Python?](https://onelinerhub.com/python-tensorflow/how-do-i-use-tensorflow------with-python)
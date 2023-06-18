# How do I install TensorFlow in a Python Jupyter Notebook?
// plain

1. Install TensorFlow in your environment:
  ```
  pip install tensorflow
  ```

2. Import TensorFlow in your Jupyter Notebook:
  ```
  import tensorflow as tf
  ```

3. Check the version of TensorFlow installed:
  ```
  print(tf.__version__)
  ```
  Output: `2.2.0`

4. Create a constant in TensorFlow:
  ```
  hello = tf.constant('Hello, TensorFlow!')
  ```

5. Run the constant in a session:
  ```
  sess = tf.Session()
  print(sess.run(hello))
  ```
  Output: `Hello, TensorFlow!`

6. Close the session to release resources:
  ```
  sess.close()
  ```

7. You have now successfully installed and used TensorFlow in your Python Jupyter Notebook!

## Helpful links
- [Install TensorFlow](https://www.tensorflow.org/install)
- [TensorFlow Guide](https://www.tensorflow.org/tutorials)

onelinerhub: [How do I install TensorFlow in a Python Jupyter Notebook?](https://onelinerhub.com/python-tensorflow/how-do-i-install-tensorflow-in-a-python-jupyter-notebook)
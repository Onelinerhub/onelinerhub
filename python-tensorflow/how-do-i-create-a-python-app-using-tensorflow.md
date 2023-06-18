# How do I create a Python app using TensorFlow?
// plain

Using TensorFlow to create a Python app requires a few steps.

1. Install TensorFlow, either using `pip install tensorflow` or `conda install tensorflow`.

2. Create a Python script, such as `my_app.py`

3. Import TensorFlow into the script, using `import tensorflow as tf`

4. Create a TensorFlow graph, with operations such as `tf.add()` and `tf.multiply()`

## Example

```
import tensorflow as tf

a = tf.add(3,5)
b = tf.multiply(3,5)

with tf.Session() as sess:
    print("a =", sess.run(a))
    print("b =", sess.run(b))
```

## Output example

```
a = 8
b = 15
```

5. Run the TensorFlow graph within a session, using `tf.Session()`

6. Execute the graph with `sess.run()`

7. Close the session with `sess.close()`

## Helpful links
- [TensorFlow Installation Guide](https://www.tensorflow.org/install)
- [TensorFlow Basics Tutorial](https://www.tensorflow.org/tutorials/quickstart/beginner)

onelinerhub: [How do I create a Python app using TensorFlow?](https://onelinerhub.com/python-tensorflow/how-do-i-create-a-python-app-using-tensorflow)
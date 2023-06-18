# How do I get started with TensorFlow in Python for beginners?
// plain

To get started with TensorFlow in Python for beginners, you can follow this guide:
1. Install TensorFlow:
   ```pip install tensorflow```
2. Import TensorFlow into your Python program:
   ```import tensorflow as tf```
3. Create a TensorFlow constant:
   ```a = tf.constant(2.0)```
4. Create a TensorFlow variable:
   ```b = tf.Variable(3.0)```
5. Create a TensorFlow operation:
   ```c = a + b```
6. Initialize the variables:
   ```init = tf.global_variables_initializer()```
7. Create a TensorFlow session and run the operation:
   ```with tf.Session() as sess:
    sess.run(init)
    print(sess.run(c))
   ```
   Output: ```5.0```

## Helpful links
- [TensorFlow Installation Guide](https://www.tensorflow.org/install)
- [TensorFlow Tutorials](https://www.tensorflow.org/tutorials)

onelinerhub: [How do I get started with TensorFlow in Python for beginners?](https://onelinerhub.com/python-tensorflow/how-do-i-get-started-with-tensorflow-in-python-for-beginners)
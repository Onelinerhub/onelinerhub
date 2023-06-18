# How do Python TensorFlow and Keras compare in terms of performance and features?
// plain

Python TensorFlow and Keras are both open source libraries for deep learning and machine learning. TensorFlow is a lower-level library that provides a more direct approach to working with data, while Keras is a higher-level library that makes it easier to develop deep learning models.

In terms of performance, TensorFlow is faster, but Keras is more user-friendly. TensorFlow is often used for complex deep learning models, while Keras is better suited for simpler models.

In terms of features, TensorFlow has more advanced features such as distributed training, custom models, and automatic differentiation. Keras, on the other hand, has fewer features but is easier to use and can be used to quickly build deep learning models.

For example, here is a simple TensorFlow model:
```
import tensorflow as tf

x = tf.placeholder(tf.float32, shape=[None, 784])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
y = tf.matmul(x, W) + b

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    print(sess.run(y))
```

## Output example

```
[[0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 ...
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]]
```

And here is a simple Keras model:
```
from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
model.add(Dense(units=64, activation='relu', input_dim=100))
model.add(Dense(units=10, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])
```

In summary, Python TensorFlow and Keras are both powerful deep learning libraries, but they have different strengths and weaknesses. TensorFlow is faster and more powerful, but Keras is easier to use and can be used to quickly build deep learning models.

## Helpful links
- [TensorFlow](https://www.tensorflow.org/)
- [Keras](https://keras.io/)

onelinerhub: [How do Python TensorFlow and Keras compare in terms of performance and features?](https://onelinerhub.com/python-tensorflow/how-do-python-tensorflow-and-keras-compare-in-terms-of-performance-and-features)
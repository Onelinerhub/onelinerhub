# How do I use Python and TensorFlow to implement gradient descent?
// plain

Gradient descent is a technique used to minimize a cost function in machine learning. It can be used to optimize the weights and parameters of a model. In Python, TensorFlow provides an easy-to-use API for implementing gradient descent.

```
# import the necessary modules
import tensorflow as tf

# define the model parameters
w = tf.Variable([.3], tf.float32)
b = tf.Variable([-.3], tf.float32)

# define the inputs and outputs of the model
x = tf.placeholder(tf.float32)
linear_model = w * x + b
y = tf.placeholder(tf.float32)

# define the cost/loss function
loss = tf.reduce_sum(tf.square(linear_model - y))

# define the optimizer
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

# initialize the variables
init = tf.global_variables_initializer()

# define the training data
x_train = [1, 2, 3, 4]
y_train = [0, -1, -2, -3]

# run the training loop
with tf.Session() as sess:
  sess.run(init)
  for i in range(1000):
    sess.run(train, {x: x_train, y: y_train})

  # evaluate training accuracy
  curr_w, curr_b, curr_loss  = sess.run([w, b, loss], {x: x_train, y: y_train})
  print("w: %s b: %s loss: %s"%(curr_w, curr_b, curr_loss))
```

## Output example

```
w: [-0.9999969] b: [0.9999908] loss: 5.6999738e-11
```

The code above implements gradient descent in TensorFlow. It first imports the necessary modules (1). It then defines the model parameters (2) and the inputs and outputs of the model (3). The cost/loss function is then defined (4). An optimizer is then defined (5) and the variables are initialized (6). The training data is then defined (7) and the training loop is run (8). Finally, the training accuracy is evaluated (9).

1. Import modules: `import tensorflow as tf`
2. Define model parameters: `w = tf.Variable([.3], tf.float32)`, `b = tf.Variable([-.3], tf.float32)`
3. Define inputs and outputs: `x = tf.placeholder(tf.float32)`, `linear_model = w * x + b`, `y = tf.placeholder(tf.float32)`
4. Define cost/loss function: `loss = tf.reduce_sum(tf.square(linear_model - y))`
5. Define optimizer: `optimizer = tf.train.GradientDescentOptimizer(0.01)`, `train = optimizer.minimize(loss)`
6. Initialize variables: `init = tf.global_variables_initializer()`
7. Define training data: `x_train = [1, 2, 3, 4]`, `y_train = [0, -1, -2, -3]`
8. Run training loop: `with tf.Session() as sess: sess.run(init) for i in range(1000): sess.run(train, {x: x_train, y: y_train})`
9. Evaluate training accuracy: `curr_w, curr_b, curr_loss  = sess.run([w, b, loss], {x: x_train, y: y_train})`

## Helpful links
- [TensorFlow Documentation - Gradient Descent](https://www.tensorflow.org/api_docs/python/tf/train/GradientDescentOptimizer)
- [TensorFlow Tutorial - Gradient Descent](https://www.tensorflow.org/tutorials/keras/basic_regression)

onelinerhub: [How do I use Python and TensorFlow to implement gradient descent?](https://onelinerhub.com/python-tensorflow/how-do-i-use-python-and-tensorflow-to-implement-gradient-descent)
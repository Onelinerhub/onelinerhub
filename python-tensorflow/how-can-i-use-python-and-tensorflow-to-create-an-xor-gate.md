# How can I use Python and TensorFlow to create an XOR gate?
// plain

This can be done by creating a neural network with two input neurons, one output neuron and one hidden layer with two neurons. With this structure, we can create an XOR gate using TensorFlow and Python.

```
import tensorflow as tf

# Inputs
x = tf.placeholder(tf.float32, shape=[4,2], name='x')

# Outputs
y_ = tf.placeholder(tf.float32, shape=[4,1], name='y_')

# Weights and biases
W_h = tf.Variable(tf.random_uniform([2,2], -1, 1), name="W_h")
b_h = tf.Variable(tf.zeros([2]), name="b_h")

W_o = tf.Variable(tf.random_uniform([2,1], -1, 1), name="W_o")
b_o = tf.Variable(tf.zeros([1]), name="b_o")

# Hidden Layer
h = tf.sigmoid(tf.matmul(x, W_h) + b_h)

# Output Layer
y = tf.sigmoid(tf.matmul(h, W_o) + b_o)

# Cost Function
cost = tf.reduce_mean(( (y_ * tf.log(y)) +
        ((1 - y_) * tf.log(1.0 - y)) ) * -1)

# Optimizer
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cost)

# Training
sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)

# Training Data
XOR_X = [[0,0],[0,1],[1,0],[1,1]]
XOR_Y = [[0],[1],[1],[0]]

# Run
for i in range(100000):
    sess.run(train_step, feed_dict={x: XOR_X, y_: XOR_Y})

# Print
print('Output:')
print(sess.run(y, feed_dict={x: XOR_X}))
```

## Output example

```
[[0.01991707]
 [0.980087   ]
 [0.97948706]
 [0.01991817]]
```

## Code explanation


1. Importing the TensorFlow library: `import tensorflow as tf`
2. Creating the placeholders for inputs and outputs: `x = tf.placeholder(tf.float32, shape=[4,2], name='x')` and `y_ = tf.placeholder(tf.float32, shape=[4,1], name='y_')`
3. Creating the weights and biases for the hidden and output layers: `W_h = tf.Variable(tf.random_uniform([2,2], -1, 1), name="W_h")`, `b_h = tf.Variable(tf.zeros([2]), name="b_h")`, `W_o = tf.Variable(tf.random_uniform([2,1], -1, 1), name="W_o")` and `b_o = tf.Variable(tf.zeros([1]), name="b_o")`
4. Computing the output of the hidden layer: `h = tf.sigmoid(tf.matmul(x, W_h) + b_h)`
5. Computing the output of the output layer: `y = tf.sigmoid(tf.matmul(h, W_o) + b_o)`
6. Computing the cost function: `cost = tf.reduce_mean(( (y_ * tf.log(y)) + ((1 - y_) * tf.log(1.0 - y)) ) * -1)`
7. Creating the optimizer: `train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cost)`
8. Initializing the variables: `init = tf.global_variables_initializer()`
9. Creating the training data: `XOR_X = [[0,0],[0,1],[1,0],[1,1]]` and `XOR_Y = [[0],[1],[1],[0]]`
10. Running the training loop: `for i in range(100000): sess.run(train_step, feed_dict={x: XOR_X, y_: XOR_Y})`
11. Printing the output: `print(sess.run(y, feed_dict={x: XOR_X}))`

## Helpful links

1. [TensorFlow Tutorials](https://www.tensorflow.org/tutorials/)
2. [Neural Networks and Deep Learning](http://neuralnetworksanddeeplearning.com/)
3. [Building Neural Network with TensorFlow](https://www.datacamp.com/community/tutorials/tensorflow-tutorial)

onelinerhub: [How can I use Python and TensorFlow to create an XOR gate?](https://onelinerhub.com/python-tensorflow/how-can-i-use-python-and-tensorflow-to-create-an-xor-gate)
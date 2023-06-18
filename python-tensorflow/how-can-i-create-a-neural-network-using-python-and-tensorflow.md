# How can I create a neural network using Python and TensorFlow?
// plain

Creating a neural network using Python and TensorFlow is relatively simple. The following example code block shows how to create a basic neural network with one hidden layer of 10 neurons:

```
import tensorflow as tf

# define the number of neurons in each layer
n_inputs = 784
n_hidden1 = 10
n_outputs = 10

# define the placeholders for the inputs
X = tf.placeholder(tf.float32, shape=(None, n_inputs), name="X")
y = tf.placeholder(tf.int64, shape=(None), name="y")

# define the layers of the neural network
hidden1 = tf.layers.dense(X, n_hidden1, name="hidden1", activation=tf.nn.relu)
logits = tf.layers.dense(hidden1, n_outputs, name="outputs")

# define the cost function
xentropy = tf.nn.sparse_softmax_cross_entropy_with_logits(labels=y, logits=logits)
cost = tf.reduce_mean(xentropy, name="cost")

# define the optimizer
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
training_op = optimizer.minimize(cost)

# define the accuracy function
correct = tf.nn.in_top_k(logits, y, 1)
accuracy = tf.reduce_mean(tf.cast(correct, tf.float32))

# initialize all variables
init = tf.global_variables_initializer()
```

This code block creates a neural network with 784 inputs, 10 neurons in the hidden layer, and 10 outputs. It also defines the placeholders for the inputs, the layers of the neural network, the cost function, the optimizer, and the accuracy function. Finally, it initializes all the variables.

## Code explanation


- `import tensorflow as tf`: imports the TensorFlow library.
- `n_inputs = 784`: sets the number of inputs to 784.
- `n_hidden1 = 10`: sets the number of neurons in the hidden layer to 10.
- `n_outputs = 10`: sets the number of outputs to 10.
- `X = tf.placeholder(tf.float32, shape=(None, n_inputs), name="X")`: creates a placeholder for the inputs.
- `y = tf.placeholder(tf.int64, shape=(None), name="y")`: creates a placeholder for the outputs.
- `hidden1 = tf.layers.dense(X, n_hidden1, name="hidden1", activation=tf.nn.relu)`: creates the hidden layer with 10 neurons and a ReLU activation function.
- `logits = tf.layers.dense(hidden1, n_outputs, name="outputs")`: creates the output layer.
- `xentropy = tf.nn.sparse_softmax_cross_entropy_with_logits(labels=y, logits=logits)`: defines the cost function.
- `cost = tf.reduce_mean(xentropy, name="cost")`: calculates the mean cost.
- `optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)`: creates the optimizer.
- `training_op = optimizer.minimize(cost)`: defines the training operation.
- `correct = tf.nn.in_top_k(logits, y, 1)`: defines the accuracy function.
- `accuracy = tf.reduce_mean(tf.cast(correct, tf.float32))`: calculates the mean accuracy.
- `init = tf.global_variables_initializer()`: initializes all the variables.

## Helpful links

- [TensorFlow Tutorials](https://www.tensorflow.org/tutorials/)
- [Getting Started with TensorFlow](https://www.tensorflow.org/get_started/get_started)
- [Neural Networks with TensorFlow](https://www.tensorflow.org/tutorials/layers)

onelinerhub: [How can I create a neural network using Python and TensorFlow?](https://onelinerhub.com/python-tensorflow/how-can-i-create-a-neural-network-using-python-and-tensorflow)
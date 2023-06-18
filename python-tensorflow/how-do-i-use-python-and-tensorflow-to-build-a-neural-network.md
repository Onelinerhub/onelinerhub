# How do I use Python and TensorFlow to build a neural network?
// plain

To use Python and TensorFlow to build a neural network, you first need to create a graph using the TensorFlow library. This graph will define the structure of the neural network. Then, you need to define the layers of the network and the weights associated with them. Finally, you need to define the activation functions for each layer and the optimizer used to optimize the weights.

## Example code

```
import tensorflow as tf

# Define the graph
graph = tf.Graph()

# Define the layers
input_layer = tf.keras.layers.Input(shape=(784,))
hidden_layer_1 = tf.keras.layers.Dense(256, activation='relu')(input_layer)
hidden_layer_2 = tf.keras.layers.Dense(128, activation='relu')(hidden_layer_1)
output_layer = tf.keras.layers.Dense(10, activation='softmax')(hidden_layer_2)

# Define the weights
weights = tf.Variable(tf.random_normal([784, 256]))
bias = tf.Variable(tf.random_normal([256]))

# Define the activation functions
activation_function_1 = tf.nn.relu(tf.matmul(input_layer, weights) + bias)
activation_function_2 = tf.nn.relu(tf.matmul(hidden_layer_1, weights) + bias)

# Define the optimizer
optimizer = tf.train.AdamOptimizer(learning_rate=0.001).minimize(loss)

# Initialize the graph
init = tf.global_variables_initializer()
```

## Code explanation

- `import tensorflow as tf`: This imports the TensorFlow library.
- `graph = tf.Graph()`: This creates a graph object which will define the structure of the neural network.
- `input_layer = tf.keras.layers.Input(shape=(784,))`: This creates an input layer of the neural network with 784 neurons.
- `hidden_layer_1 = tf.keras.layers.Dense(256, activation='relu')(input_layer)`: This creates a hidden layer of the neural network with 256 neurons and the ReLU activation function.
- `output_layer = tf.keras.layers.Dense(10, activation='softmax')(hidden_layer_2)`: This creates an output layer of the neural network with 10 neurons and the Softmax activation function.
- `weights = tf.Variable(tf.random_normal([784, 256]))`: This creates a variable for the weights of the neural network.
- `bias = tf.Variable(tf.random_normal([256]))`: This creates a variable for the bias of the neural network.
- `activation_function_1 = tf.nn.relu(tf.matmul(input_layer, weights) + bias)`: This defines the ReLU activation function for the first layer of the neural network.
- `activation_function_2 = tf.nn.relu(tf.matmul(hidden_layer_1, weights) + bias)`: This defines the ReLU activation function for the second layer of the neural network.
- `optimizer = tf.train.AdamOptimizer(learning_rate=0.001).minimize(loss)`: This defines the optimizer used to optimize the weights of the neural network.
- `init = tf.global_variables_initializer()`: This initializes the graph.

## Helpful links
- [TensorFlow Tutorials](https://www.tensorflow.org/tutorials/)
- [TensorFlow Neural Network Tutorial](https://www.tensorflow.org/tutorials/quickstart/beginner)
- [TensorFlow Documentation](https://www.tensorflow.org/api_docs/)

onelinerhub: [How do I use Python and TensorFlow to build a neural network?](https://onelinerhub.com/python-tensorflow/how-do-i-use-python-and-tensorflow-to-build-a-neural-network)
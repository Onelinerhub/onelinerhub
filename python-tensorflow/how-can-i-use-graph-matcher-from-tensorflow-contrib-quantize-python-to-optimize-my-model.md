# How can I use graph_matcher from tensorflow.contrib.quantize.python to optimize my model?
// plain

`graph_matcher` from `tensorflow.contrib.quantize.python` provides a convenient way to optimize models. It allows you to apply a series of optimizations to the model's graph, such as quantizing weights and replacing certain operations with more efficient ones.

## Example code

```
import tensorflow as tf
from tensorflow.contrib.quantize.python import graph_matcher

g = tf.Graph()
with g.as_default():
  # Create the model
  x = tf.placeholder(tf.float32, shape=[None, 784])
  W = tf.Variable(tf.random_normal([784, 10]))
  b = tf.Variable(tf.zeros([10]))
  y = tf.matmul(x, W) + b

# Match all nodes that have "Variable" as an op
matcher = graph_matcher.GraphMatcher(g, "Variable")

# Apply quantization to all the matched nodes
for match in matcher.match():
  tf.contrib.quantize.create_training_graph(input_graph=g, weight_bits=8)
```

The code above applies quantization to all the variables in the model's graph. This is just one of the optimizations that `graph_matcher` can perform. Other optimizations include replacing operations with more efficient ones, such as replacing `tf.matmul` with `tf.linalg.matmul`.

## Code explanation


1. `import tensorflow as tf`: imports the TensorFlow library.
2. `from tensorflow.contrib.quantize.python import graph_matcher`: imports the graph_matcher module from TensorFlow's contrib library.
3. `g = tf.Graph()`: creates a new graph object.
4. `with g.as_default():`: sets the new graph as the default graph.
5. `x = tf.placeholder(tf.float32, shape=[None, 784])`: creates a placeholder for the input data.
6. `W = tf.Variable(tf.random_normal([784, 10]))`: creates a variable for the weights of the model.
7. `b = tf.Variable(tf.zeros([10]))`: creates a variable for the bias of the model.
8. `y = tf.matmul(x, W) + b`: creates an operation to calculate the output of the model.
9. `matcher = graph_matcher.GraphMatcher(g, "Variable")`: creates a GraphMatcher object to match nodes in the graph.
10. `for match in matcher.match():`: iterates through the matched nodes.
11. `tf.contrib.quantize.create_training_graph(input_graph=g, weight_bits=8)`: applies quantization to the matched nodes.

## Helpful links

- [TensorFlow GraphMatcher API](https://www.tensorflow.org/api_docs/python/tf/contrib/quantize/GraphMatcher)
- [TensorFlow Quantization API](https://www.tensorflow.org/api_docs/python/tf/contrib/quantize)

onelinerhub: [How can I use graph_matcher from tensorflow.contrib.quantize.python to optimize my model?](https://onelinerhub.com/python-tensorflow/how-can-i-use-graph-matcher-from-tensorflow-contrib-quantize-python-to-optimize-my-model)
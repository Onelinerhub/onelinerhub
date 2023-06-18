# How can I use the get_graph attribute in the 'tensorflow.python.keras.backend' module?
// plain

The `get_graph()` attribute is a function within the `tensorflow.python.keras.backend` module that can be used to retrieve the current TensorFlow graph. This is useful in cases where you want to access the TensorFlow graph from within a Keras model, for example to add custom operations.

## Example code

```
import tensorflow as tf
from tensorflow.python.keras.backend import get_graph

graph = get_graph()
print(graph)
```
## Output example

```
<tensorflow.python.framework.ops.Graph object at 0x7f7a7c7fad30>
```

The code above imports the `tensorflow` and `tensorflow.python.keras.backend` modules, then uses the `get_graph()` attribute to retrieve the current TensorFlow graph and assign it to the `graph` variable. The `graph` variable is then printed to the console.

The parts of the code are as follows:
- `import tensorflow as tf`: imports the TensorFlow module and assigns it to the `tf` variable.
- `from tensorflow.python.keras.backend import get_graph`: imports the `get_graph()` attribute from the `tensorflow.python.keras.backend` module.
- `graph = get_graph()`: assigns the current TensorFlow graph to the `graph` variable.
- `print(graph)`: prints the `graph` variable to the console.

## Helpful links
- [TensorFlow Documentation: get_graph()](https://www.tensorflow.org/api_docs/python/tf/keras/backend/get_graph)
- [TensorFlow Documentation: Graph](https://www.tensorflow.org/api_docs/python/tf/Graph)

onelinerhub: [How can I use the get_graph attribute in the 'tensorflow.python.keras.backend' module?](https://onelinerhub.com/python-tensorflow/how-can-i-use-the-get-graph-attribute-in-the--tensorflow-python-keras-backend--module)
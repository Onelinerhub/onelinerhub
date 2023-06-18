# How can I install and use TensorFlow on a Windows machine using Python?
// plain

1. Install Python: First, you need to install Python 3.6 or above from the [Python website](https://www.python.org/).

2. Install TensorFlow: After Python is installed, you can install TensorFlow with the command `pip install tensorflow` in the command line.

3. Test Installation: To test the installation, you can run the following code block:
```
import tensorflow as tf

print(tf.__version__)
```
## Output example
 `2.2.0`

4. Create a Graph: After the installation is verified, you can create a graph in TensorFlow using code such as the following:
```
# Create a graph
g = tf.Graph()

# Establish the graph as the default one
with g.as_default():
  # Assemble a graph consisting of the following three operations:
  #   * Two tf.constant operations to create the operands.
  #   * One tf.add operation to add the two operands.
  x = tf.constant(8, name="x_const")
  y = tf.constant(5, name="y_const")
  my_sum = tf.add(x, y, name="x_y_sum")
```

5. Run the Graph: To run the graph, you can use the following code:
```
# Create a session
with tf.Session() as sess:
  # Run the graph and store the output
  output = sess.run(my_sum)
  print(output)
```
## Output example
 `13`

6. Clean Up: Finally, you can close the session and the graph by running the following code:
```
sess.close()
```

7. Additional Resources: For more information, you can refer to the [TensorFlow documentation](https://www.tensorflow.org/install/pip).

onelinerhub: [How can I install and use TensorFlow on a Windows machine using Python?](https://onelinerhub.com/python-tensorflow/how-can-i-install-and-use-tensorflow-on-a-windows-machine-using-python)
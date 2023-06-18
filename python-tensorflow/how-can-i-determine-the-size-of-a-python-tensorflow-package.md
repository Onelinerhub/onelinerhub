# How can I determine the size of a Python Tensorflow package?
// plain

To determine the size of a Python Tensorflow package, you can use the ```sys.getsizeof()``` method. This method returns the size of an object in bytes.

For example:
```
import sys
import tensorflow as tf

x = tf.random.normal([2, 2])

print(sys.getsizeof(x))
```
## Output example

```
128
```

The code above imports the ```sys``` and ```tensorflow``` modules, then creates a random normal tensor of size 2x2 using ```tf.random.normal()```. Finally, it uses ```sys.getsizeof()``` to determine the size of the tensor, which is 128 bytes.

## Helpful links

- [sys.getsizeof()](https://docs.python.org/3/library/sys.html#sys.getsizeof)
- [TensorFlow](https://www.tensorflow.org/)

onelinerhub: [How can I determine the size of a Python Tensorflow package?](https://onelinerhub.com/python-tensorflow/how-can-i-determine-the-size-of-a-python-tensorflow-package)
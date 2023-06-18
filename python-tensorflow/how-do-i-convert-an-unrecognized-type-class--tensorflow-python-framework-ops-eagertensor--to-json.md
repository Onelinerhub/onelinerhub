# How do I convert an unrecognized type class 'tensorflow.python.framework.ops.eagertensor' to JSON?
// plain

The `tensorflow.python.framework.ops.eagertensor` type class cannot be directly converted to JSON. However, it can be converted to a Python dictionary, which can then be converted to a JSON string.

## Example code

```
import json
import tensorflow as tf

tensor_object = tf.constant([[1, 2], [3, 4]])

# Convert tensor to a numpy array
numpy_array = tensor_object.numpy()

# Convert numpy array to a dictionary
dict_object = numpy_array.tolist()

# Convert dictionary to JSON string
json_string = json.dumps(dict_object)

print(json_string)
```
## Output example

```
[[1, 2], [3, 4]]
```

The code above consists of the following parts:

1. Import the `json` and `tensorflow` modules.
2. Create a `tensor_object` using the `tf.constant` function.
3. Convert the `tensor_object` to a `numpy_array` using the `tensor_object.numpy()` method.
4. Convert the `numpy_array` to a `dict_object` using the `numpy_array.tolist()` method.
5. Convert the `dict_object` to a `json_string` using the `json.dumps()` function.
6. Print the `json_string`.

## Helpful links
- [json.dumps()](https://docs.python.org/3/library/json.html#json.dumps)
- [tf.constant()](https://www.tensorflow.org/api_docs/python/tf/constant)
- [tensor_object.numpy()](https://www.tensorflow.org/api_docs/python/tf/Tensor#numpy)
- [numpy_array.tolist()](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.tolist.html)

onelinerhub: [How do I convert an unrecognized type class 'tensorflow.python.framework.ops.eagertensor' to JSON?](https://onelinerhub.com/python-tensorflow/how-do-i-convert-an-unrecognized-type-class--tensorflow-python-framework-ops-eagertensor--to-json)
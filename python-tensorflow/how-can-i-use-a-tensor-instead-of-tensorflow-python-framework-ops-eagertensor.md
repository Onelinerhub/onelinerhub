# How can I use a tensor instead of TensorFlow.Python.Framework.Ops.EagerTensor?
// plain

Tensor is a data structure used to represent multidimensional data. It is used in deep learning, machine learning and other fields of artificial intelligence. TensorFlow.Python.Framework.Ops.EagerTensor is a library that provides an efficient way to work with tensors.

You can use a tensor without TensorFlow.Python.Framework.Ops.EagerTensor by creating and manipulating tensors directly. For example, the following code creates a 2-dimensional tensor and prints its shape:

```
import numpy as np

# Create a 2-dimensional tensor
tensor = np.array([[1, 2], [3, 4]])

# Print its shape
print(tensor.shape)
```

## Output example

```
(2, 2)
```

The code consists of the following parts:
1. `import numpy as np`: imports the NumPy library, which provides functions for working with arrays and matrices.
2. `tensor = np.array([[1, 2], [3, 4]])`: creates a 2-dimensional array and assigns it to the `tensor` variable.
3. `print(tensor.shape)`: prints the shape of the `tensor` array.

## Helpful links
- [NumPy](https://numpy.org/)
- [TensorFlow.Python.Framework.Ops.EagerTensor](https://www.tensorflow.org/api_docs/python/tf/eager/EagerTensor)

onelinerhub: [How can I use a tensor instead of TensorFlow.Python.Framework.Ops.EagerTensor?](https://onelinerhub.com/python-tensorflow/how-can-i-use-a-tensor-instead-of-tensorflow-python-framework-ops-eagertensor)
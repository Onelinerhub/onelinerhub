# How do I use keras.utils.to_categorical in Python?
// plain

Keras.utils.to_categorical is a utility function used to convert a numerical label vector (integers) to a binary class matrix. This is useful for working with a categorical data set in a neural network.

An example of using this function is shown below:

```
import numpy as np
from keras.utils import to_categorical

# define input data
data = np.array([1, 3, 2, 0, 3, 2, 2, 1, 0, 1])

# one hot encode the data
encoded = to_categorical(data)

print(encoded)
```

## Output example

```
[[0. 1. 0. 0.]
 [0. 0. 0. 1.]
 [0. 0. 1. 0.]
 [1. 0. 0. 0.]
 [0. 0. 0. 1.]
 [0. 0. 1. 0.]
 [0. 0. 1. 0.]
 [0. 1. 0. 0.]
 [1. 0. 0. 0.]
 [0. 1. 0. 0.]]
```

## Code explanation

- `import numpy as np`: import numpy library for array operations.
- `from keras.utils import to_categorical`: import to_categorical function from keras.utils.
- `data = np.array([1, 3, 2, 0, 3, 2, 2, 1, 0, 1])`: define input data.
- `encoded = to_categorical(data)`: one hot encode the data.
- `print(encoded)`: print the encoded data.

## Helpful links
- https://keras.io/utils/#to_categorical
- https://www.tensorflow.org/api_docs/python/tf/keras/utils/to_categorical

onelinerhub: [How do I use keras.utils.to_categorical in Python?](https://onelinerhub.com/python-keras/how-do-i-use-keras-utils-to-categorical-in-python)
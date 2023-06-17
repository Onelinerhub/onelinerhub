# How do I use the to_categorical function in Python Keras?
// plain

The `to_categorical` function in Python Keras is used to convert a class vector (integers) to binary class matrix. This is useful for using with categorical crossentropy loss function, which expects the labels to follow a binary encoding.

## Example

```
from keras.utils import to_categorical

# define example
data = [1, 3, 2, 0, 3, 2, 2, 1, 0, 1]

# one hot encode
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

The `to_categorical` function takes the following parameters:
- `y`: class vector to be converted into a matrix (integers from 0 to num_classes).
- `num_classes`: total number of classes.
- `dtype`: The data type expected by the input, as a string (float32, float64, int32...)

The function returns a binary matrix representation of the input.

## Helpful links
- [Keras Documentation - to_categorical](https://keras.io/utils/#to_categorical)
- [Towards Data Science - One Hot Encoding with Keras](https://towardsdatascience.com/one-hot-encoding-using-keras-to-categorical-dummies-and-how-to-inverse-the-transformation-74466c16ebc5)

onelinerhub: [How do I use the to_categorical function in Python Keras?](https://onelinerhub.com/python-keras/how-do-i-use-the-to-categorical-function-in-python-keras)
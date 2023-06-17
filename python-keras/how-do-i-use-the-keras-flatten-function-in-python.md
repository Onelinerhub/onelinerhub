# How do I use the Keras Flatten function in Python?
// plain

The `Flatten` function in Keras is used to flatten a multi-dimensional tensor into a one-dimensional tensor. It can be used to convert a 2D or 3D tensor into a single vector.

## Example code

```
from keras.layers import Flatten

# Create a 3D tensor
input = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

# Flatten the input tensor
flatten_tensor = Flatten()(input)

# Print the output
print(flatten_tensor)
```

## Output example

```
tf.Tensor([ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18], shape=(18,), dtype=int32)
```

The code above first imports the `Flatten` function from the `keras.layers` library. Then it creates a 3D tensor and passes it as an argument to the `Flatten()` function. The output of the function is a single vector containing all the elements of the 3D tensor.

## Code explanation


1. `from keras.layers import Flatten`: This line imports the `Flatten` function from the `keras.layers` library.

2. `input = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]`: This line creates a 3D tensor.

3. `flatten_tensor = Flatten()(input)`: This line passes the 3D tensor as an argument to the `Flatten()` function and assigns the output to the `flatten_tensor` variable.

4. `print(flatten_tensor)`: This line prints the output of the `Flatten()` function.

## Helpful links

- [Keras Documentation - Flatten](https://keras.io/layers/core/#flatten)

onelinerhub: [How do I use the Keras Flatten function in Python?](https://onelinerhub.com/python-keras/how-do-i-use-the-keras-flatten-function-in-python)
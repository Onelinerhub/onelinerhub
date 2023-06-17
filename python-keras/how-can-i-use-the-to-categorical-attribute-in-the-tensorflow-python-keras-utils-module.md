# How can I use the to_categorical attribute in the tensorflow.python.keras.utils module?
// plain

The `to_categorical()` attribute in the `tensorflow.python.keras.utils` module can be used to convert a class vector (integers) to binary class matrix. This is useful for working with categorical data in machine learning models.

Here is an example of using `to_categorical()`:

```
from tensorflow.python.keras.utils import to_categorical

# example of class vector
y = [0, 1, 2, 2, 1]

# convert to binary class matrix
y_cat = to_categorical(y)
print(y_cat)
```

The output of this code is:

```
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]
 [0. 0. 1.]
 [0. 1. 0.]]
```

The `to_categorical()` attribute takes two parameters:

* `y`: class vector to be converted into a matrix
* `num_classes`: total number of classes

The `y` parameter is the class vector that needs to be converted to a binary class matrix. The `num_classes` parameter is the total number of classes in the data.

## Helpful links

* [tf.keras.utils.to_categorical](https://www.tensorflow.org/api_docs/python/tf/keras/utils/to_categorical)
* [Using Categorical Data in Machine Learning with Python](https://machinelearningmastery.com/how-to-one-hot-encode-sequence-data-in-python/)

onelinerhub: [How can I use the to_categorical attribute in the tensorflow.python.keras.utils module?](https://onelinerhub.com/python-keras/how-can-i-use-the-to-categorical-attribute-in-the-tensorflow-python-keras-utils-module)
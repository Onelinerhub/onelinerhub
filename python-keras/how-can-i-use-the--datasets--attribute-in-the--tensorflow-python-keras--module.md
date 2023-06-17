# How can I use the 'datasets' attribute in the 'tensorflow.python.keras' module?
// plain

The 'datasets' attribute in the 'tensorflow.python.keras' module can be used to access and manipulate datasets. It provides functions to import, preprocess, and load data into a TensorFlow model.

For example, we can use the 'datasets.load_data' function to load the MNIST dataset into a TensorFlow model.

```
from tensorflow.python.keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
```

The above code loads the MNIST dataset into variables `x_train`, `y_train`, `x_test`, and `y_test`.

The 'datasets' attribute also provides functions to preprocess and normalize data. For example, we can use the 'datasets.normalize' function to normalize the MNIST dataset.

```
from tensorflow.python.keras.datasets import normalize

x_train = normalize(x_train)
x_test = normalize(x_test)
```

The above code normalizes the MNIST dataset stored in the `x_train` and `x_test` variables.

The 'datasets' attribute can also be used to access and manipulate other datasets, such as the CIFAR-10 dataset.

## Helpful links
- [TensorFlow Datasets](https://www.tensorflow.org/datasets)
- [Keras Datasets](https://keras.io/datasets/)

onelinerhub: [How can I use the 'datasets' attribute in the 'tensorflow.python.keras' module?](https://onelinerhub.com/python-keras/how-can-i-use-the--datasets--attribute-in-the--tensorflow-python-keras--module)
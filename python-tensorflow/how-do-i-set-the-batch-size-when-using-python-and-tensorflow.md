# How do I set the batch size when using Python and TensorFlow?
// plain

In Python and TensorFlow, the batch size is set using the `batch_size` parameter when constructing the `tf.data.Dataset` object.

For example, if we have a dataset of size 10, we can set the batch size to 3 as follows:

```
dataset = tf.data.Dataset.range(10)
dataset = dataset.batch(3)
```

The output of this code will be a `tf.data.Dataset` object with 4 batches of size 3.

## Code explanation


1. `tf.data.Dataset.range(10)`: This creates a `tf.data.Dataset` object with 10 elements.

2. `dataset.batch(3)`: This sets the batch size of the dataset to 3.

## Helpful links
* [TensorFlow Documentation](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#batch)

onelinerhub: [How do I set the batch size when using Python and TensorFlow?](https://onelinerhub.com/python-tensorflow/how-do-i-set-the-batch-size-when-using-python-and-tensorflow)
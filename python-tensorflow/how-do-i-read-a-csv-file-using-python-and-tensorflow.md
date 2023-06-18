# How do I read a CSV file using Python and TensorFlow?
// plain

Reading a CSV file using Python and TensorFlow is quite simple. The following example code block demonstrates how to read a CSV file and load it into a TensorFlow dataset:

```python
import tensorflow as tf

# Create a TensorFlow dataset object from the CSV file
dataset = tf.data.experimental.make_csv_dataset(
    'my_file.csv',
    batch_size=32,
    label_name='target'
)

# Print the first batch of data
for features, label in dataset.take(1):
    print("Features:", features)
    print("Label:", label)
```

## Output example

```
Features: {'feature1': <tf.Tensor: shape=(32,), dtype=float32, numpy=
array([1.2, 0.4, 3.5, ..., 0.9, 0.2, 1.7], dtype=float32)>, 'feature2': <tf.Tensor: shape=(32,), dtype=float32, numpy=
array([0.4, 0.9, 0.2, ..., 0.2, 0.5, 0.6], dtype=float32)>}
Label: <tf.Tensor: shape=(32,), dtype=int32, numpy=array([1, 0, 0, ..., 0, 1, 0], dtype=int32)>
```

The code consists of the following parts:
1. Importing the TensorFlow library.
2. Creating a TensorFlow dataset object from the CSV file.
3. Looping through the dataset to print the first batch of data.

For more information on how to read a CSV file using Python and TensorFlow, please refer to the [TensorFlow documentation](https://www.tensorflow.org/guide/data).

onelinerhub: [How do I read a CSV file using Python and TensorFlow?](https://onelinerhub.com/python-tensorflow/how-do-i-read-a-csv-file-using-python-and-tensorflow)
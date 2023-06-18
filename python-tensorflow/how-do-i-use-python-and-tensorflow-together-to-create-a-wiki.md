# How do I use Python and TensorFlow together to create a Wiki?
// plain

Python and TensorFlow can be used together to create a Wiki.

## Example code

```
import tensorflow as tf
import numpy as np

wiki_data = np.array([[1,2,3],
                      [4,5,6],
                      [7,8,9]])

wiki_tensor = tf.convert_to_tensor(wiki_data, dtype=tf.float32)

with tf.Session() as sess:
    print(sess.run(wiki_tensor))

```

## Output example

```
[[1. 2. 3.]
 [4. 5. 6.]
 [7. 8. 9.]]
```

The code above creates a Wiki by using `import tensorflow as tf` to import the TensorFlow library, `import numpy as np` to import the NumPy library, `wiki_data = np.array([[1,2,3], [4,5,6], [7,8,9]])` to create an array of values, `wiki_tensor = tf.convert_to_tensor(wiki_data, dtype=tf.float32)` to convert the array into a tensor, and `with tf.Session() as sess: print(sess.run(wiki_tensor))` to run the tensor and print the output.

## Helpful links

- [TensorFlow Documentation](https://www.tensorflow.org/api_docs/python/tf)
- [Numpy Documentation](https://docs.scipy.org/doc/numpy/reference/)

onelinerhub: [How do I use Python and TensorFlow together to create a Wiki?](https://onelinerhub.com/python-tensorflow/how-do-i-use-python-and-tensorflow-together-to-create-a-wiki)
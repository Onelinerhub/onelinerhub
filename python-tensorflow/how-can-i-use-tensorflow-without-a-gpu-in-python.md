# How can I use TensorFlow without a GPU in Python?
// plain

TensorFlow can be used without a GPU in Python by using the CPU as the device for computation. To do this, you must set the `device` parameter of the `tf.Session()` to `/cpu:0` when creating the TensorFlow session.

## Example code


```
import tensorflow as tf

# Create the session
sess = tf.Session(config=tf.ConfigProto(device_count={'GPU': 0}))

# Run computation
result = sess.run(...)
```

## Code explanation

- `import tensorflow as tf`: imports the TensorFlow library.
- `tf.Session()`: creates the session with the `config` parameter set to `tf.ConfigProto(device_count={'GPU': 0})` to disable the GPU and use the CPU instead.
- `sess.run(...)`: runs the computation.

## Helpful links
- [TensorFlow documentation on using GPUs](https://www.tensorflow.org/guide/using_gpu)
- [TensorFlow documentation on configuring sessions](https://www.tensorflow.org/api_docs/python/tf/Session#__init__)

onelinerhub: [How can I use TensorFlow without a GPU in Python?](https://onelinerhub.com/python-tensorflow/how-can-i-use-tensorflow-without-a-gpu-in-python)
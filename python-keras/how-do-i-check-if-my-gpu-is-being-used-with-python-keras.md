# How do I check if my GPU is being used with Python Keras?
// plain

To check if your GPU is being used with Python Keras, you can use the following code:

```
from keras import backend as K
K.tensorflow_backend._get_available_gpus()
```

This will output a list of available GPUs if any. For example, if you have an NVIDIA GPU installed, the output will look like this:

```
['/gpu:0']
```

The code works by using the `Keras` backend module to access the `tensorflow_backend` module. The `_get_available_gpus()` method is then used to check for available GPUs.

If you don't have a GPU installed, or if the GPU is not being detected, the output will be an empty list `[]`.

## Code explanation

- `from keras import backend as K`: imports the `Keras` backend module as `K`
- `K.tensorflow_backend._get_available_gpus()`: calls the `tensorflow_backend` module and uses the `_get_available_gpus()` method to check for available GPUs

## Helpful links
- [Keras Backend Documentation](https://keras.io/backend/)
- [TensorFlow Backend Documentation](https://www.tensorflow.org/api_docs/python/tf/keras/backend)

onelinerhub: [How do I check if my GPU is being used with Python Keras?](https://onelinerhub.com/python-keras/how-do-i-check-if-my-gpu-is-being-used-with-python-keras)
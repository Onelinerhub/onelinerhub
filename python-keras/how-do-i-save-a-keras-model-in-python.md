# How do I save a Keras model in Python?
// plain

Keras models can be saved in Python using the `model.save()` method. This method saves the architecture, weights, and training configuration of a model in a single `HDF5` file.

## Example code

```
from keras.models import load_model

model.save('model.h5')
```

This will create a single `HDF5` file called `model.h5` in the current working directory. The model can be reinstantiated at any time by calling the `load_model()` function with the path to the `HDF5` file as an argument.

## Example code

```
from keras.models import load_model

model = load_model('model.h5')
```

The `load_model()` function returns a compiled model identical to the original, including weights and training configuration.

## Code explanation

1. `model.save()`: Saves the architecture, weights, and training configuration of a model in a single `HDF5` file.
2. `load_model()`: Loads a compiled model including weights and training configuration.

## Helpful links
- [Keras Documentation: Save and serialize models](https://keras.io/getting-started/faq/#how-can-i-save-a-keras-model)

onelinerhub: [How do I save a Keras model in Python?](https://onelinerhub.com/python-keras/how-do-i-save-a-keras-model-in-python)
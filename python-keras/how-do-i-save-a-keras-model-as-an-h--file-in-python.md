# How do I save a Keras model as an H5 file in Python?
// plain

To save a Keras model as an H5 file in Python, you need to use the `model.save()` method. This method takes the path to the file as an argument and saves the model as an HDF5 file. The following example code saves a Keras model to an H5 file:

```
from keras.models import Sequential
from keras.layers import Dense

# Create the model
model = Sequential()
model.add(Dense(2, input_dim=3, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Save the model as an H5 file
model.save('model.h5')
```

The above code will save the model as an H5 file named `model.h5` in the current working directory.

## Code explanation

- `from keras.models import Sequential`: imports the `Sequential` model from the `keras.models` module.
- `from keras.layers import Dense`: imports the `Dense` layer from the `keras.layers` module.
- `model = Sequential()`: creates a `Sequential` model object.
- `model.add(Dense(2, input_dim=3, activation='relu'))`: adds a `Dense` layer to the model with 2 nodes, 3 input dimensions and a ReLU activation function.
- `model.add(Dense(1, activation='sigmoid'))`: adds a `Dense` layer to the model with 1 node and a sigmoid activation function.
- `model.save('model.h5')`: saves the model as an H5 file named `model.h5` in the current working directory.

## Helpful links
- [Keras Documentation - Model Saving](https://keras.io/getting-started/faq/#how-can-i-save-a-keras-model)

onelinerhub: [How do I save a Keras model as an H5 file in Python?](https://onelinerhub.com/python-keras/how-do-i-save-a-keras-model-as-an-h--file-in-python)
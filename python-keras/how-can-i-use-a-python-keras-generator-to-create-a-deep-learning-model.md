# How can I use a Python Keras Generator to create a deep learning model?
// plain

A Python Keras Generator can be used to create a deep learning model by defining a generator function that yields batches of training data. The generator can be used as an input to the `fit_generator` function of the Keras Model class.

For example, the following code snippet defines a generator that yields batches of data and labels:

```
def data_generator(data, labels, batch_size):
    while True:
        # Get a random set of indices for the batch
        indices = np.random.randint(data.shape[0], size=batch_size)
        # Get the data and labels for the batch
        X, y = data[indices], labels[indices]
        yield X, y
```

The generator can then be used as an input to the `fit_generator` function of the Keras Model class, as shown in the following example:

```
model.fit_generator(data_generator(X_train, y_train, batch_size=32),
                    steps_per_epoch=len(X_train) // batch_size,
                    epochs=10)
```

The code above will train the model for 10 epochs, using batches of 32 samples each.

Parts of the code:

- `data_generator`: Function that yields batches of training data.
- `np.random.randint`: Function to generate a random set of indices for the batch.
- `data[indices]`: Get the data for the batch.
- `labels[indices]`: Get the labels for the batch.
- `yield X, y`: Yield the batch of data and labels.
- `fit_generator`: Function to fit the model with generator as input.
- `steps_per_epoch`: Number of steps (batches of samples) to yield from generator before declaring one epoch finished.
- `epochs`: Number of epochs to train the model.

## Helpful links

- [Keras documentation - fit_generator](https://keras.io/models/model/#fit_generator)
- [Keras documentation - Writing your own generators](https://keras.io/models/model/#writing-your-own-generators)

onelinerhub: [How can I use a Python Keras Generator to create a deep learning model?](https://onelinerhub.com/python-keras/how-can-i-use-a-python-keras-generator-to-create-a-deep-learning-model)
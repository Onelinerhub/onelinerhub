# How do I set the batch size when using Python and Keras?
// plain

The batch size is an important hyperparameter that controls the number of samples propagated through the network before the weights are updated.

In Python and Keras, the batch size can be set using the `batch_size` argument of the `fit()` method.

For example, if we want to set the batch size to 32, we can do so as follows:

```
model.fit(x_train, y_train, batch_size=32)
```

The `batch_size` argument can also be passed to the `fit_generator()` method if using a generator to supply data.

```
model.fit_generator(generator, batch_size=32)
```

The batch size can also be set when creating the model. For example, if we are using a Sequential model, we can pass the `batch_input_shape` argument to specify the batch size.

```
model = Sequential(batch_input_shape=(32, x_train.shape[1], x_train.shape[2]))
```

## Helpful links
- [Keras Documentation - fit](https://keras.io/models/model/#fit)
- [Keras Documentation - fit_generator](https://keras.io/models/model/#fit_generator)
- [Keras Documentation - Sequential](https://keras.io/models/sequential/)

onelinerhub: [How do I set the batch size when using Python and Keras?](https://onelinerhub.com/python-keras/how-do-i-set-the-batch-size-when-using-python-and-keras)
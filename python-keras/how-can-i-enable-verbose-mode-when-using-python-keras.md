# How can I enable verbose mode when using Python Keras?
// plain

Verbose mode in Python Keras can be enabled by setting the verbose parameter to 1 or 2. The verbose parameter determines the amount of information that is displayed during training.

Setting verbose to 1 will print out a progress bar and a one-line summary for each epoch.

Setting verbose to 2 will print out more detailed information about the training process, such as the number of batches processed and the time taken for each epoch.

## Example code

```
model.fit(X_train, y_train, verbose=1)
```

## Output example

```
Epoch 1/10
1875/1875 [==============================] - 7s 4ms/step - loss: 0.3281
```

The verbose parameter can also be a function that takes in the logs dictionary as an argument and prints out the desired information.

## Example code

```
def verbose_print(logs):
    print(f"loss: {logs['loss']}")

model.fit(X_train, y_train, verbose=verbose_print)
```

## Output example

```
loss: 0.3281
```

## Helpful links
- [Keras Documentation: verbose](https://keras.io/models/model/#fit)
- [Keras Tutorial: Verbosity Mode](https://www.tensorflow.org/guide/keras/train_and_evaluate#verbosity_mode)

onelinerhub: [How can I enable verbose mode when using Python Keras?](https://onelinerhub.com/python-keras/how-can-i-enable-verbose-mode-when-using-python-keras)
# How do I save weights in a Python Keras model?
// plain

The weights of a Keras model can be saved in two ways:
1. **Saving the entire model**: This will save the model's architecture, weights, and training configuration in a single file. This can be done using the `model.save()` method.

## Example code

```
model.save('model.h5')
```

2. **Saving only the weights**: This will only save the weights of the model, and not its architecture or training configuration. This can be done using the `model.save_weights()` method.

## Example code

```
model.save_weights('weights.h5')
```

## Helpful links
- [Keras Documentation - Save and Restore](https://keras.io/getting-started/faq/#how-can-i-save-a-keras-model)

onelinerhub: [How do I save weights in a Python Keras model?](https://onelinerhub.com/python-keras/how-do-i-save-weights-in-a-python-keras-model)
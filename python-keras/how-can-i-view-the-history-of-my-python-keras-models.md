# How can I view the history of my Python Keras models?
// plain

To view the history of your Python Keras models, you can use the `model.fit()` method. This method takes in the training and validation data, and returns a `History` object. The `History` object contains a record of all the metrics that were measured during the training process.

## Example code

```python
history = model.fit(X_train, y_train,
                    batch_size=32,
                    epochs=10,
                    validation_data=(X_val, y_val))
```

The `History` object has a `history` attribute that contains a dictionary with all the metrics that were measured during training.

## Example code

```python
print(history.history)
```

## Output example

```
{'val_loss': [0.9031, 0.7456, 0.6854, 0.6458, 0.6185, 0.5989, 0.5839, 0.5722, 0.5646, 0.5584],
 'val_accuracy': [0.7296, 0.7736, 0.7912, 0.8024, 0.8104, 0.816, 0.8208, 0.8236, 0.8264, 0.8296],
 'loss': [1.1817, 0.826, 0.7187, 0.6546, 0.6062, 0.5726, 0.5461, 0.5262, 0.5114, 0.4993],
 'accuracy': [0.6354, 0.7582, 0.7862, 0.8062, 0.822, 0.8324, 0.8412, 0.8468, 0.8518, 0.856]}
```

You can also access the metrics individually, such as loss and accuracy, using the `history.history['loss']` and `history.history['accuracy']` methods.

## Code explanation

1. model.fit() - method to train the model
2. History object - contains a record of all metrics measured during training
3. history.history - attribute of the History object, contains a dictionary of all metrics measured during training
4. history.history['loss'] and history.history['accuracy'] - methods to access individual metrics

## Helpful links
- [Keras Documentation - Model Training History](https://keras.io/api/models/model_training_apis/#history-method)

onelinerhub: [How can I view the history of my Python Keras models?](https://onelinerhub.com/python-keras/how-can-i-view-the-history-of-my-python-keras-models)
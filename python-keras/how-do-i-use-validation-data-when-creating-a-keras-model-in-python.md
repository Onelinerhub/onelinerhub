# How do I use validation_data when creating a Keras model in Python?
// plain

When creating a Keras model in Python, validation_data can be used to evaluate the model's performance on unseen data. Validation_data is a tuple consisting of input data and labels. The input data should be provided in the same format as the training data. The labels should be provided as a one-dimensional array.

## Example

```
# Create a model
model = Sequential()
model.add(Dense(32, input_dim=30))
model.add(Activation('relu'))
model.add(Dense(1))
model.add(Activation('sigmoid'))
model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])
# Fit the model
model.fit(X_train, y_train, validation_data=(X_val, y_val))
```
## Output example

```
Train on 8000 samples, validate on 2000 samples
Epoch 1/10
8000/8000 [==============================] - 1s 125us/step - loss: 0.6156 - acc: 0.6778 - val_loss: 0.5307 - val_acc: 0.7495
Epoch 2/10
8000/8000 [==============================] - 0s 57us/step - loss: 0.5138 - acc: 0.7478 - val_loss: 0.4820 - val_acc: 0.7745
```

## Code explanation

- `model = Sequential()`: This line creates a Sequential model.
- `model.add(Dense(32, input_dim=30))`: This line adds a Dense layer with 32 nodes and an input dimension of 30.
- `model.add(Activation('relu'))`: This line adds an activation layer with the ReLU activation function.
- `model.add(Dense(1))`: This line adds a Dense layer with 1 node.
- `model.add(Activation('sigmoid'))`: This line adds an activation layer with the sigmoid activation function.
- `model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])`: This line compiles the model with the RMSprop optimizer, binary crossentropy loss, and accuracy metrics.
- `model.fit(X_train, y_train, validation_data=(X_val, y_val))`: This line fits the model to the training data with the validation_data tuple.

## Helpful links
- [Keras Documentation: Model Training](https://keras.io/getting-started/sequential-model-guide/#model-training)
- [Keras Documentation: Sequential Model](https://keras.io/getting-started/sequential-model-guide/)

onelinerhub: [How do I use validation_data when creating a Keras model in Python?](https://onelinerhub.com/python-keras/how-do-i-use-validation-data-when-creating-a-keras-model-in-python)
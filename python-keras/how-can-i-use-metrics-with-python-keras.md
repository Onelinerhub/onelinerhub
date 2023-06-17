# How can I use metrics with Python Keras?
// plain

Using metrics with Python Keras is easy. The Keras library provides a number of metrics that can be used to evaluate a model. These include accuracy, precision, recall, AUC, and F1 score. To use a metric, you need to specify it when you compile the model.

```
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy', 'precision'])
```

This code snippet compiles a model using the Adam optimizer and binary cross-entropy loss, and evaluates it using accuracy and precision metrics.

The metrics are then available to view when the model is fit.

```
model.fit(X_train, y_train, epochs=10)

# Output
Epoch 1/10
9000/9000 [==============================] - 0s 48us/step - loss: 0.3490 - accuracy: 0.8556 - precision: 0.8846
Epoch 2/10
9000/9000 [==============================] - 0s 32us/step - loss: 0.1759 - accuracy: 0.9357 - precision: 0.9477
```

The output shows the loss, accuracy, and precision values for each epoch.

The Keras library also provides a number of other metrics that can be used to evaluate a model, such as recall, AUC, and F1 score.

## Code explanation


1. `model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy', 'precision'])`: This line of code compiles the model using the Adam optimizer and binary cross-entropy loss, and evaluates it using accuracy and precision metrics.

2. `model.fit(X_train, y_train, epochs=10)`: This line of code fits the model to the training data for 10 epochs.

3. `Epoch 1/10 9000/9000 [==============================] - 0s 48us/step - loss: 0.3490 - accuracy: 0.8556 - precision: 0.8846`: This line of output shows the loss, accuracy, and precision values for the first epoch.

## Helpful links

- [Keras Metrics](https://keras.io/metrics/)
- [Keras Model Compilation](https://keras.io/models/model/#compile)
- [Keras Model Training](https://keras.io/models/model/#fit)

onelinerhub: [How can I use metrics with Python Keras?](https://onelinerhub.com/python-keras/how-can-i-use-metrics-with-python-keras)
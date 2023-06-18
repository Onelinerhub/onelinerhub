# How do I use the model.fit method in Python Tensorflow?
// plain

The `model.fit()` method in Python TensorFlow is used to train a model. It takes in the input features and labels, and then fits the model to the data. To use the `model.fit()` method, you must first create a model and compile it. Then, you can call the `model.fit()` method and pass in the training data.

## Example code

```
model = Sequential()
model.add(Dense(32, activation='relu', input_dim=784))
model.add(Dense(10, activation='softmax'))
model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Train the model, iterating on the data in batches of 32 samples
model.fit(x_train, y_train, epochs=10, batch_size=32)
```

This code will train the model on the data `x_train` and `y_train` for 10 epochs, with a batch size of 32.

Parts of the code:
* `model = Sequential()` - This creates a new Sequential model.
* `model.add(Dense(32, activation='relu', input_dim=784))` - This adds a fully-connected layer with 32 units and ReLU activation to the model.
* `model.add(Dense(10, activation='softmax'))` - This adds a fully-connected layer with 10 units and a softmax activation to the model.
* `model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])` - This compiles the model with the RMSprop optimizer, the categorical cross-entropy loss function, and accuracy as the metric.
* `model.fit(x_train, y_train, epochs=10, batch_size=32)` - This fits the model to the training data for 10 epochs, with a batch size of 32.

## Helpful links
* [TensorFlow Documentation - Model Training](https://www.tensorflow.org/guide/keras/train_and_evaluate)
* [TensorFlow Documentation - Sequential Model](https://www.tensorflow.org/guide/keras/sequential_model)

onelinerhub: [How do I use the model.fit method in Python Tensorflow?](https://onelinerhub.com/python-tensorflow/how-do-i-use-the-model-fit-method-in-python-tensorflow)
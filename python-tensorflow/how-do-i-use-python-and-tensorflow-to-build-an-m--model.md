# How do I use Python and TensorFlow to build an M1 model?
// plain

To use Python and TensorFlow to build an M1 model, you will need to install the TensorFlow library. Once installed, you can use the following example code to create and train a basic M1 model:

```
import tensorflow as tf

# Create the model
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=5)

# Evaluate the model
model.evaluate(x_test, y_test)
```

The code above creates a basic M1 model in TensorFlow using the Sequential model API. The first line imports the TensorFlow library, followed by the creation of the model. The model consists of a flatten layer, a Dense layer with 128 nodes and a ReLU activation function, and a Dense layer with 10 nodes and a Softmax activation function. The model is then compiled using an Adam optimizer, a sparse categorical crossentropy loss function, and accuracy as a metric. The model is then trained using the x_train and y_train data for 5 epochs, and finally evaluated using the x_test and y_test data.

## Code explanation


1. `import tensorflow as tf`: imports the TensorFlow library.
2. `model = tf.keras.models.Sequential([`: creates a Sequential model.
3. `tf.keras.layers.Flatten(input_shape=(28, 28))`: creates a flatten layer with an input shape of 28x28.
4. `tf.keras.layers.Dense(128, activation='relu')`: creates a Dense layer with 128 nodes and a ReLU activation function.
5. `tf.keras.layers.Dense(10, activation='softmax')`: creates a Dense layer with 10 nodes and a Softmax activation function.
6. `model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])`: compiles the model using an Adam optimizer, a sparse categorical crossentropy loss function, and accuracy as a metric.
7. `model.fit(x_train, y_train, epochs=5)`: trains the model using the x_train and y_train data for 5 epochs.
8. `model.evaluate(x_test, y_test)`: evaluates the model using the x_test and y_test data.

## Helpful links

- [TensorFlow Tutorials](https://www.tensorflow.org/tutorials)
- [TensorFlow Keras Guide](https://www.tensorflow.org/guide/keras)

onelinerhub: [How do I use Python and TensorFlow to build an M1 model?](https://onelinerhub.com/python-tensorflow/how-do-i-use-python-and-tensorflow-to-build-an-m--model)
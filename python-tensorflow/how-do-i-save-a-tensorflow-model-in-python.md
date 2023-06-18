# How do I save a TensorFlow model in Python?
// plain

Saving a TensorFlow model in Python is easy and straightforward. The following example code shows how to save a model in TensorFlow:

```
# Create and train a model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(4,))
])
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(X_train, y_train, epochs=5)

# Save the model
model.save('my_model.h5')
```

This will save the model as an HDF5 file called `my_model.h5`. The code can be broken down into the following parts:

1. `tf.keras.Sequential()`: This creates a `Sequential` model in TensorFlow.
2. `tf.keras.layers.Dense()`: This adds a densely-connected layer to the model.
3. `model.compile()`: This compiles the model with the given optimizer, loss, and metrics.
4. `model.fit()`: This fits the model to the training data.
5. `model.save()`: This saves the model as an HDF5 file.

For more information, see the [TensorFlow documentation](https://www.tensorflow.org/guide/keras/save_and_serialize).

onelinerhub: [How do I save a TensorFlow model in Python?](https://onelinerhub.com/python-tensorflow/how-do-i-save-a-tensorflow-model-in-python)
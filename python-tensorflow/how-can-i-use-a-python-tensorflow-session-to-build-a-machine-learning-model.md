# How can I use a Python TensorFlow session to build a machine learning model?
// plain

Using Python TensorFlow, you can build a machine learning model by first defining the model's architecture. This can be done using the `tf.keras.Sequential` API. For example:

```
model = tf.keras.Sequential([
  tf.keras.layers.Dense(128, activation='relu', input_shape=(784,)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dense(10, activation='softmax')
])
```

The above code creates a model with three layers:

1. A `Dense` layer with 128 neurons and the `relu` activation function. The `input_shape` parameter specifies the shape of the input data (784 in this case).

2. A second `Dense` layer with 128 neurons and the `relu` activation function.

3. A third `Dense` layer with 10 neurons and the `softmax` activation function.

Once the model's architecture is defined, you can compile it by specifying the optimizer and loss function. For example:

```
model.compile(
  optimizer='sgd',
  loss='categorical_crossentropy',
  metrics=['accuracy']
)
```

The above code compiles the model with the `sgd` optimizer and `categorical_crossentropy` loss function. It also specifies the `accuracy` metric to be used for evaluation.

Finally, you can train the model using the `model.fit` API. For example:

```
model.fit(x_train, y_train, epochs=5)
```

The above code trains the model on the training data (`x_train` and `y_train`) for 5 epochs.

## Helpful links

- [TensorFlow Keras Sequential API](https://www.tensorflow.org/api_docs/python/tf/keras/Sequential)
- [TensorFlow Compile API](https://www.tensorflow.org/api_docs/python/tf/keras/Model#compile)
- [TensorFlow Fit API](https://www.tensorflow.org/api_docs/python/tf/keras/Model#fit)

onelinerhub: [How can I use a Python TensorFlow session to build a machine learning model?](https://onelinerhub.com/python-tensorflow/how-can-i-use-a-python-tensorflow-session-to-build-a-machine-learning-model)
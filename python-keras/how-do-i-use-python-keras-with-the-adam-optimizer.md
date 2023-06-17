# How do I use Python Keras with the Adam optimizer?
// plain

Keras is a high-level neural networks API, written in Python and capable of running on top of TensorFlow, CNTK, or Theano. One of the most popular optimization algorithms used with Keras is the Adam optimizer.

To use the Adam optimizer with Keras, you need to specify it when compiling the model. The following example shows how to compile a model with the Adam optimizer:

```
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
```

The Adam optimizer has several parameters, such as the learning rate, which can be specified when compiling the model. The following example shows how to specify the learning rate when compiling the model with the Adam optimizer:

```
model.compile(loss='categorical_crossentropy',
              optimizer=Adam(lr=0.001),
              metrics=['accuracy'])
```

## Code explanation


- `model.compile()`: This is a method of the Keras Model class that is used to compile the model with the specified loss function, optimizer, and metrics.

- `optimizer='adam'`: This is the parameter that specifies the optimizer to be used when compiling the model. In this case, it is set to the string 'adam' to indicate that the Adam optimizer should be used.

- `Adam(lr=0.001)`: This is an instance of the Adam optimizer class that is used to specify the learning rate when compiling the model. In this case, the learning rate is set to 0.001.

The following is a list of ## Helpful links

- [Keras Documentation - Optimizers](https://keras.io/optimizers/)
- [Keras Documentation - Model Compilation](https://keras.io/models/model/#compile)
- [TensorFlow Documentation - Adam Optimizer](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adam)

onelinerhub: [How do I use Python Keras with the Adam optimizer?](https://onelinerhub.com/python-keras/how-do-i-use-python-keras-with-the-adam-optimizer)
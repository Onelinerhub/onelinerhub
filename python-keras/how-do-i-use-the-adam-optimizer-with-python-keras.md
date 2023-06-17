# How do I use the Adam optimizer with Python Keras?
// plain

The Adam optimizer is a popular optimization algorithm for training deep learning models in Python Keras. It is an extension of the stochastic gradient descent algorithm that is based on adaptive estimation of first-order and second-order moments.

To use the Adam optimizer with Python Keras, you first need to import the Adam optimizer class from the Keras library:
```
from keras.optimizers import Adam
```

You then need to instantiate the Adam optimizer object with desired parameters such as learning rate, decay rate, and momentum:
```
opt = Adam(lr=0.001, decay=1e-6, momentum=0.9)
```

Finally, you need to compile your model with the Adam optimizer object:
```
model.compile(loss='binary_crossentropy', optimizer=opt, metrics=['accuracy'])
```

## Code explanation


1. `from keras.optimizers import Adam`: This imports the Adam optimizer class from the Keras library.
2. `opt = Adam(lr=0.001, decay=1e-6, momentum=0.9)`: This instantiates the Adam optimizer object with the given parameters.
3. `model.compile(loss='binary_crossentropy', optimizer=opt, metrics=['accuracy'])`: This compiles the model with the Adam optimizer object.

## Helpful links

- [Keras Documentation - Optimizers](https://keras.io/optimizers/)
- [Understanding the Concept of Learning Rate Decay](https://towardsdatascience.com/understanding-the-concept-of-learning-rate-decay-3d2e6f7d6d7f)

onelinerhub: [How do I use the Adam optimizer with Python Keras?](https://onelinerhub.com/python-keras/how-do-i-use-the-adam-optimizer-with-python-keras)
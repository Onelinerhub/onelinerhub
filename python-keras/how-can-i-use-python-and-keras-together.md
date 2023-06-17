# How can I use Python and Keras together?
// plain

Python and Keras can be used together to create powerful deep learning models. Keras is a high-level API written in Python that can be used to quickly build and train deep learning models. It is built on top of popular deep learning libraries such as TensorFlow, Theano, and CNTK.

Example code using Python and Keras to create a simple neural network:

```
# Import necessary libraries
import numpy as np
from keras.models import Sequential
from keras.layers import Dense

# Create the model
model = Sequential()
model.add(Dense(units=64, activation='relu', input_dim=100))
model.add(Dense(units=10, activation='softmax'))

# Compile the model
model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=5, batch_size=32)
```

This code creates a simple neural network using Python and Keras. First, the necessary libraries are imported. Then, a Sequential model is created and layers are added. The model is then compiled with a loss function, optimizer, and metrics. Finally, the model is trained with the training data.

## Code explanation

1. Import necessary libraries
2. Create the model
3. Compile the model
4. Train the model

## Helpful links
- [Keras Documentation](https://keras.io/)
- [TensorFlow Documentation](https://www.tensorflow.org/guide)
- [Theano Documentation](http://deeplearning.net/software/theano/)
- [CNTK Documentation](https://docs.microsoft.com/en-us/cognitive-toolkit/)

onelinerhub: [How can I use Python and Keras together?](https://onelinerhub.com/python-keras/how-can-i-use-python-and-keras-together)
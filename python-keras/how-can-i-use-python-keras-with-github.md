# How can I use Python Keras with Github?
// plain

Using Python Keras with Github is a great way to collaborate on deep learning projects. To do this, you will need to first install Keras with Python. Then, create a Github repository and clone it to your local machine.

Once you have the repository setup, you can start writing your deep learning code in Python with Keras. Here is an example of a simple Keras model:

```
from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
model.add(Dense(units=64, activation='relu', input_dim=100))
model.add(Dense(units=10, activation='softmax'))
model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])
```

This code creates a neural network with one hidden layer of 64 neurons and one output layer of 10 neurons.

Once your code is ready, you can commit and push it to Github. This will allow you to collaborate with other developers and share your work.

## Code explanation

- from keras.models import Sequential: imports the Sequential class from the keras.models module
- from keras.layers import Dense: imports the Dense class from the keras.layers module
- model = Sequential(): creates a Sequential model object
- model.add(Dense(units=64, activation='relu', input_dim=100)): adds a Dense layer to the model with 64 neurons, a ReLU activation function, and an input dimension of 100
- model.add(Dense(units=10, activation='softmax')): adds a Dense layer to the model with 10 neurons and a Softmax activation function
- model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy']): compiles the model with a categorical cross entropy loss function, an SGD optimizer, and an accuracy metric

## Helpful links
- Keras documentation: https://keras.io/
- Github: https://github.com/

onelinerhub: [How can I use Python Keras with Github?](https://onelinerhub.com/python-keras/how-can-i-use-python-keras-with-github)
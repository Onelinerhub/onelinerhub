# How do I create a Python Keras model?
// plain

Creating a Keras model in Python is a straightforward process. First, import the necessary libraries:
```
import keras
from keras.models import Sequential
from keras.layers import Dense
```
Then, define the model architecture:
```
model = Sequential()
model.add(Dense(units=64, activation='relu', input_dim=100))
model.add(Dense(units=10, activation='softmax'))
```
The first layer has 64 nodes, a ReLU activation, and takes input of dimension 100. The second layer has 10 nodes and a Softmax activation.

Next, compile the model:
```
model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])
```
This specifies the loss function, optimizer, and metrics for the model.

Finally, train the model:
```
model.fit(x_train, y_train, epochs=5, batch_size=32)
```
This trains the model on the training data for 5 epochs with a batch size of 32.

The complete code should look something like this:
```
import keras
from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
model.add(Dense(units=64, activation='relu', input_dim=100))
model.add(Dense(units=10, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5, batch_size=32)
```

## Helpful links
- [Keras Documentation](https://keras.io/)
- [Getting Started with Keras](https://keras.io/getting-started/sequential-model-guide/)

onelinerhub: [How do I create a Python Keras model?](https://onelinerhub.com/python-keras/how-do-i-create-a-python-keras-model)
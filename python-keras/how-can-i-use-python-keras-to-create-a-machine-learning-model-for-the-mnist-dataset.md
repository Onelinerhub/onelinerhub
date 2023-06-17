# How can I use Python Keras to create a machine learning model for the MNIST dataset?
// plain

To use Python Keras to create a machine learning model for the MNIST dataset, you can follow the steps below:

1. Import the necessary libraries:
```python
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
```

2. Load the data:
```python
(x_train, y_train), (x_test, y_test) = mnist.load_data()
```

3. Preprocess the data:
```python
x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255
```

4. Create the model:
```python
model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(784,)))
model.add(Dense(10, activation='softmax'))
```

5. Compile the model:
```python
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
```

6. Fit the model:
```python
model.fit(x_train, y_train, batch_size=128, epochs=10, verbose=1)
```

7. Evaluate the model:
```python
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])
```

## Output example

```
Test loss: 0.07912476190745235
Test accuracy: 0.9776
```

## Helpful links
- [Keras Documentation](https://keras.io/)
- [MNIST Dataset](http://yann.lecun.com/exdb/mnist/)

onelinerhub: [How can I use Python Keras to create a machine learning model for the MNIST dataset?](https://onelinerhub.com/python-keras/how-can-i-use-python-keras-to-create-a-machine-learning-model-for-the-mnist-dataset)
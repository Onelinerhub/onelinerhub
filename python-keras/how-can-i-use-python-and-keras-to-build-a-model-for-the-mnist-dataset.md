# How can I use Python and Keras to build a model for the MNIST dataset?
// plain

1. First, import the necessary libraries for the task:
```
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
```

2. Then, load the MNIST dataset from Keras:
```
(x_train, y_train), (x_test, y_test) = mnist.load_data()
```

3. Next, reshape the data to fit the model:
```
x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
input_shape = (28, 28, 1)
```

4. Then, normalize the data:
```
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255
```

5. After that, one-hot encode the labels:
```
y_train = keras.utils.to_categorical(y_train, 10)
y_test = keras.utils.to_categorical(y_test, 10)
```

6. Finally, build and compile the model:
```
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=input_shape))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(10, activation='softmax'))
model.compile(loss=keras.losses.categorical_crossentropy, optimizer=keras.optimizers.Adadelta(), metrics=['accuracy'])
```

7. Finally, fit the model:
```
model.fit(x_train, y_train, batch_size=128, epochs=10, verbose=1, validation_data=(x_test, y_test))
```

## Output example

```
Train on 60000 samples, validate on 10000 samples
Epoch 1/10
60000/60000 [==============================] - 15s 252us/step - loss: 0.2796 - accuracy: 0.9187 - val_loss: 0.1162 - val_accuracy: 0.9648
Epoch 2/10
60000/60000 [==============================] - 5s 81us/step - loss: 0.0911 - accuracy: 0.9737 - val_loss: 0.0791 - val_accuracy: 0.9761
...
```

This is an example of how to use Python and Keras to build a model for the MNIST dataset. The code is composed of the following parts:

1. Import the necessary libraries for the task: `keras`, `mnist`, `Sequential`, `Dense`, `Dropout`, `Flatten`, `Conv2D`, `MaxPooling2D` and `K`.
2. Load the MNIST dataset from Keras.
3. Reshape the data to fit the model.
4. Normalize the data.
5. One-hot encode the labels.
6. Build and compile the model.
7. Fit the model.

## Helpful links
- [Keras Documentation](https://keras.io/)
- [MNIST Dataset](http://yann.lecun.com/exdb/mnist/)

onelinerhub: [How can I use Python and Keras to build a model for the MNIST dataset?](https://onelinerhub.com/python-keras/how-can-i-use-python-and-keras-to-build-a-model-for-the-mnist-dataset)
# How can I use Python and Keras to create a Convolutional Neural Network?
// plain

To create a Convolutional Neural Network (CNN) using Python and Keras, you need to follow these steps:

1. Import the necessary libraries:
```
import numpy as np
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten
```

2. Create a model and add layers:
```
model = Sequential()
model.add(Conv2D(filters=32, kernel_size=(3,3), activation='relu', input_shape=(28, 28, 1)))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(10, activation='softmax'))
```

3. Compile the model:
```
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
```

4. Fit the model:
```
model.fit(x_train, y_train, batch_size=128, epochs=10, verbose=1, validation_data=(x_test, y_test))
```

5. Evaluate the model:
```
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])
```

6. Make predictions:
```
predictions = model.predict(x_test)
```

7. Save the model:
```
model.save('my_model.h5')
```

## Helpful links
- [Keras Documentation](https://keras.io/)
- [TensorFlow Keras Guide](https://www.tensorflow.org/guide/keras)
- [Keras Convolutional Layers](https://keras.io/layers/convolutional/)

onelinerhub: [How can I use Python and Keras to create a Convolutional Neural Network?](https://onelinerhub.com/python-keras/how-can-i-use-python-and-keras-to-create-a-convolutional-neural-network)
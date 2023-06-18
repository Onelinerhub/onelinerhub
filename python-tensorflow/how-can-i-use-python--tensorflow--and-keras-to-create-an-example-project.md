# How can I use Python, TensorFlow, and Keras to create an example project?
// plain

To create an example project using Python, TensorFlow, and Keras, the following steps can be followed:

1. Install Python, TensorFlow, and Keras.
2. Import the necessary libraries, such as NumPy, Matplotlib, and TensorFlow.
```
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
```
3. Build the model using the Keras API.
```
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])
```
4. Compile the model.
```
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
```
5. Train the model.
```
model.fit(x_train, y_train, epochs=5)
```
6. Evaluate the model.
```
test_loss, test_acc = model.evaluate(x_test,  y_test, verbose=2)
print('\nTest accuracy:', test_acc)
```
7. Make predictions using the model.
```
predictions = model.predict(x_test)
```

## Helpful links
- [Python](https://www.python.org/)
- [TensorFlow](https://www.tensorflow.org/)
- [Keras](https://keras.io/)
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)

onelinerhub: [How can I use Python, TensorFlow, and Keras to create an example project?](https://onelinerhub.com/python-tensorflow/how-can-i-use-python--tensorflow--and-keras-to-create-an-example-project)
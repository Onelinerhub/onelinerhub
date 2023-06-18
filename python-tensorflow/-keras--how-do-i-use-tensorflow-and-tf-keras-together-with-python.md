# .keras

How do I use TensorFlow and tf.keras together with Python?
// plain

TensorFlow and tf.keras can be used together to create powerful machine learning models with Python. To do this, you will need to import both TensorFlow and tf.keras into your Python code. The example code below shows how to do this:

```
import tensorflow as tf
import tensorflow.keras as keras
```

Once imported, you can create models using the Keras API, which is part of the TensorFlow library. The example code below shows how to create a simple model using the Sequential API:

```
model = keras.Sequential([
    keras.layers.Dense(64, activation='relu', input_shape=(784,)),
    keras.layers.Dense(10, activation='softmax')
])
```

You can then compile and train the model using the model.compile() and model.fit() methods respectively. The example code below shows how to compile and train the model using the Adam optimizer and the categorical cross-entropy loss function:

```
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)
```

Once the model is trained, you can evaluate it using the model.evaluate() method. The example code below shows how to evaluate the model on the test set:

```
test_loss, test_acc = model.evaluate(x_test, y_test)

print('Test accuracy:', test_acc)
```

This is just a basic example of how to use TensorFlow and tf.keras together with Python. For more information, please refer to the following links:

* [TensorFlow Documentation](https://www.tensorflow.org/guide)
* [Keras Documentation](https://keras.io/getting-started/sequential-model-guide/)
* [Tutorial: Deep Learning in Python with TensorFlow and Keras](https://www.datacamp.com/community/tutorials/deep-learning-python)

onelinerhub: [.keras

How do I use TensorFlow and tf.keras together with Python?](https://onelinerhub.com/python-tensorflow/-keras--how-do-i-use-tensorflow-and-tf-keras-together-with-python)
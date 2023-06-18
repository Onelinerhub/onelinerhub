# How do I use Python TensorFlow.Keras.Models to create a machine learning model?
// plain

Python TensorFlow.Keras.Models can be used to create a machine learning model. To do this, the following steps can be taken:

1. First, import the relevant libraries:
```
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
```

2. Then, create the model structure by defining the layers:
```
model = Sequential()
model.add(Dense(units=64, activation='relu', input_dim=100))
model.add(Dense(units=10, activation='softmax'))
```

3. Compile the model, specifying the optimizer, loss function and metrics:
```
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
```

4. Fit the model to the training data for a specified number of epochs:
```
model.fit(train_data, train_targets, epochs=5)
```

5. Evaluate the model on the test data:
```
test_loss, test_acc = model.evaluate(test_data, test_targets)
```

6. Make predictions using the model:
```
predictions = model.predict(test_data)
```

7. Finally, save the model for future use:
```
model.save('my_model.h5')
```

## Helpful links
- [TensorFlow - Get Started](https://www.tensorflow.org/tutorials/quickstart/beginner)
- [Keras - Getting Started](https://keras.io/#getting-started-30-seconds-to-keras)
- [Keras - Model](https://keras.io/models/model/)

onelinerhub: [How do I use Python TensorFlow.Keras.Models to create a machine learning model?](https://onelinerhub.com/python-tensorflow/how-do-i-use-python-tensorflow-keras-models-to-create-a-machine-learning-model)
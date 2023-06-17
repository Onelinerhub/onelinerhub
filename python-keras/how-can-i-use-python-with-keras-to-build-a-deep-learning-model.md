# How can I use Python with Keras to build a deep learning model?
// plain

Python with Keras can be used to build a deep learning model by following these steps:

1. Import the required libraries:
```
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
```

2. Create the model:
```
model = Sequential()
model.add(Dense(units=64, activation='relu', input_dim=100))
model.add(Dense(units=10, activation='softmax'))
```

3. Compile the model:
```
model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])
```

4. Train the model:
```
model.fit(x_train, y_train, epochs=5, batch_size=32)
```

5. Evaluate the model:
```
loss_and_metrics = model.evaluate(x_test, y_test, batch_size=128)
```

6. Make predictions with the model:
```
classes = model.predict(x_test, batch_size=128)
```

7. Save the model:
```
model.save('my_model.h5')
```

## Helpful links
- [Keras Documentation](https://keras.io/)
- [Getting Started with Deep Learning using Keras](https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/)

onelinerhub: [How can I use Python with Keras to build a deep learning model?](https://onelinerhub.com/python-keras/how-can-i-use-python-with-keras-to-build-a-deep-learning-model)
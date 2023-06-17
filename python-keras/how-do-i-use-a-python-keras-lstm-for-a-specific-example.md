# How do I use a Python Keras LSTM for a specific example?
// plain

The following example code shows how to use a Python Keras LSTM for a specific example. This example uses a simple dataset of 1000 samples consisting of two features and a label. The label is binary, and the features are randomly generated.

```
# import libraries
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, LSTM

# generate dataset
data_dim = 2
timesteps = 8
num_classes = 2

# expected input data shape: (batch_size, timesteps, data_dim)
x_train = np.random.random((1000, timesteps, data_dim))
y_train = np.random.randint(2, size=(1000, 1))

# build model
model = Sequential()
model.add(LSTM(32, return_sequences=True,
               input_shape=(timesteps, data_dim)))
model.add(LSTM(32, return_sequences=True))
model.add(LSTM(32))
model.add(Dense(2, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

# train model
model.fit(x_train, y_train,
          batch_size=64, epochs=5)
```

The code above builds a LSTM model with three LSTM layers and a Dense layer. The input shape is set to (batch_size, timesteps, data_dim). The model is then compiled with the `categorical_crossentropy` loss function and the `rmsprop` optimizer. Finally, the model is trained on the generated dataset.

## Code explanation


1. `import numpy as np`: imports the NumPy library as `np`
2. `from keras.models import Sequential`: imports the `Sequential` model from Keras
3. `from keras.layers import Dense, LSTM`: imports the `Dense` and `LSTM` layers from Keras
4. `data_dim = 2`: sets the dimension of the data to 2
5. `timesteps = 8`: sets the number of timesteps to 8
6. `num_classes = 2`: sets the number of classes to 2
7. `x_train = np.random.random((1000, timesteps, data_dim))`: generates a dataset of 1000 samples with two features and a label
8. `y_train = np.random.randint(2, size=(1000, 1))`: generates a binary label for the dataset
9. `model = Sequential()`: creates a sequential model
10. `model.add(LSTM(32, return_sequences=True, input_shape=(timesteps, data_dim)))`: adds a LSTM layer to the model with 32 units, `return_sequences=True` to return the output of each timestep, and `input_shape` set to the data shape
11. `model.add(LSTM(32, return_sequences=True))`: adds another LSTM layer to the model with 32 units and `return_sequences=True`
12. `model.add(LSTM(32))`: adds another LSTM layer to the model with 32 units
13. `model.add(Dense(2, activation='softmax'))`: adds a Dense layer with 2 units and the `softmax` activation function
14. `model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])`: compiles the model with the `categorical_crossentropy` loss function, the `rmsprop` optimizer, and accuracy as the metric
15. `model.fit(x_train, y_train, batch_size=64, epochs=5)`: trains the model on the dataset with a batch size of 64 and 5 epochs

## Helpful links

- [Keras Documentation - LSTM](https://keras.io/layers/recurrent/#lstm)
- [Keras Documentation - Sequential Model](https://keras.io/models/sequential/)

onelinerhub: [How do I use a Python Keras LSTM for a specific example?](https://onelinerhub.com/python-keras/how-do-i-use-a-python-keras-lstm-for-a-specific-example)
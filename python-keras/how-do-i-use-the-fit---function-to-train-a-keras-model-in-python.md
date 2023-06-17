# How do I use the fit() function to train a Keras model in Python?
// plain

The `fit()` function is used to train a Keras model in Python. It takes the model, the training data, and the number of epochs as arguments and returns a history object.

## Example code

```
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Create a model
model = Sequential()
model.add(Dense(2, activation='relu', input_dim=3))
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
training_data = [[1,2,3],[4,5,6]]
target_data = [[0],[1]]
history = model.fit(training_data, target_data, epochs=10)
```

Output (if any):

`Epoch 1/10
1/1 [==============================] - 0s 2ms/step - loss: 0.6931 - accuracy: 0.5000
Epoch 2/10
1/1 [==============================] - 0s 2ms/step - loss: 0.6931 - accuracy: 0.5000
Epoch 3/10
1/1 [==============================] - 0s 2ms/step - loss: 0.6931 - accuracy: 0.5000
...
Epoch 10/10
1/1 [==============================] - 0s 2ms/step - loss: 0.6931 - accuracy: 0.5000`

## Code explanation


1. `from tensorflow.keras.models import Sequential`: This imports the Sequential model from the Keras library.
2. `from tensorflow.keras.layers import Dense`: This imports the Dense layer from the Keras library.
3. `model = Sequential()`: This creates an empty sequential model.
4. `model.add(Dense(2, activation='relu', input_dim=3))`: This adds a dense layer with two neurons and a ReLU activation function to the model. The input dimension is set to 3.
5. `model.add(Dense(1, activation='sigmoid'))`: This adds a dense layer with one neuron and a sigmoid activation function to the model.
6. `model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])`: This compiles the model, using the Adam optimizer, the binary cross entropy loss function, and accuracy as the metric.
7. `history = model.fit(training_data, target_data, epochs=10)`: This trains the model using the training data and target data, for 10 epochs. The history object is returned.

## Helpful links

- [Keras Documentation - fit()](https://keras.io/api/models/model_training_apis/#fit-method)
- [TensorFlow Documentation - Compile a model](https://www.tensorflow.org/guide/keras/r1/training_and_evaluation#compile_a_model)

onelinerhub: [How do I use the fit() function to train a Keras model in Python?](https://onelinerhub.com/python-keras/how-do-i-use-the-fit---function-to-train-a-keras-model-in-python)
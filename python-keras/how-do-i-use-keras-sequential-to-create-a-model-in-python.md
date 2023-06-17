# How do I use Keras Sequential to create a model in Python?
// plain

Keras Sequential is a way of creating a linear stack of layers in a deep learning model. To use Keras Sequential, you must first create a Sequential object and then add layers to it. The layers can be added one by one or all at once.

## Example code


```
from keras.models import Sequential
from keras.layers import Dense

# Create the Sequential model
model = Sequential()

# 1st Layer - Add a flatten layer
model.add(Flatten(input_shape=(32, 32, 3)))

# 2nd Layer - Add a fully connected layer
model.add(Dense(100, activation='relu'))

# 3rd Layer - Add a fully connected layer
model.add(Dense(60, activation='relu'))

# Output Layer - Add a fully connected layer
model.add(Dense(10, activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
```

## Code explanation


1. `from keras.models import Sequential` - imports the Sequential model from the Keras library.
2. `model = Sequential()` - creates the Sequential model object.
3. `model.add(Flatten(input_shape=(32, 32, 3)))` - adds a flatten layer to the model. The input shape is the size of the image (32x32 pixels with 3 color channels).
4. `model.add(Dense(100, activation='relu'))` - adds a fully connected layer with 100 nodes and ReLU activation.
5. `model.add(Dense(60, activation='relu'))` - adds another fully connected layer with 60 nodes and ReLU activation.
6. `model.add(Dense(10, activation='softmax'))` - adds the output layer with 10 nodes and Softmax activation.
7. `model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])` - compiles the model with the Adam optimizer, categorical cross-entropy loss function, and accuracy metrics.

## Helpful links

- [Keras Documentation - Sequential Model](https://keras.io/getting-started/sequential-model-guide/)
- [Keras Documentation - Layers](https://keras.io/layers/core/)
- [Keras Documentation - Compilation](https://keras.io/getting-started/sequential-model-guide/#compilation)

onelinerhub: [How do I use Keras Sequential to create a model in Python?](https://onelinerhub.com/python-keras/how-do-i-use-keras-sequential-to-create-a-model-in-python)
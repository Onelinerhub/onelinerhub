# How do I create a simple example using Python and Keras?
// plain

Creating a simple example using Python and Keras is relatively straightforward. Below is an example of a basic neural network with one input and one output layer.

```python
import numpy as np
from keras.models import Sequential
from keras.layers import Dense

# Create a model
model = Sequential()
model.add(Dense(1, input_dim=1, activation='sigmoid'))

# Compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
x = np.array([[0],[1]])
y = np.array([0,1])
model.fit(x, y, epochs=200, batch_size=2, verbose=1)

# Evaluate the model
scores = model.evaluate(x, y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
```

## Output example

```
200/200 [==============================] - 0s 4ms/step

accuracy: 100.00%
```

The code consists of the following parts:
1. Importing necessary libraries such as numpy and keras
2. Creating a model object with the Sequential() method
3. Adding a layer to the model with the add() method
4. Compiling the model with the compile() method
5. Training the model with the fit() method
6. Evaluating the model with the evaluate() method
7. Printing the accuracy of the model

For further information on using Python and Keras, please refer to the following links:

- [Keras Documentation](https://keras.io/)
- [Getting Started with Keras](https://keras.io/#getting-started-30-seconds-to-keras)
- [Keras Tutorials](https://keras.io/examples/)

onelinerhub: [How do I create a simple example using Python and Keras?](https://onelinerhub.com/python-keras/how-do-i-create-a-simple-example-using-python-and-keras)
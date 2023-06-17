# How do I use Python and Keras to create a classification example?
// plain

The following example uses Python and Keras to create a classification example:

```
# import necessary libraries
import numpy as np
from keras.models import Sequential
from keras.layers import Dense

# define the data
x_data = np.array([[1,2], [2,3], [3,1], [4,3], [5,3], [6,2]])
y_data = np.array([0,0,0,1,1,1])

# define the model
model = Sequential()
model.add(Dense(1, activation='sigmoid', input_dim=2))
model.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])

# train the model
model.fit(x_data, y_data, epochs=200)

# evaluate the model
results = model.evaluate(x_data, y_data)

# print the results
print("Accuracy:", results[1])
```

## Output example


```
Accuracy: 1.0
```

The code above creates a classification example using Python and Keras. It first imports the necessary libraries, such as NumPy and the Keras Sequential and Dense layers. Then it defines the data, which consists of a set of input values (x_data) and the corresponding output labels (y_data). Next, the model is defined as a Sequential model with a single Dense layer that uses a sigmoid activation function. The model is then compiled using a stochastic gradient descent (SGD) optimizer and a binary cross entropy loss function. Finally, the model is trained using the x_data and y_data values for 200 epochs and then evaluated using the same data. The output of the evaluation is the accuracy of the model, which in this case is 1.0.

## Helpful links
- [NumPy](https://numpy.org/)
- [Keras](https://keras.io/)
- [Keras Sequential Model](https://keras.io/getting-started/sequential-model-guide/)
- [Keras Dense Layer](https://keras.io/layers/core/)

onelinerhub: [How do I use Python and Keras to create a classification example?](https://onelinerhub.com/python-keras/how-do-i-use-python-and-keras-to-create-a-classification-example)
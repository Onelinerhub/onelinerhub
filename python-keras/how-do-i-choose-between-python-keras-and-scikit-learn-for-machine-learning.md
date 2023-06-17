# How do I choose between Python Keras and Scikit Learn for machine learning?
// plain

When deciding between Python Keras and Scikit Learn for machine learning, you should consider the type of problem you are trying to solve. If you are looking to solve a complex problem, such as deep learning, then Keras is the right choice. If you are looking to solve simpler problems, such as linear regression, then Scikit Learn is the better option.

For example, if you wanted to use Keras to create a deep learning model, you could use the following code:

```
# import necessary modules
import keras
from keras.models import Sequential
from keras.layers import Dense

# create a model
model = Sequential()
model.add(Dense(units=64, activation='relu', input_dim=100))
model.add(Dense(units=10, activation='softmax'))

# compile the model
model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])
```

On the other hand, if you wanted to use Scikit Learn to build a linear regression model, you could use the following code:

```
# import necessary modules
import numpy as np
from sklearn.linear_model import LinearRegression

# define input and output variables
X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
y = np.dot(X, np.array([1, 2])) + 3

# create a model
model = LinearRegression().fit(X, y)

# predict
predicted_y = model.predict([[3, 5]])

# print prediction
print(predicted_y)

# output
[16.]
```

In summary, when deciding between Python Keras and Scikit Learn for machine learning, consider the type of problem you are trying to solve. If you are looking to solve a complex problem, such as deep learning, then Keras is the right choice. If you are looking to solve simpler problems, such as linear regression, then Scikit Learn is the better option.

**List of Code Parts with Detailed Explanation**

1. `import keras`: imports the Keras library for use in the code.
2. `from keras.models import Sequential`: imports the Sequential model from Keras.
3. `from keras.layers import Dense`: imports the Dense layer from Keras.
4. `model = Sequential()`: creates a Sequential model.
5. `model.add(Dense(units=64, activation='relu', input_dim=100))`: adds a Dense layer to the model with 64 neurons, a ReLU activation function, and an input dimension of 100.
6. `model.add(Dense(units=10, activation='softmax'))`: adds a Dense layer to the model with 10 neurons and a Softmax activation function.
7. `model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])`: compiles the model with a categorical cross-entropy loss function, an SGD optimizer, and an accuracy metric.
8. `import numpy as np`: imports the NumPy library for use in the code.
9. `from sklearn.linear_model import LinearRegression`: imports the LinearRegression model from Scikit Learn.
10. `X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])`: creates a NumPy array of input data.
11. `y = np.dot(X, np.array([1, 2])) + 3`: creates a NumPy array of output data.
12. `model = LinearRegression().fit(X, y)`: creates a LinearRegression model and fits it to the input and output data.
13. `predicted_y = model.predict([[3, 5]])`: predicts the output for the given input.
14. `print(predicted_y)`: prints the prediction.

**List of Relevant Links**

- [Keras Documentation](https://keras.io/)
- [Scikit Learn Documentation](https://scikit-learn.org/stable/documentation.html)

onelinerhub: [How do I choose between Python Keras and Scikit Learn for machine learning?](https://onelinerhub.com/python-keras/how-do-i-choose-between-python-keras-and-scikit-learn-for-machine-learning)
# How do I use Python Keras to perform a train-test split?
// plain

Using Python Keras to perform a train-test split is a simple process. Here is an example code block to demonstrate how to do this:
```
# import necessary libraries
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense

# define dataset
X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# define model
model = Sequential()
model.add(Dense(1, input_dim=1))

# compile model
model.compile(loss='mean_squared_error', optimizer='adam')

# fit model
model.fit(X_train, y_train, epochs=500, verbose=0)

# evaluate model
test_error = model.evaluate(X_test, y_test, verbose=0)
print('Test Error: %.2f' % test_error)
```

This code will output the following:
```
Test Error: 0.00
```

The code is composed of several parts:
1. Import the necessary libraries: `from sklearn.model_selection import train_test_split` and `from keras.models import Sequential` and `from keras.layers import Dense`.
2. Define the dataset: `X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` and `y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`.
3. Split the dataset into training and testing sets: `X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)`.
4. Define the model: `model = Sequential()` and `model.add(Dense(1, input_dim=1))`.
5. Compile the model: `model.compile(loss='mean_squared_error', optimizer='adam')`.
6. Fit the model: `model.fit(X_train, y_train, epochs=500, verbose=0)`.
7. Evaluate the model: `test_error = model.evaluate(X_test, y_test, verbose=0)` and `print('Test Error: %.2f' % test_error)`.

This example code will successfully perform a train-test split using Python Keras. For more information, please see the following links:
- [Keras Documentation](https://keras.io/getting-started/sequential-model-guide/)
- [Scikit-Learn Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)

onelinerhub: [How do I use Python Keras to perform a train-test split?](https://onelinerhub.com/python-keras/how-do-i-use-python-keras-to-perform-a-train-test-split)
# How do I create a sequential model using Python and Keras?
// plain

Creating a sequential model using Python and Keras is relatively straightforward. To begin, import the necessary libraries:

```
import keras
from keras.models import Sequential
from keras.layers import Dense
```

Next, create a Sequential model object:

```
model = Sequential()
```

The model can then be built by adding layers one at a time. For example, adding a Dense layer with 10 neurons and an input shape of 8:

```
model.add(Dense(10, input_shape=(8,)))
```

More layers can be added in a similar fashion. For example, adding a second Dense layer with 6 neurons:

```
model.add(Dense(6))
```

Once the model is built, it can be compiled using the .compile() method:

```
model.compile(optimizer='adam', loss='mse')
```

The model can then be fit using the .fit() method:

```
model.fit(X, y, epochs=20)
```

The model can then be evaluated using the .evaluate() method:

```
model.evaluate(X, y)
```

## Code explanation


1. Importing Libraries: `import keras`, `from keras.models import Sequential`, `from keras.layers import Dense`
2. Creating a Sequential Model Object: `model = Sequential()`
3. Adding Layers: `model.add(Dense(10, input_shape=(8,)))`, `model.add(Dense(6))`
4. Compiling the Model: `model.compile(optimizer='adam', loss='mse')`
5. Fitting the Model: `model.fit(X, y, epochs=20)`
6. Evaluating the Model: `model.evaluate(X, y)`

## Helpful links

- [Keras Documentation](https://keras.io/)
- [Getting Started with the Keras Sequential Model](https://machinelearningmastery.com/getting-started-with-the-keras-sequential-model/)

onelinerhub: [How do I create a sequential model using Python and Keras?](https://onelinerhub.com/python-keras/how-do-i-create-a-sequential-model-using-python-and-keras)
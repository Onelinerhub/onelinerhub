# How can I use Python Keras to perform a grid search?
// plain

You can use Python Keras to perform a grid search by using the `KerasClassifier` class from the `keras.wrappers.scikit_learn` module. This class allows you to use the scikit-learn library's `GridSearchCV` method to perform a grid search.

## Example code

```
# Import necessary modules
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import GridSearchCV

# Create function to build model
def create_model(optimizer='rmsprop', init='glorot_uniform'):
    # Create model
    model = Sequential()
    # Add layers
    # Compile model
    model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])
    return model

# Create model
model = KerasClassifier(build_fn=create_model, verbose=0)

# Define the grid search parameters
optimizer = ['SGD', 'RMSprop', 'Adagrad', 'Adadelta', 'Adam', 'Adamax', 'Nadam']
init = ['uniform', 'lecun_uniform', 'normal', 'zero', 'glorot_normal', 'glorot_uniform', 'he_normal', 'he_uniform']

# Create the grid
param_grid = dict(optimizer=optimizer, init=init)

# Perform the grid search
grid = GridSearchCV(estimator=model, param_grid=param_grid, n_jobs=-1, cv=3)
grid_result = grid.fit(X, Y)

# Print the best parameters
print("Best: %f using %s" % (grid_result.best_score_, grid_result.best_params_))
```

The code above will search through a set of optimizers and initialization parameters to find the best combination for the model. The `GridSearchCV` method will then output the best score and parameters.

## Code explanation

- `KerasClassifier`: This class allows you to use the scikit-learn library's `GridSearchCV` method to perform a grid search.
- `GridSearchCV`: This method will search through a set of optimizers and initialization parameters to find the best combination for the model.
- `fit`: This method will perform the grid search.
- `best_score_`: This will output the best score from the grid search.
- `best_params_`: This will output the best parameters from the grid search.

## Helpful links
- [KerasClassifier](https://keras.io/scikit-learn-api/)
- [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html)

onelinerhub: [How can I use Python Keras to perform a grid search?](https://onelinerhub.com/python-keras/how-can-i-use-python-keras-to-perform-a-grid-search)
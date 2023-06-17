# How can I get the weights of my Python Keras model?
// plain

To get the weights of a Python Keras model, you can use the `get_weights()` method. This method returns a list of numpy arrays, each containing the weights of the model for a single layer.

## Example code

```
model = Sequential()
model.add(Dense(64, input_dim=64, kernel_initializer='uniform', activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
weights = model.get_weights()
```

## Output example

```
[array([[ 0.03738443, -0.00438571, -0.03912098, ...,  0.05268976,
          0.06986515, -0.05466834],
       [ 0.04930462,  0.06912202, -0.01011086, ...,  0.06700403,
         -0.05242571, -0.06801051],
       [ 0.05172399, -0.01971836,  0.03024069, ...,  0.06730981,
         -0.00643077,  0.0496422 ],
       ...,
       [-0.05837193,  0.00091718,  0.07959776, ...,  0.06146731,
         -0.07918619, -0.07769193],
       [-0.06421017,  0.0687856 ,  0.05856385, ...,  0.07944132,
         -0.06224829, -0.04787586],
       [ 0.04507772,  0.05773481, -0.05817863, ...,  0.07451814,
          0.06830471,  0.05868983]], dtype=float32),
 array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
         0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
         0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
         0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
         0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
         0.,  0.,  0.,  0.,  0.], dtype=float32)]
```

## Code explanation


- `model = Sequential()`: This creates a Sequential model object, which is a linear stack of layers.
- `model.add(Dense(64, input_dim=64, kernel_initializer='uniform', activation='relu'))`: This adds a dense layer with 64 neurons and a ReLU activation function. The input dimension is set to 64.
- `model.add(Dense(32, activation='relu'))`: This adds a second dense layer with 32 neurons and a ReLU activation function.
- `model.add(Dense(1, activation='sigmoid'))`: This adds a third dense layer with 1 neuron and a sigmoid activation function.
- `weights = model.get_weights()`: This retrieves the weights of the model and stores them in a list of numpy arrays.

## Helpful links

- [Keras Documentation: get_weights](https://keras.io/api/layers/base_layer/#get_weights-method)

onelinerhub: [How can I get the weights of my Python Keras model?](https://onelinerhub.com/python-keras/how-can-i-get-the-weights-of-my-python-keras-model)
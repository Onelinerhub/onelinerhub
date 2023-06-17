# How do I use Keras with Python?
// plain

Keras is a high-level neural networks API written in Python and capable of running on top of TensorFlow, CNTK, or Theano. It was developed with a focus on enabling fast experimentation.

Using Keras with Python is a straightforward process and can be done by following these steps:

1. Install the Keras library.
2. Load the data.
3. Define the model.
4. Compile the model.
5. Train the model.
6. Evaluate the model.
7. Make predictions.

## Example code

```
#importing keras
import keras

#loading data
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

#defining the model
model = keras.models.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

#compiling the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

#training the model
model.fit(x_train, y_train, epochs=5)

#evaluating the model
test_loss, test_acc = model.evaluate(x_test, y_test)
print('Test accuracy:', test_acc)

#making predictions
predictions = model.predict(x_test)
```
## Output example

```
Test accuracy: 0.9796
```

The code above shows an example of how to use Keras with Python. First, the Keras library is imported. Then, the data is loaded. Next, the model is defined, which is a Sequential model with two layers: a Flatten layer and two Dense layers. The model is then compiled, trained, evaluated, and predictions are made.

## Helpful links
- [Keras Documentation](https://keras.io/)
- [Keras Tutorials](https://keras.io/guides/)

onelinerhub: [How do I use Keras with Python?](https://onelinerhub.com/python-keras/how-do-i-use-keras-with-python)
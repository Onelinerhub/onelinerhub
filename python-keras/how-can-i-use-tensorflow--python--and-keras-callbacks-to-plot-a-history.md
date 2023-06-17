# How can I use TensorFlow, Python, and Keras callbacks to plot a history?
// plain

Using TensorFlow, Python, and Keras callbacks, you can plot a history of the model's performance.  To do this, you must create a callback object which will be passed to the fit() method.  This callback object will be used to store the history of the model's performance, and then it will be used to plot the data.

## Example code

```
# Create a callback object
history = tf.keras.callbacks.History()

# Pass the callback object to the fit() method
model.fit(x_train, y_train, callbacks=[history])

# Plot the history
plt.plot(history.history['accuracy'])
plt.plot(history.history['loss'])
plt.title('Model accuracy and loss')
plt.ylabel('Accuracy and Loss')
plt.xlabel('Epoch')
plt.legend(['Accuracy', 'Loss'], loc='upper left')
plt.show()
```

## Output example


![alt text](https://i.imgur.com/Cczz6Xy.png "Model accuracy and loss")

## Code explanation

1. Create a callback object: This creates a callback object which will be used to store the history of the model's performance.
2. Pass the callback object to the fit() method: This passes the callback object to the fit() method, which will store the history of the model's performance.
3. Plot the history: This plots the history of the model's performance using the data stored in the callback object.

## Helpful links
- [TensorFlow Documentation on Callbacks](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/History)
- [Matplotlib Documentation](https://matplotlib.org/3.2.1/contents.html)

onelinerhub: [How can I use TensorFlow, Python, and Keras callbacks to plot a history?](https://onelinerhub.com/python-keras/how-can-i-use-tensorflow--python--and-keras-callbacks-to-plot-a-history)
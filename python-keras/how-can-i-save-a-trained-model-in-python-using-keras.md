# How can I save a trained model in Python using Keras?
// plain

Saving a trained model in Python using Keras is relatively straightforward. Here is an example code block to illustrate the process:

```
# Save the weights
model.save_weights('model_weights.h5')

# Save the model architecture
with open('model_architecture.json', 'w') as f:
    f.write(model.to_json())
```

The first line saves the weights of the model in an .h5 file, which can be loaded back in later. The second line saves the model architecture as a JSON file, which can also be loaded back in later.

## Code explanation

- `model.save_weights('model_weights.h5')`: This line saves the weights of the model in an .h5 file.
- `with open('model_architecture.json', 'w') as f`: This line opens a file for writing.
- `f.write(model.to_json())`: This line writes the model architecture as a JSON file.

## Helpful links
- [Keras Documentation - Saving and serializing models](https://keras.io/getting-started/faq/#how-can-i-save-a-keras-model)

onelinerhub: [How can I save a trained model in Python using Keras?](https://onelinerhub.com/python-keras/how-can-i-save-a-trained-model-in-python-using-keras)
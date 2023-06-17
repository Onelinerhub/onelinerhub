# How to load a model in Python Keras?
// plain

Loading a model in Python Keras is a simple process. The following example code block loads a model from a JSON file:

```
from keras.models import model_from_json

# load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)

# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")
```

The output of this code block will be: `Loaded model from disk`

## Code explanation


1. `from keras.models import model_from_json`: This imports the `model_from_json` function from the Keras library.

2. `json_file = open('model.json', 'r')`: This opens the `model.json` file in read mode.

3. `loaded_model_json = json_file.read()`: This reads the contents of the `model.json` file.

4. `json_file.close()`: This closes the `model.json` file.

5. `loaded_model = model_from_json(loaded_model_json)`: This creates a model from the `model.json` file.

6. `loaded_model.load_weights("model.h5")`: This loads the weights from the `model.h5` file into the model.

7. `print("Loaded model from disk")`: This prints the message `Loaded model from disk` when the model is successfully loaded.

## Helpful links

- [Keras Documentation - Model Saving & Loading](https://keras.io/getting-started/faq/#how-can-i-save-a-keras-model)
- [TensorFlow Documentation - Save and Restore Models](https://www.tensorflow.org/guide/saved_model#saving_whole_models)

onelinerhub: [How to load a model in Python Keras?](https://onelinerhub.com/python-keras/how-to-load-a-model-in-python-keras)
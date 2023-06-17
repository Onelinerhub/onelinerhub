# How can I convert a TensorFlow Keras model to ONNX using keras2onnx?
// plain

To convert a TensorFlow Keras model to ONNX using keras2onnx, you need to install the keras2onnx package and import the necessary modules.

```python
pip install keras2onnx

from keras.models import load_model
import keras2onnx
import onnx
```

Then, you can load the Keras model and convert it to ONNX.

```python
model = load_model('model.h5')
onnx_model = keras2onnx.convert_keras(model, model.name)
onnx.save_model(onnx_model, 'model.onnx')
```

The above example code will save the converted model as `model.onnx`.

You can also specify the target ONNX opset version, input and output names, and the input shape.

```python
onnx_model = keras2onnx.convert_keras(model, model.name, target_opset=7,
	input_names=['input_1'], output_names=['output_1'],
	custom_conversion_functions={'MyLayer': my_conversion_function},
	inputs=[(input_shape, 'input_1')])
```

- `target_opset`: ONNX opset version (defaults to 9)
- `input_names`: list of input names (defaults to ['input_1'])
- `output_names`: list of output names (defaults to ['output_1'])
- `custom_conversion_functions`: dictionary of custom conversion functions for layers not supported by keras2onnx
- `inputs`: list of tuples containing input shape and name

For more information, see the [keras2onnx documentation](https://github.com/onnx/keras-onnx/blob/master/README.md).

onelinerhub: [How can I convert a TensorFlow Keras model to ONNX using keras2onnx?](https://onelinerhub.com/python-keras/how-can-i-convert-a-tensorflow-keras-model-to-onnx-using-keras-onnx)
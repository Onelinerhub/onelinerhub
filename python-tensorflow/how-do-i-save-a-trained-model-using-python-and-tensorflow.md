# How do I save a trained model using Python and TensorFlow?
// plain

Saving a trained model using Python and TensorFlow is a simple process. The following steps outline the process:

1. Create a Saver object, specifying the variables you want to save:
```
saver = tf.compat.v1.train.Saver(var_list=tf.global_variables())
```

2. Call the `save()` method of the Saver object, specifying the path where you want to save the model:
```
saver.save(sess, './my_model.ckpt')
```

3. To restore the model from a saved checkpoint, use the `restore()` method of the Saver object:
```
saver.restore(sess, './my_model.ckpt')
```

4. To save the model as a SavedModel, use the `tf.saved_model.save()` method:
```
tf.saved_model.save(sess, './my_model')
```

5. To restore the model from a SavedModel, use the `tf.saved_model.load()` method:
```
tf.saved_model.load(sess, './my_model')
```

6. To save the model as a frozen graph, use the `tf.graph_util.convert_variables_to_constants()` method:
```
tf.graph_util.convert_variables_to_constants(
    sess, sess.graph_def, ['output_node_name'])
```

7. To restore the model from a frozen graph, use the `tf.import_graph_def()` method:
```
graph_def = tf.GraphDef()
with tf.gfile.GFile('frozen_model.pb', 'rb') as f:
    graph_def.ParseFromString(f.read())

tf.import_graph_def(graph_def)
```

## Helpful links
- [Saving and Restoring Models](https://www.tensorflow.org/guide/saved_model)
- [Freezing a Model](https://www.tensorflow.org/guide/graph_viz)

onelinerhub: [How do I save a trained model using Python and TensorFlow?](https://onelinerhub.com/python-tensorflow/how-do-i-save-a-trained-model-using-python-and-tensorflow)
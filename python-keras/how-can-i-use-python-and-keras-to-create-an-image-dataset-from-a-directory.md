# How can I use Python and Keras to create an image dataset from a directory?
// plain

Creating an image dataset from a directory with Python and Keras is a relatively straightforward process. The following example code block can be used to achieve this:

```
from keras.preprocessing.image import ImageDataGenerator

# Set the directory where the images are stored
data_dir = 'data/'

# Create the data generator
datagen = ImageDataGenerator(rescale=1./255)

# Load the images from the directory
data_generator = datagen.flow_from_directory(
    data_dir,
    target_size=(150, 150),
    batch_size=32,
    class_mode='categorical')
```

The code above will load the images from the directory specified by `data_dir`. The images will be resized to 150x150 pixels. The images will also be rescaled to a range of 0-1. The `data_generator` variable will contain the dataset.

## Code explanation


* `from keras.preprocessing.image import ImageDataGenerator` - imports the `ImageDataGenerator` class from the `keras.preprocessing.image` module.
* `data_dir = 'data/'` - sets the directory where the images are stored.
* `datagen = ImageDataGenerator(rescale=1./255)` - creates the data generator, with the images rescaled to a range of 0-1.
* `data_generator = datagen.flow_from_directory(data_dir, target_size=(150, 150), batch_size=32, class_mode='categorical')` - loads the images from the directory, resizing them to 150x150 pixels, and returns the dataset in the `data_generator` variable.

## Helpful links

* [Keras Image Preprocessing](https://keras.io/preprocessing/image/)
* [Keras ImageDataGenerator Documentation](https://keras.io/preprocessing/image/#imagedatagenerator-class)

onelinerhub: [How can I use Python and Keras to create an image dataset from a directory?](https://onelinerhub.com/python-keras/how-can-i-use-python-and-keras-to-create-an-image-dataset-from-a-directory)
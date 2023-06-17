# How do I use Python and Keras to resize an image?
// plain

Using Python and Keras, you can resize an image by using the `ImageDataGenerator` class. This class allows you to easily preprocess images, including resizing them.

To use this class, first import the `ImageDataGenerator` class from Keras:
```
from keras.preprocessing.image import ImageDataGenerator
```

Then, create an instance of the `ImageDataGenerator` class, and set the `rescale` parameter to the desired size:
```
datagen = ImageDataGenerator(rescale=1./255)
```

Finally, use the `flow_from_directory` method to generate batches of images, specifying the directory containing the images and the desired target size:
```
generator = datagen.flow_from_directory(
    'data/',
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical')
```

The above code will resize all images in the `data/` directory to a size of (224, 224).

## Code explanation

1. `from keras.preprocessing.image import ImageDataGenerator`: imports the `ImageDataGenerator` class from Keras
2. `datagen = ImageDataGenerator(rescale=1./255)`: creates an instance of the `ImageDataGenerator` class, and sets the `rescale` parameter to the desired size
3. `generator = datagen.flow_from_directory('data/', target_size=(224, 224), batch_size=32, class_mode='categorical')`: uses the `flow_from_directory` method to generate batches of images, specifying the directory containing the images and the desired target size

## Helpful links
- [Keras Image Preprocessing](https://keras.io/preprocessing/image/)

onelinerhub: [How do I use Python and Keras to resize an image?](https://onelinerhub.com/python-keras/how-do-i-use-python-and-keras-to-resize-an-image)
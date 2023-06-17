# How do I use the Python Keras preprocessing image module?
// plain

The Python Keras preprocessing image module is a library for preprocessing images in Keras. It enables you to prepare images for deep learning models.

To use the module, you first need to import it:
```
from keras.preprocessing import image
```

The module can be used to load images from the file system, to convert them to numpy arrays, and to resize them.

For example, to load an image from the file system and convert it to a numpy array, you can use the following code:
```
img = image.load_img('example.jpg', target_size=(224, 224))
x = image.img_to_array(img)
```

The module also provides functions for image augmentation, such as random rotations, shifts, zoom, and flips. For example, to randomly rotate an image by 90 degrees, you can use the following code:

```
from keras.preprocessing.image import ImageDataGenerator

datagen = ImageDataGenerator(rotation_range=90)
datagen.fit(x)
```

The module also provides functions for saving images to the file system. For example, to save an image to the file system, you can use the following code:

```
image.save_img('example_rotated.jpg', x)
```

## Code explanation

1. `from keras.preprocessing import image`: imports the module
2. `img = image.load_img('example.jpg', target_size=(224, 224))`: loads an image from the file system and resizes it
3. `x = image.img_to_array(img)`: converts the image to a numpy array
4. `from keras.preprocessing.image import ImageDataGenerator`: imports the ImageDataGenerator class
5. `datagen = ImageDataGenerator(rotation_range=90)`: creates a new ImageDataGenerator object with a rotation range of 90 degrees
6. `datagen.fit(x)`: fits the ImageDataGenerator object to the image
7. `image.save_img('example_rotated.jpg', x)`: saves the image to the file system

## Helpful links
- [Keras Preprocessing Image Documentation](https://keras.io/preprocessing/image/)
- [Keras ImageDataGenerator Documentation](https://keras.io/preprocessing/image/#imagedatagenerator-class)

onelinerhub: [How do I use the Python Keras preprocessing image module?](https://onelinerhub.com/python-keras/how-do-i-use-the-python-keras-preprocessing-image-module)
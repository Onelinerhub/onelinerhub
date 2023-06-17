# How do I use the Python Keras ImageDataGenerator to create batches of image data?
// plain

The Python Keras ImageDataGenerator is a powerful tool for creating batches of image data. It can be used to read images from a directory and generate batches of augmented images.

## Example code

```
# Import the ImageDataGenerator
from keras.preprocessing.image import ImageDataGenerator

# Create an ImageDataGenerator and set parameters
datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)

# Load images from the directory
generator = datagen.flow_from_directory(
    'data/train',
    target_size=(150, 150),
    batch_size=32,
    class_mode='binary'
)

# Generate batches of augmented images
for data_batch, labels_batch in generator:
    print('data batch shape:', data_batch.shape)
    print('labels batch shape:', labels_batch.shape)
    break

```
## Output example

```
data batch shape: (32, 150, 150, 3)
labels batch shape: (32,)
```

The code above shows how to use the ImageDataGenerator to create batches of image data:

1. Import the ImageDataGenerator from keras.preprocessing.image.
2. Create an ImageDataGenerator and set parameters such as rescale, rotation_range, width_shift_range, height_shift_range, shear_range, zoom_range, and horizontal_flip.
3. Load images from the directory using the flow_from_directory method.
4. Generate batches of augmented images using a for loop.

## Helpful links

- [Keras ImageDataGenerator Documentation](https://keras.io/preprocessing/image/)
- [Keras Image Preprocessing Tutorial](https://www.pyimagesearch.com/2018/12/24/how-to-use-keras-fit-and-fit_generator-a-hands-on-tutorial/)

onelinerhub: [How do I use the Python Keras ImageDataGenerator to create batches of image data?](https://onelinerhub.com/python-keras/how-do-i-use-the-python-keras-imagedatagenerator-to-create-batches-of-image-data)
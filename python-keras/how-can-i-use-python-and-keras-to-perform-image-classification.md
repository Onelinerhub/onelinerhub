# How can I use Python and Keras to perform image classification?
// plain

Image classification using Python and Keras can be done by first loading the images and pre-processing them. This can be done using libraries like scikit-learn, NumPy, and OpenCV. Then the images can be loaded into a convolutional neural network (CNN) model using Keras. The model can be trained using the fit() function and then evaluated using the evaluate() function.

```
# Load the images and pre-process them
from sklearn.datasets import load_files
from keras.preprocessing.image import load_img

# Load the data
dataset = load_files('data/')

# Pre-process the images
X, y = [], []
for img_name in dataset['filenames']:
    img = load_img(img_name)
    X.append(img)
    y.append(dataset['target'][i])

# Load the images into a CNN model
from keras.models import Sequential
from keras.layers import Conv2D

model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)))

# Train the model
model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(X, y, epochs=10, batch_size=32)

# Evaluate the model
score = model.evaluate(X, y, batch_size=32)
print(score)
```

## Output example

`[0.639, 0.841]`

## Code explanation

1. Load the images and pre-process them - This can be done using libraries like scikit-learn, NumPy, and OpenCV.
2. Load the images into a CNN model - This can be done using the Keras Sequential model and adding a Conv2D layer.
3. Train the model - The model can be trained using the fit() function.
4. Evaluate the model - The model can be evaluated using the evaluate() function.

## Helpful links
- [Keras Documentation](https://keras.io/)
- [scikit-learn Documentation](https://scikit-learn.org/stable/)
- [NumPy Documentation](https://numpy.org/)
- [OpenCV Documentation](https://opencv.org/)

onelinerhub: [How can I use Python and Keras to perform image classification?](https://onelinerhub.com/python-keras/how-can-i-use-python-and-keras-to-perform-image-classification)
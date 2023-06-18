# How can I use Python and SciPy to downsample an image?
// plain

Using Python and SciPy, you can downsample an image by first loading it into an array using SciPy's `imread()` function. Then, use SciPy's `resize()` function to downsize the image.

## Example code

```
from scipy.misc import imread, imsave, imresize

# Read an JPEG image into a numpy array
img = imread('assets/cat.jpg')

# Resize the image
img_resized = imresize(img, (300, 300))

# Save the resized image
imsave('assets/cat_resized.jpg', img_resized)
```

The above code will read the image `cat.jpg` from the `assets` folder, resize it to 300x300 pixels, and save it as `cat_resized.jpg` in the `assets` folder.

## Code explanation

1. `imread()`: Loads the image into a numpy array
2. `imresize()`: Resizes the image
3. `imsave()`: Saves the resized image

## Helpful links
- SciPy Documentation: https://docs.scipy.org/doc/scipy/reference/
- SciPy Image Processing: https://scipy-lectures.org/advanced/image_processing/

onelinerhub: [How can I use Python and SciPy to downsample an image?](https://onelinerhub.com/python-scipy/how-can-i-use-python-and-scipy-to-downsample-an-image)
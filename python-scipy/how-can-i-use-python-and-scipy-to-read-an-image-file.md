# How can I use Python and SciPy to read an image file?
// plain

Using Python and SciPy to read an image file is relatively straightforward. The following example code reads in an image file and prints out its dimensions:

```
from scipy import misc
img = misc.imread('image.jpg')
print(img.shape)
```

## Output example
 `(300, 400, 3)`

The code is composed of the following parts:

1. `from scipy import misc` imports the SciPy module `misc` which contains functions to work with images.
2. `img = misc.imread('image.jpg')` reads in the image file `image.jpg` and stores it as an array in the variable `img`.
3. `print(img.shape)` prints out the shape of the array `img`, which is the dimensions of the image.

## Helpful links

- [SciPy Documentation](https://docs.scipy.org/doc/scipy/reference/index.html)
- [SciPy Image Processing Tutorial](https://scipy-lectures.org/advanced/image_processing/index.html)

onelinerhub: [How can I use Python and SciPy to read an image file?](https://onelinerhub.com/python-scipy/how-can-i-use-python-and-scipy-to-read-an-image-file)
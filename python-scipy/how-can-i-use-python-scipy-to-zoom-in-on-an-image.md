# How can I use Python Scipy to zoom in on an image?
// plain

Python Scipy can be used to zoom in on an image by using the `zoom()` function. This function takes an array and a zoom factor as parameters and returns a zoomed array. The following example code zooms in on a sample image by a factor of two:

```
from scipy.ndimage import zoom
from scipy import misc

img = misc.face()
zoomed_img = zoom(img, 2)
```

The output of the above code is an array which contains the zoomed image.

## Code explanation


1. `from scipy.ndimage import zoom`: This imports the `zoom` function from the `scipy.ndimage` module.
2. `from scipy import misc`: This imports the `misc` module from `scipy`.
3. `img = misc.face()`: This stores the sample image in the `img` variable.
4. `zoomed_img = zoom(img, 2)`: This calls the `zoom` function with the `img` array and a zoom factor of two as parameters and stores the resulting array in the `zoomed_img` variable.

## Helpful links

- [Scipy Documentation](https://docs.scipy.org/doc/scipy/reference/ndimage.html)
- [Scipy Zoom Example](https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.zoom.html)

onelinerhub: [How can I use Python Scipy to zoom in on an image?](https://onelinerhub.com/python-scipy/how-can-i-use-python-scipy-to-zoom-in-on-an-image)
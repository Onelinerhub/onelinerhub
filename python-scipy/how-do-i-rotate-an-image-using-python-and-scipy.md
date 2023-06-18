# How do I rotate an image using Python and SciPy?
// plain

To rotate an image using Python and SciPy, you can use the `ndimage.rotate` function. This function takes in an image array, an angle in degrees, and optionally an order of interpolation. The following example rotates an image 90 degrees clockwise:

```
from scipy import ndimage
import matplotlib.pyplot as plt

# Load the image
img = plt.imread('image.jpg')

# Rotate the image 90 degrees clockwise
rotated_img = ndimage.rotate(img, 90)

# Show the rotated image
plt.imshow(rotated_img)
```

![Rotated Image](rotated_image.jpg)

## Code explanation

- `from scipy import ndimage`: imports the `ndimage` module from `scipy`
- `import matplotlib.pyplot as plt`: imports the `pyplot` module from `matplotlib`
- `img = plt.imread('image.jpg')`: loads the image from the specified filename
- `rotated_img = ndimage.rotate(img, 90)`: rotates the image by 90 degrees clockwise
- `plt.imshow(rotated_img)`: displays the rotated image

## Helpful links
- [SciPy ndimage rotate documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.rotate.html)
- [Matplotlib pyplot imread documentation](https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.imread.html)
- [Matplotlib pyplot imshow documentation](https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.imshow.html)

onelinerhub: [How do I rotate an image using Python and SciPy?](https://onelinerhub.com/python-scipy/how-do-i-rotate-an-image-using-python-and-scipy)
# How can I use Python and SciPy to apply a Gaussian filter?
// plain

Using Python and SciPy, a Gaussian filter can be applied to an image. To do this, the ```scipy.ndimage.filters.gaussian_filter``` function can be used. For example, the following code will apply a Gaussian filter to an image, where ```img``` is the image array and ```sigma``` is the standard deviation for the Gaussian kernel:

```
from scipy.ndimage.filters import gaussian_filter
filtered_img = gaussian_filter(img, sigma=sigma)
```

The parts of the code are as follows:

- ```from scipy.ndimage.filters import gaussian_filter``` imports the ```gaussian_filter``` function from SciPy.
- ```gaussian_filter(img, sigma=sigma)``` applies the Gaussian filter to the image array ```img``` with standard deviation ```sigma```.
- ```filtered_img``` is the filtered image array.

## Helpful links

- [scipy.ndimage.filters.gaussian_filter](https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.filters.gaussian_filter.html)

onelinerhub: [How can I use Python and SciPy to apply a Gaussian filter?](https://onelinerhub.com/python-scipy/how-can-i-use-python-and-scipy-to-apply-a-gaussian-filter)
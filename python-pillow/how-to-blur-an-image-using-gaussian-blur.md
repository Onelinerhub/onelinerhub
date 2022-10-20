# How to blur an image using Gaussian blur

```python
from PIL import Image, ImageFilter

im = Image.open('/var/www/examples/heroine.png')
im = im.filter(ImageFilter.GaussianBlur(15))

im.show()
```

- `PIL` - import [lib:Pillow](https://onelinerhub.com/python-pillow/how-to-install-python-pillow-module) package modules
- `Image.open` - open given image with Pillow
- `/var/www/examples/heroine.png` - path to sample image to open
- `.filter(` - add specified filter to an image
- `ImageFilter.GaussianBlur` - blur type we use
- `15` - blur radius (strength of blur, the larger the more blurry image we get)
- `.show()` - displays resulting image

group: blur

## Example: 
```python
from PIL import Image, ImageFilter

im = Image.open('/var/www/examples/heroine.png')
im = im.filter(ImageFilter.GaussianBlur(15))

im.show()
```


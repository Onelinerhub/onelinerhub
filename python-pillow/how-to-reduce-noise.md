# How to reduce noise

### Most efficient way to get rid of noise - is to use [blurring](https://onelinerhub.com/python-pillow/how-to-blur-an-image):

```python
from PIL import Image, ImageFilter

im = Image.open('/var/www/examples/noisy.png')
im = im.filter(ImageFilter.BLUR)
im.show()
```

- `PIL` - import [lib:Pillow](https://onelinerhub.com/python-pillow/how-to-install-python-pillow-module) package modules
- `Image.open` - open given image with Pillow
- `.filter(` - apply given filter to an image
- `ImageFilter.BLUR` - blurs an image
- `.show()` - displays resulting image

group: noise

## Example: 
```python
from PIL import Image, ImageFilter

im = Image.open('/var/www/examples/noisy.png')
im = im.filter(ImageFilter.BLUR)
im.show()
```


# How to rotate image without cropping

```python
from PIL import Image, ImageEnhance

im = Image.open('/var/www/examples/heroine.png')
im = im.rotate(90, expand=True)

im.show()
```

- `PIL` - import [lib:Pillow](https://onelinerhub.com/python-pillow/how-to-install-python-pillow-module) package modules
- `Image.open` - open given image with Pillow
- `.rotate(` - rotate given image
- `expand=True` - increase image size instead of cropping while rotating
- `.show()` - displays resulting image

group: rotate

## Example: 
```python
from PIL import Image, ImageEnhance

im = Image.open('/var/www/examples/heroine.png')
im = im.rotate(90, expand=True)

im.show()
```


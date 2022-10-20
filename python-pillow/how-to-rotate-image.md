# How to rotate image 90 degrees

```python
from PIL import Image, ImageEnhance

im = Image.open('/var/www/examples/heroine.png')
im = im.rotate(90)

im.show()
```

- `PIL` - import [lib:Pillow](https://onelinerhub.com/python-pillow/how-to-install-python-pillow-module) package modules
- `Image.open` - open given image with Pillow
- `.rotate(` - rotate given image
- `90` - degrees to rotate given image by
- `.show()` - displays resulting image

group: rotate

## Example: 
```python
from PIL import Image, ImageEnhance

im = Image.open('/var/www/examples/heroine.png')
im = im.rotate(90)

im.show()
```


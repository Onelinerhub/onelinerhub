# How to convert an image to grayscale

```python
from PIL import Image, ImageFilter

im = Image.open('/var/www/examples/heroine.png')
im = im.convert('L')

im.show()
```

- `PIL` - import [lib:Pillow](https://onelinerhub.com/python-pillow/how-to-install-python-pillow-module) package modules
- `Image.open` - open given image with Pillow
- `convert('L')` - convert image to gray scale colors
- `.show()` - displays resulting image

group: black_white

## Example: 
```python
from PIL import Image, ImageFilter

im = Image.open('/var/www/examples/heroine.png')
im = im.convert('L')

im.show()
```


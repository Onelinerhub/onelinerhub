# How to create square thumbnail (cropped to fit)

```python
from PIL import Image, ImageOps

im = Image.open('/var/www/examples/heroine.png')
im = ImageOps.fit(im, (100,100), Image.ANTIALIAS)

im.show()
```

- `PIL` - import [lib:Pillow](https://onelinerhub.com/python-pillow/how-to-install-python-pillow-module) package modules
- `Image.open` - open given image with Pillow
- `100,100` - thumbnail square area width and height
- `ImageOps.fit(` - fits an image into given area
- `.show()` - displays resulting image

group: resize

## Example: 
```python
from PIL import Image, ImageOps

im = Image.open('/var/www/examples/heroine.png')
im = ImageOps.fit(im, (100,100), Image.ANTIALIAS)

im.show()
```


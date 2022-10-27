# How to resize and image and maintain aspect ratio

```python
from PIL import Image, ImageDraw, ImageFont

im = Image.open('/var/www/examples/heroine.png')
width = 100
height = width * im.size[1]/im.size[0]
im = im.resize((width, height))

im.show()
```

- `PIL` - import [lib:Pillow](https://onelinerhub.com/python-pillow/how-to-install-python-pillow-module) package modules
- `Image.open` - open given image with Pillow
- `100` - resized image width
- `im.size` - returns original image width and height
- `width * im.size[1]/im.size[0]` - calculates height so that aspect ratio is maintained
- `.resize(` - resizes given image to the specified size
- `.show()` - displays resulting image

group: resize

## Example: 
```python
from PIL import Image, ImageDraw, ImageFont

im = Image.open('/var/www/examples/heroine.png')
width = 150
height = round(width * im.size[1]/im.size[0])
im = im.resize((width, height))
im.show()
```


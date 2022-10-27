# How to change pixel color

```python
from PIL import Image

im = Image.open('/var/www/examples/small.png')
im.putpixel((10, 20), (255,255,255))

im.show()
```

- `PIL` - import [lib:Pillow](https://onelinerhub.com/python-pillow/how-to-install-python-pillow-module) package modules
- `Image.open` - open given image with Pillow
- `.putpixel(` - sets color of a given pixel
- `(10, 20)` - coordinates of the pixel to set color for
- `(255,255,255)` - RGB color (in a tuple form) to set
- `.show()` - displays resulting image

group: pixel

## Example: 
```python
from PIL import Image

im = Image.open('/var/www/examples/heroine.png')
for i in range(0, 700):
  im.putpixel((i,i), (255,255,255))
  im.putpixel((i,i+1), (255,255,255))
  im.putpixel((i,i+2), (255,255,255))

im.show()
```


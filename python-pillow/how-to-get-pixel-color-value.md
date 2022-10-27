# How to get pixel color value

```python
from PIL import Image

im = Image.open('/var/www/examples/small.png')
rgb = im.getpixel((20, 20))
```

- `PIL` - import [lib:Pillow](https://onelinerhub.com/python-pillow/how-to-install-python-pillow-module) package modules
- `Image.open` - open given image with Pillow
- `.getpixel(` - returns pixel color value based on given coordinates
- `(20, 20)` - get pixel color at `20` from left and `20` from top
- `rgb` - will contain tuple of `3` (or `4`) items representing RGB values (and opacity when relevant)

group: pixel

## Example: 
```python
from PIL import Image

im = Image.open('/var/www/examples/small.png')
rgb = im.getpixel((20, 20))

print(rgb)
```
```
(255, 215, 50, 255)

```


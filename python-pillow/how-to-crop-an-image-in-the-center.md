# How to crop an image in the center

```python
from PIL import Image, ImageDraw, ImageFont

im = Image.open('/var/www/examples/heroine.png')
crop = (400, 400)
left = round((im.size[0] - crop[0])/2)
top = round((im.size[1] - crop[1])/2)
im = im.crop((left, top, crop[0]+left, crop[1] + top))

im.show()
```

- `PIL` - import [lib:Pillow](https://onelinerhub.com/python-pillow/how-to-install-python-pillow-module) package modules
- `Image.open` - open given image with Pillow
- `/var/www/examples/heroine.png` - path to sample image to open
- `.crop(` - crops image to a given area
- `300, 200` - top left corner of a crop area
- `500, 800` - bottom right corner of a crop area
- `.show()` - displays resulting image

group: crop

## Example: 
```python
from PIL import Image, ImageDraw, ImageFont

im = Image.open('/var/www/examples/heroine.png')
im = im.crop((300, 200, 500, 800))

im.show()
```


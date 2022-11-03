# How to add noise

### Pillow doesn't have integrated noise methods, but noise can be easily simulated using [putpixel()](https://onelinerhub.com/python-pillow/how-to-change-pixel-color) to set random color for random pixels of an image:

```python
from PIL import Image
import random

im = Image.open('/var/www/examples/heroine.png')
for i in range( round(im.size[0]*im.size[1]/5) ):
  im.putpixel(
    (random.randint(0, im.size[0]-1), random.randint(0, im.size[1]-1)),
    (random.randint(0,255),random.randint(0,255),random.randint(0,255))
  )

im.show()
```

- `PIL` - import [lib:Pillow](https://onelinerhub.com/python-pillow/how-to-install-python-pillow-module) package modules
- `Image.open` - open given image with Pillow
- `round(im.size[0]*im.size[1]/5` - each 5th pixel will be noised out (change `5` to larger values to decrease noise density)
- `.putpixel(` - sets color of a given pixel
- `.show()` - displays resulting image

group: noise

## Example: 
```python
from PIL import Image, ImageFilter
import random

im = Image.open('/var/www/examples/heroine.png')
for i in range( round(im.size[0]*im.size[1]/5) ):
  im.putpixel(
    (random.randint(0, im.size[0]-1), random.randint(0, im.size[1]-1)),
    (random.randint(0,255),random.randint(0,255),random.randint(0,255))
  )

im.show()
```


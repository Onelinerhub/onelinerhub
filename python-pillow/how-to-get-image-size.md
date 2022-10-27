# How to get image size

```python
from PIL import Image, ImageDraw, ImageFont

im = Image.open('/var/www/examples/heroine.png')
width = im.size[0]
height = im.size[1]
```

- `PIL` - import [lib:Pillow](https://onelinerhub.com/python-pillow/how-to-install-python-pillow-module) package modules
- `Image.open` - open given image with Pillow
- `/var/www/examples/heroine.png` - path to sample image to open
- `im.size` - returns original image width and height
- `im.size[0]` - image width
- `im.size[1]` - image height

## Example: 
```python
from PIL import Image, ImageDraw, ImageFont

im = Image.open('/var/www/examples/heroine.png')
width = im.size[0]
height = im.size[1]

print(width, height)
```
```
733 1100

```


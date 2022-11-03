# How to find image edges

```python
from PIL import Image, ImageFilter

im = Image.open('/var/www/examples/heroine.png')
im = im.convert("L")
im = im.filter(ImageFilter.FIND_EDGES)

im.show()
```

- `PIL` - import [lib:Pillow](https://onelinerhub.com/python-pillow/how-to-install-python-pillow-module) package modules
- `Image.open` - open given image with Pillow
- `.convert("L")` - convert image to grayscale to prepare it for edge detection
- `.filter(` - apply given filter to an image
- `ImageFilter.FIND_EDGES` - this filter highlights edges of an image and removed everything else
- `.show()` - displays resulting image

## Example: 
```python
from PIL import Image, ImageFilter

im = Image.open('/var/www/examples/heroine.png')
im = im.convert("L")
im = im.filter(ImageFilter.FIND_EDGES)

im.show()
```


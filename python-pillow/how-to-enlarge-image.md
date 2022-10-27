# How to enlarge (scale up) an image

```python
from PIL import Image

im = Image.open('/var/www/examples/small.png')
im = im.resize((150, 150))

im.show()
```

- `PIL` - import [lib:Pillow](https://onelinerhub.com/python-pillow/how-to-install-python-pillow-module) package modules
- `Image.open` - open given image with Pillow
- `.resize(` - resizes given image to the specified size
- `(150, 150)` - width and height to enlarge our image to
- `.show()` - displays resulting image

## Example: 
```python
from PIL import Image

im = Image.open('/var/www/examples/small.png')
im = im.resize((150, 150))

im.show()
```


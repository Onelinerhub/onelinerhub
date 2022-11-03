# How to to image opacity

```python
from PIL import Image

im = Image.open('/var/www/examples/heroine.png')
im.putalpha(100)

im.show()
```

- `PIL` - import [lib:Pillow](https://onelinerhub.com/python-pillow/how-to-install-python-pillow-module) package modules
- `Image.open` - open given image with Pillow
- `.putalpha(` - change transparency of an image (the higher the value the less the transparency)
- `.show()` - displays resulting image

## Example: 
```python
from PIL import Image

im = Image.open('/var/www/examples/heroine.png')
im.putalpha(100)

im.show()
```


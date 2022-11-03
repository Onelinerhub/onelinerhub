# How to convert TIFF to JPG

```python
from PIL import Image

im = Image.open('image.tiff')
im.save('image.jpg')
```

- `PIL` - import [lib:Pillow](https://onelinerhub.com/python-pillow/how-to-install-python-pillow-module) package modules
- `Image.open` - open given image with Pillow
- `.save(` - saves image under given path (format is automatically picked based on file extension)

group: convert



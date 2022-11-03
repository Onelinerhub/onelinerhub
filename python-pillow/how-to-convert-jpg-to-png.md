# How to convert JPG to PNG

```python
from PIL import Image

im = Image.open('image.jpg')
im.save('image.png')
```

- `PIL` - import [lib:Pillow](https://onelinerhub.com/python-pillow/how-to-install-python-pillow-module) package modules
- `Image.open` - open given image with Pillow
- `.save(` - saves image under given path (format is automatically picked based on file extension)

group: convert



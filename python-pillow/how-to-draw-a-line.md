# How to draw a line

```python
from PIL import Image, ImageDraw
  
im = Image.new("RGB", (400, 300))  
dr = ImageDraw.Draw(im)
dr.line([(50,200), (350,200)], fill ="white", width = 5)
im.show()
```

- `PIL` - import [lib:Pillow](https://onelinerhub.com/python-pillow/how-to-install-python-pillow-module) package modules
- `Image.new` - create new `PIL` image object
- `ImageDraw.Draw` - create drawing object
- `.line(` - draws a line
- `(50,200), (350,200)` - starting and ending coordinates of a line
- `.show()` - displays resulting image

group: draw

## Example: 
```python
from PIL import Image, ImageDraw
  
im = Image.new("RGB", (400, 300))  
dr = ImageDraw.Draw(im)
dr.line([(50,200), (350,200)], fill ="white", width = 5)
im.show()
```


# How to draw a point

```python
from PIL import Image, ImageDraw
  
im = Image.new("RGB", (400, 300))  
dr = ImageDraw.Draw(im)
dr.point((50,50), fill="white")
im.show()
```

- `PIL` - import [lib:Pillow](https://onelinerhub.com/python-pillow/how-to-install-python-pillow-module) package modules
- `Image.new` - create new `PIL` image object
- `ImageDraw.Draw` - create drawing object
- `.point(` - draws a single point
- `(50,50)` - point coordinates
- `.show()` - displays resulting image

group: draw

## Example: 
```python
from PIL import Image, ImageDraw
  
im = Image.new("RGB", (400, 300))  
dr = ImageDraw.Draw(im)
for i in range(30):
  dr.point((i * 10,300-i * 10), fill="white")
im.show()
```


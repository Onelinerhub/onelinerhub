# How to draw a triangle

```python
from PIL import Image, ImageDraw
  
im = Image.new("RGB", (400, 300))  
dr = ImageDraw.Draw(im)
dr.polygon([(50,50), (350,150), (200, 250)], outline="white")
im.show()
```

- `PIL` - import [lib:Pillow](https://onelinerhub.com/python-pillow/how-to-install-python-pillow-module) package modules
- `Image.new` - create new `PIL` image object
- `ImageDraw.Draw` - create drawing object
- `.polygon(` - draws polygon from given coordinates (with any number of dots)
- `(50,50), (350,150), (200, 250)` - triangle dots coordinates
- `.show()` - displays resulting image

group: draw

## Example: 
```python
from PIL import Image, ImageDraw
  
im = Image.new("RGB", (400, 300))  
dr = ImageDraw.Draw(im)
dr.polygon([(50,50), (350,150), (200, 250)], outline="white")
im.show()
```


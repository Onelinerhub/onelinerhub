# How to draw an ellipse

```python
from PIL import Image, ImageDraw
  
im = Image.new("RGB", (400, 300))  
dr = ImageDraw.Draw(im)
dr.ellipse([(50,50), (350,250)], outline ="white")
im.show()
```

- `PIL` - import [lib:Pillow](https://onelinerhub.com/python-pillow/how-to-install-python-pillow-module) package modules
- `Image.new` - create new `PIL` image object
- `ImageDraw.Draw` - create drawing object
- `.ellipse(` - draws an ellipse
- `(50,50), (350,250)` - bounding rectangle to fit ellipse into
- `outline` - ellipse border color
- `.show()` - displays resulting image

group: draw

## Example: 
```python
from PIL import Image, ImageDraw
  
im = Image.new("RGB", (400, 300))  
dr = ImageDraw.Draw(im)
dr.ellipse([(50,50), (350,250)], outline ="white")
im.show()
```


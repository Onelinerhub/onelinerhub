# How to draw an arc

```python
from PIL import Image, ImageDraw
  
im = Image.new("RGB", (400, 300))  
dr = ImageDraw.Draw(im)
dr.arc([(50,50), (350,250)], start = 20, end = 230, fill ="white")
im.show()
```

- `PIL` - import [lib:Pillow](https://onelinerhub.com/python-pillow/how-to-install-python-pillow-module) package modules
- `Image.new` - create new `PIL` image object
- `ImageDraw.Draw` - create drawing object
- `.arc(` - draws an arc
- `(50,50), (350,250)` - coordinates of an arc bounding rectangle
- `start = 20` - starting angle (starts from 3pm)
- `end = 230` - ending angle
- `.show()` - displays resulting image

group: draw

## Example: 
```python
from PIL import Image, ImageDraw
  
im = Image.new("RGB", (400, 300))  
dr = ImageDraw.Draw(im)
dr.arc([(50,50), (350,250)], start = 20, end = 230, fill ="white")
im.show()
```


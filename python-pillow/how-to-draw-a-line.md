# How to draw a line

```python
from PIL import Image, ImageDraw
  
im = ImageDraw.Draw( Image.new("RGB", (400, 300)) )
im.line([(50,50), (250,200)], fill ="none", width = 0)
im.show()
```


group: draw



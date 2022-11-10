# How to draw ellipse

```python
from PIL import Image, ImageDraw
  
im = Image.new("RGB", (400, 300))  
dr = ImageDraw.Draw(im)
dr.ellipse([(50,50), (350,250)], outline ="white")
im.show()
```


group: draw



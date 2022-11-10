# How to draw an arc

```python
from PIL import Image, ImageDraw
  
im = Image.new("RGB", (400, 300))  
dr = ImageDraw.Draw(im)
dr.arc([(50,200), (350,200)], start = 20, end = 130, fill ="white")
im.show()
```


group: draw



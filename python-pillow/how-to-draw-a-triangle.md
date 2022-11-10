# How to draw a triangle

```python
from PIL import Image, ImageDraw
  
im = Image.new("RGB", (400, 300))  
dr = ImageDraw.Draw(im)
dr.polygon([(50,50), (350,150), (200, 250)], outline="white")
im.show()
```


group: draw

## Example: 
```python
from PIL import Image, ImageDraw
  
im = Image.new("RGB", (400, 300))  
dr = ImageDraw.Draw(im)
dr.polygon([(50,50), (350,150), (200, 250)], outline="white")
im.show()
```


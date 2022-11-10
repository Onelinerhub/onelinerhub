# How to draw rectangle

```python
from PIL import Image, ImageDraw
  
im = Image.new("RGB", (400, 300))  
dr = ImageDraw.Draw(im)
dr.rectangle([(50,50), (350,250)], outline="white")
im.show()
```


group: draw

## Example: 
```python
from PIL import Image, ImageDraw
  
im = Image.new("RGB", (400, 300))  
dr = ImageDraw.Draw(im)
dr.rectangle([(50,50), (350,250)], outline="white")
im.show()
```


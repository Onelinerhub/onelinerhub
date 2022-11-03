# How to add noise

```python
from PIL import Image, ImageFilter, random

im = Image.open('/var/www/examples/heroine.png')
im[0][0]=255

im.show()
```


group: noise

## Example: 
```python
from PIL import Image, ImageFilter, random

im = Image.open('/var/www/examples/heroine.png')
for i in range(100):
  im.putpixel((random.randint(0, 100), random.randint(0, 100)), (255,255,255))

im.show()
```


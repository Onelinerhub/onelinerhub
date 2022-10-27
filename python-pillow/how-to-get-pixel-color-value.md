# How to get pixel color value

```python
from PIL import Image

im = Image.open('/var/www/examples/small.png')
rgb = im.getpixel(20, 20)
```


group: pixel

## Example: 
```python
from PIL import Image

im = Image.open('/var/www/examples/small.png')
rgb = im.getpixel((20, 20))

print(rgb)
```
```
(255, 215, 50, 255)

```


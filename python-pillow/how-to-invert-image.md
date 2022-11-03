# How to invert image

```python
from PIL import Image, ImageOps

im = Image.open('/var/www/examples/heroine.png')
im = ImageOps.invert(im)

im.show()
```


## Example: 
```python
from PIL import Image, ImageOps

im = Image.open('/var/www/examples/heroine.png')
im = ImageOps.invert(im)

im.show()
```


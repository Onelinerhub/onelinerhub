# How to mirror image

```python
from PIL import Image, ImageOps

im = Image.open('/var/www/examples/heroine.png')
im = ImageOps.mirror(im)

im.show()
```


group: flip_mirror

## Example: 
```python
from PIL import Image, ImageOps

im = Image.open('/var/www/examples/heroine.png')
im = ImageOps.mirror(im)

im.show()
```


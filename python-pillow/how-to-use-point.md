# How to use point()

```python
from PIL import Image, ImageOps

im = Image.open('/var/www/examples/heroine.png')

im = im.point(lambda p: p >value 100 and 255)
im.show()
```


## Example: 
```python
from PIL import Image, ImageOps

im = Image.open('/var/www/examples/heroine.png')

im = im.point(lambda p: p >value 100 and 255)
im.show()
```


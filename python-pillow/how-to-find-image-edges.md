# How to find image edges

```python
from PIL import Image, ImageFilter

im = Image.open('/var/www/examples/heroine.png')
im = im.convert("L")
im = im.filter(ImageFilter.FIND_EDGES)

im.show()
```


## Example: 
```python
from PIL import Image, ImageFilter

im = Image.open('/var/www/examples/heroine.png')
im = im.convert("L")
im = im.filter(ImageFilter.FIND_EDGES)

im.show()
```


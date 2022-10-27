# How to flip an image

```python
from PIL import Image

im = Image.open('/var/www/examples/heroine.png')
im = im.flip()

im.show()
```


group: flip_mirror



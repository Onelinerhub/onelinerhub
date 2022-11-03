# How to reduce noise

```python
from PIL import Image

im = Image.open('/var/www/examples/noisy.png')
im = im.filter(ImageFilter.MinFilter(3))
im.show()
```


group: noise



# How to enlarge image

```python
from PIL import Image

im = Image.open('/var/www/examples/small.png')
im = im.resize((100, 100))

im.show()
```




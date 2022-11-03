# How to to image opacity

```python
from PIL import Image

im = Image.open('/var/www/examples/heroine.png')
im.putalpha(100)

im.show()
```


## Example: 
```python
from PIL import Image

im = Image.open('/var/www/examples/heroine.png')
im.putalpha(100)

im.show()
```


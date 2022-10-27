# How to change pixel color

```python
from PIL import Image

im = Image.open('/var/www/examples/small.png')
p = im.load()
p[21,21] = (0,0,0,0)

im.show()
```


group: pixel

## Example: 
```python
from PIL import Image

im = Image.open('/var/www/examples/small.png')
p = im.load()
p[21,21] = (0,0,0,0)

im.show()
```


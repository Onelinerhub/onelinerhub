# Using mask to merge images

```python
from PIL import Image

im = Image.open('/var/www/examples/heroine.png'))
im_merge = Image.open('/var/www/examples/small.png')

im.paste(im_merge, 10, 10)

im.show()
```


group: merge

## Example: 
```python
from PIL import Image

im = Image.open('/var/www/examples/heroine.png'))
im_merge = Image.open('/var/www/examples/small.png')

im.paste(im_merge, 10, 10)

im.show()
```


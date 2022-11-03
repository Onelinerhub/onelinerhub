# How to add watermark to image

```python
from PIL import Image

im = Image.open('/var/www/examples/heroine.png')
im_merge = Image.open('/var/www/examples/hammer.png')
im_merge.putalpha(100)

im.paste(im_merge, (40, 500), im_merge)

im.show()
```


group: merge

## Example: 
```python
from PIL import Image

im = Image.open('/var/www/examples/heroine.png')
im_merge = Image.open('/var/www/examples/hammer.png')
im_merge.putalpha(100)

im.paste(im_merge, (40, 500), im_merge)

im.show()
```


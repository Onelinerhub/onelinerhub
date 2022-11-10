# How to get array from image

```python
from PIL import Image

im = Image.open('/var/www/examples/heroine.png')
data = im.asarray()
```

- `PIL` - import [lib:Pillow](https://onelinerhub.com/python-pillow/how-to-install-python-pillow-module) package modules
- `np.random.randint(` - generate matrix of the given shape with random integers in the given range
- `Image.fromarray(` - creates image from given array
- `mode="L"` - creates image in black and white mode
- `.show()` - displays resulting image

group: array

## Example: 
```python
from PIL import Image

im = Image.open('/var/www/examples/heroine.png')
data = im.asarray()

print(len(data))
```


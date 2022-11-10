# How to get image from an array

```python
from PIL import Image
import numpy as np

data = np.random.randint(1, 255, (100,300))
im = Image.fromarray(data, mode="L")
im.show()
```

- `PIL` - import [lib:Pillow](https://onelinerhub.com/python-pillow/how-to-install-python-pillow-module) package modules
- `np.random.randint(` - generate matrix of the given shape with random integers in the given range
- `Image.fromarray(` - creates image from given array
- `mode="L"` - creates image in black and white mode
- `.show()` - displays resulting image

## Example: 
```python
from PIL import Image
import numpy as np

data = np.random.randint(1, 255, (100,300))
im = Image.fromarray( data, mode="L" )
im.show()
```


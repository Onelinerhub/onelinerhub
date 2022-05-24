# How to get complex number magnitude

```python
import numpy as np
z = 3 + 4j
magnitude = np.abs(z)
```

- `z` - declared complex number
- `3` - real part
- `4` - imaginary part
- `.abs` - returns complex number magnitude
- `magnitude` - will contain calculated magnitude value (`sqrt(3*3 + 4*4)`)

group: complex

## Example: 
```python
import numpy as np
z = 3+4j
print(np.abs(z))
```
```
5.0

```


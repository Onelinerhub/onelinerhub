# How to get angle in degrees from complex number

```python
import numpy as np
za = np.angle(3+4j, True)
```

- `3` - real part
- `4` - imaginary part
- `.angle` - computes angle of the complex argument
- `za` - will contain computed value in degrees
- `True` - set second argument to `True` to return value in degrees

group: complex

## Example: 
```python
import numpy as np
z = 3+4j
za = np.angle(z, True)
print(za)
```
```
53.13010235415598

```

link_youtube: https://youtu.be/fxwy3axHYeM

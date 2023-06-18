# angles

How do I use Python Scipy to rotate an object using Euler angles?
// plain

Python Scipy can be used to rotate an object using Euler angles by using the `scipy.spatial.transform.Rotation` class. The `Rotation` class takes in three Euler angles as parameters which represent the angles of rotation in the x, y, and z axis respectively.

The following example code block demonstrates how to use the `Rotation` class to rotate an object in 3D space using Euler angles:

```
# import the Rotation class from scipy
from scipy.spatial.transform import Rotation

# define the Euler angles
euler_angles = [0.1, 0.2, 0.3]

# create the Rotation object
rotation = Rotation.from_euler('xyz', euler_angles)

# rotate the object
rotated_object = rotation.apply(object)
```

The code above consists of the following parts:
1. `from scipy.spatial.transform import Rotation` imports the `Rotation` class from the `scipy.spatial.transform` module.
2. `euler_angles = [0.1, 0.2, 0.3]` defines the Euler angles representing the angle of rotation in the x, y, and z axis respectively.
3. `rotation = Rotation.from_euler('xyz', euler_angles)` creates a `Rotation` object using the Euler angles.
4. `rotated_object = rotation.apply(object)` rotates the object using the `Rotation` object.

## Helpful links
- [Scipy Documentation for Rotation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.transform.Rotation.html)

onelinerhub: [angles

How do I use Python Scipy to rotate an object using Euler angles?](https://onelinerhub.com/python-scipy/angles--how-do-i-use-python-scipy-to-rotate-an-object-using-euler-angles)
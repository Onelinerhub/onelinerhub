# How do I check the version of Python Numpy I am using?
// plain

To check the version of Python Numpy you are using, you can use the `np.__version__` command. This command will return the version of Numpy as a string.

For example,
```
import numpy as np

np.__version__
```

## Output example

```
'1.18.1'
```

The code above imports the Numpy library as `np`, and then calls the `np.__version__` command to print out the version of Numpy.

In addition, you can also check the version of Numpy from the command line. To do this, just type `python -c "import numpy; print(numpy.__version__)"` and it will return the version of Numpy.

## Code explanation

- `import numpy as np`: imports the Numpy library as `np`
- `np.__version__`: calls the `np.__version__` command to print out the version of Numpy
- `python -c "import numpy; print(numpy.__version__)"`: checks the version of Numpy from the command line

## Helpful links
- [Numpy Documentation](https://numpy.org/doc/)

onelinerhub: [How do I check the version of Python Numpy I am using?](https://onelinerhub.com/python-scipy/how-do-i-check-the-version-of-python-numpy-i-am-using)
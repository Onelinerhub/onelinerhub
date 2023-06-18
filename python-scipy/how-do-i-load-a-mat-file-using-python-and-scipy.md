# How do I load a MAT file using Python and SciPy?
// plain

To load a [MAT file](https://www.mathworks.com/help/matlab/import_export/mat-files.html) using Python and SciPy, use the `scipy.io.loadmat` function. This function takes the file path as an argument and returns a dictionary.

```python
import scipy.io
mat_file = scipy.io.loadmat('example.mat')
```

The returned dictionary contains the variables stored in the MAT file. The keys of the dictionary are the variable names and the values are the corresponding arrays.

```python
print(mat_file)
# {'__header__': b'MATLAB 5.0 MAT-file Platform: posix, Created on: Thu Jan 16 14:14:17 2020',
#  '__version__': '1.0',
#  '__globals__': [],
#  'example_array': array([[1, 2, 3],
#        [4, 5, 6]])}
```

The above example returns a dictionary with four keys. `__header__` contains the MATLAB version and the creation date. `__version__` contains the version of the MAT file. `__globals__` is an empty list. The last key `example_array` contains a 2x3 array.

## Helpful links
- [scipy.io.loadmat](https://docs.scipy.org/doc/scipy/reference/generated/scipy.io.loadmat.html)
- [MATLAB Import and Export](https://www.mathworks.com/help/matlab/import_export/mat-files.html)

onelinerhub: [How do I load a MAT file using Python and SciPy?](https://onelinerhub.com/python-scipy/how-do-i-load-a-mat-file-using-python-and-scipy)
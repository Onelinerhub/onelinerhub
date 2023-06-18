# How do I convert a Python Numpy array to a Pandas Dataframe?
// plain

Converting a Python Numpy array to a Pandas Dataframe is a simple task. The following example code demonstrates how to do this:

```python
import pandas as pd
import numpy as np

# Create a Numpy array
data = np.array([['','Col1','Col2'],
                ['Row1',1,2],
                ['Row2',3,4]])

# Create a Pandas Dataframe
df = pd.DataFrame(data=data[1:,1:],
                  index=data[1:,0],
                  columns=data[0,1:])

print(df)
```

## Output example

```
     Col1 Col2
Row1    1    2
Row2    3    4
```

The code above consists of the following parts:
1. `import pandas as pd` and `import numpy as np` - imports the necessary libraries for the task.
2. `data = np.array([['','Col1','Col2'], ['Row1',1,2], ['Row2',3,4]])` - creates a Numpy array with the data we want to convert.
3. `df = pd.DataFrame(data=data[1:,1:], index=data[1:,0], columns=data[0,1:])` - creates a Pandas Dataframe from the Numpy array.
4. `print(df)` - prints the Dataframe.

For more information, please refer to the following links:
- [Pandas Dataframe from Numpy Array](https://www.geeksforgeeks.org/create-dataframe-from-numpy-array-in-python-pandas/)
- [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)

onelinerhub: [How do I convert a Python Numpy array to a Pandas Dataframe?](https://onelinerhub.com/python-scipy/how-do-i-convert-a-python-numpy-array-to-a-pandas-dataframe)
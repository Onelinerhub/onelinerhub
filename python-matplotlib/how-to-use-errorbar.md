# How to use errorbar

```python
# Import Library

import matplotlib.pyplot as plt
  
# Define Data

x= [6, 15, 2.3, 9]
y= [9, 15, 20, 25]

# Define Error

x_error = [2.3, 5.1, 1, 3.1]

# Plot Bar chart

plt.bar(x,y)

# Plot error bar

plt.errorbar(x, y, xerr = x_error,fmt='o',ecolor = 'red',color='yellow')

# Display graph

plt.show()
```


## Example: 
```python
# Import Library

import matplotlib.pyplot as plt
  
# Define Data

x= [6, 15, 2.3, 9]
y= [9, 15, 20, 25]

# Define Error

x_error = [2.3, 5.1, 1, 3.1]

# Plot Bar chart

plt.bar(x,y)

# Plot error bar

plt.errorbar(x, y, xerr = x_error,fmt='o',ecolor = 'red',color='yellow')

# Display graph

plt.show()
```


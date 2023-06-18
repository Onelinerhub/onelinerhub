# How do I create a histogram using Python and SciPy?
// plain

To create a histogram using Python and SciPy, you can use the matplotlib.pyplot.hist() function. This function takes in an array of data and plots a histogram of the data.

```
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randint(1, 10, size=50)

plt.hist(data)
plt.show()
```

This will produce a histogram of the data:

![Histogram](histogram.png)

The matplotlib.pyplot.hist() function has several parameters that can be used to customize the histogram:

* bins: The number of bins used in the histogram (default is 10)
* range: The range of values for the histogram (default is the minimum and maximum of the data)
* density: Whether to normalize the data to form a probability density (default is False)
* cumulative: Whether to plot the cumulative distribution (default is False)

For example, to create a histogram with 20 bins and a range of 0 to 10:

```
plt.hist(data, bins=20, range=(0, 10))
plt.show()
```

This will produce a histogram with 20 bins and a range of 0 to 10:

![Histogram](histogram2.png)

For more information, see the [matplotlib.pyplot.hist() documentation](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.hist.html).

onelinerhub: [How do I create a histogram using Python and SciPy?](https://onelinerhub.com/python-scipy/how-do-i-create-a-histogram-using-python-and-scipy)
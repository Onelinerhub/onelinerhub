# How do I create a QQ plot using Python and SciPy?
// plain

To create a QQ plot using Python and SciPy, you can use the `probplot()` function from the `scipy.stats` module. This function takes two arguments, the first being the data to be plotted, and the second being the distribution of the data. Here is an example code block:

```
import matplotlib.pyplot as plt
from scipy.stats import probplot

data = [1,2,3,4,5,6]

probplot(data, dist='norm', plot=plt)
plt.show()
```

This will produce a QQ plot that looks like this:

![QQ plot](https://i.stack.imgur.com/2M6bv.png)

## Code explanation


* `import matplotlib.pyplot as plt` imports the `pyplot` module from the `matplotlib` library, which is used to display the plot.
* `from scipy.stats import probplot` imports the `probplot` function from the `scipy.stats` module, which is used to create the QQ plot.
* `data = [1,2,3,4,5,6]` creates a list of data points that will be plotted.
* `probplot(data, dist='norm', plot=plt)` calls the `probplot()` function with the data points and the normal distribution as arguments.
* `plt.show()` displays the plot.

For more information, see [this page](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.probplot.html) from the SciPy documentation.

onelinerhub: [How do I create a QQ plot using Python and SciPy?](https://onelinerhub.com/python-scipy/how-do-i-create-a-qq-plot-using-python-and-scipy)
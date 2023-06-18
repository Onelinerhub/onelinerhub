# How do I use the scipy qqplot function in Python?
// plain

The `scipy.stats.probplot` function can be used to create a Q-Q plot in Python. This function takes two arguments: an array of data and a distribution to compare the data to. The distribution is usually a normal distribution, but other distributions can be specified.

For example, to create a Q-Q plot for a sample of data:

```
import scipy.stats as stats
import matplotlib.pyplot as plt

data = [3, 5, 7, 9, 11, 13]

stats.probplot(data, dist="norm", plot=plt)
plt.show()
```

![qqplot](https://miro.medium.com/max/1000/1*WkP6_VhE3jU9zsXxVfP1GQ.png)

The code above will generate a Q-Q plot comparing the sample data to a normal distribution. The plot will show how closely the data follows the normal distribution.

The parts of the code are:

1. `import scipy.stats as stats`: This imports the `scipy.stats` module, which contains the `probplot` function.
2. `import matplotlib.pyplot as plt`: This imports the `matplotlib.pyplot` module, which is used to create the plot.
3. `data = [3, 5, 7, 9, 11, 13]`: This creates an array of data to be plotted.
4. `stats.probplot(data, dist="norm", plot=plt)`: This calls the `probplot` function, which generates the Q-Q plot. The `dist` argument specifies the distribution to compare the data to (in this case, a normal distribution). The `plot` argument specifies the plotting library to use (in this case, `matplotlib.pyplot`).
5. `plt.show()`: This displays the plot.

For more information about the `scipy.stats.probplot` function, see the [documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.probplot.html).

onelinerhub: [How do I use the scipy qqplot function in Python?](https://onelinerhub.com/python-scipy/how-do-i-use-the-scipy-qqplot-function-in-python)
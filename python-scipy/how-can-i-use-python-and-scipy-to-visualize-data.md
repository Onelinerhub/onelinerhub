# How can I use Python and SciPy to visualize data?
// plain

Python and SciPy provide a range of tools for visualizing data. To get started, you can import the matplotlib library, which contains functions for creating basic plots, such as line plots, histograms, and scatter plots.

For example, the following code block creates a simple line plot:
```
import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [1,4,9,16]

plt.plot(x,y)
plt.show()
```
## Output example


![Line Plot](https://miro.medium.com/max/1400/1*z1Vhc5jO7Bvz_Wb-L_p3Gg.png)

The code above first imports the `matplotlib.pyplot` library, which contains the `plot()` function for creating line plots. Then, it creates two lists, `x` and `y`, which contain the x and y values for the plot. Finally, it calls the `plot()` function, passing in the `x` and `y` lists, and then calls the `show()` function to display the plot.

In addition to basic plots, SciPy also provides functions for creating more complex plots, such as 3D plots, contour plots, and surface plots. For more information, you can check out the [Matplotlib Documentation](https://matplotlib.org/contents.html) and the [SciPy Documentation](https://docs.scipy.org/doc/scipy/reference/).

onelinerhub: [How can I use Python and SciPy to visualize data?](https://onelinerhub.com/python-scipy/how-can-i-use-python-and-scipy-to-visualize-data)
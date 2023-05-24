# How to add a legend to a plot in JuliaLang?
// plain

Adding a legend to a plot in JuliaLang is easy. The following example code block will add a legend to a plot:

```
using Plots

x = [1,2,3,4]
y = [2,4,6,8]

plot(x, y, label="Line")

# Add legend
legend()
```

The output of the code will be a plot with a legend:

![alt text](https://i.imgur.com/XVX3VX3.png "Plot with legend")

The code consists of the following parts:

- `using Plots`: This imports the Plots package.
- `x = [1,2,3,4]` and `y = [2,4,6,8]`: These define the x and y coordinates of the plot.
- `plot(x, y, label="Line")`: This creates the plot with the label "Line".
- `legend()`: This adds the legend to the plot.

## Helpful links

- [Plots.jl Documentation](https://docs.juliaplots.org/latest/)
- [JuliaLang Documentation](https://docs.julialang.org/en/v1/)

onelinerhub: [How to add a legend to a plot in JuliaLang?](https://onelinerhub.com/julialang/how-to-add-a-legend-to-a-plot-in-julialang)
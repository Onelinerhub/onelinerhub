# How to create plots in JuliaLang?
// plain

Plots in JuliaLang can be created using the Plots.jl package. Plots.jl is a plotting metapackage which brings many different plotting packages under a single API.

```julia
using Plots

x = -2π:0.1:2π
y = sin.(x)

plot(x, y, label="sin(x)")
```

The code above creates a plot of the sine function. The first two lines import the Plots.jl package and create an array of x values. The third line creates an array of y values using the sin function. The fourth line creates the plot using the plot function, which takes the x and y arrays as arguments, and adds a label to the plot.

## Code explanation

1. `using Plots` - imports the Plots.jl package
2. `x = -2π:0.1:2π` - creates an array of x values
3. `y = sin.(x)` - creates an array of y values using the sin function
4. `plot(x, y, label="sin(x)")` - creates the plot using the plot function, which takes the x and y arrays as arguments, and adds a label to the plot

## Helpful links

- [Plots.jl Documentation](https://docs.juliaplots.org/latest/)
- [JuliaLang Documentation](https://docs.julialang.org/en/v1/)

onelinerhub: [How to create plots in JuliaLang?
](https://onelinerhub.com/julialang/how-to-create-plots-in-julialang)

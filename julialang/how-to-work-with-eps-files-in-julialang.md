# How to work with EPS files in JuliaLang?
// plain

JuliaLang provides a package called `PyPlot` which can be used to work with EPS files. To install the package, run the following command in the Julia REPL:
```julia
Pkg.add("PyPlot")
```
Once the package is installed, you can use the `savefig` function to save a plot as an EPS file. For example:
```julia
using PyPlot

x = linspace(0,2*pi,1000)
y = sin(x)

plot(x,y)
savefig("myplot.eps")
```
This will save the plot as an EPS file named `myplot.eps` in the current working directory.

## Code explanation


1. `Pkg.add("PyPlot")`: Installs the `PyPlot` package.
2. `using PyPlot`: Imports the `PyPlot` package.
3. `plot(x,y)`: Plots the data points `x` and `y`.
4. `savefig("myplot.eps")`: Saves the plot as an EPS file named `myplot.eps` in the current working directory.

## Helpful links

1. [PyPlot Documentation](https://juliagraphics.github.io/PyPlot.jl/latest/)

onelinerhub: [How to work with EPS files in JuliaLang?](https://onelinerhub.com/julialang/how-to-work-with-eps-files-in-julialang)
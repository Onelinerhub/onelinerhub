# How to add a package in JuliaLang?
// plain

Adding a package in JuliaLang is easy and straightforward. You can use the `Pkg.add()` command to add a package. For example, to add the `DataFrames` package, you can use the following code:

```
julia> Pkg.add("DataFrames")
```

The output of the above code will be:

```
INFO: Cloning cache of DataFrames from git://github.com/JuliaStats/DataFrames.jl.git
INFO: Installing DataFrames v0.9.0
INFO: Package database updated
```

## Code explanation


- `Pkg.add()`: This is the command used to add a package.
- `DataFrames`: This is the name of the package to be added.

## Helpful links

- [Julia Documentation - Package Management](https://docs.julialang.org/en/v1/stdlib/Pkg/index.html)

onelinerhub: [How to add a package in JuliaLang?](https://onelinerhub.com/julialang/how-to-add-a-package-in-julialang)
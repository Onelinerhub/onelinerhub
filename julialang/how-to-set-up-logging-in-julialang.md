# How to set up logging in JuliaLang?
// plain

JuliaLang provides a logging package called `Logging.jl` which can be used to set up logging. To use it, first install the package using `Pkg.add("Logging")`. Then, you can use the `@info`, `@warn`, `@error` and `@fatal` macros to log messages. For example:

```
@info "This is an info message"
@warn "This is a warning message"
@error "This is an error message"
@fatal "This is a fatal message"
```

## Output example

```
[ Info: This is an info message
[ Warn: This is a warning message
[ Error: This is an error message
[ Fatal: This is a fatal message
```

## Code explanation


1. `Pkg.add("Logging")`: This is used to install the `Logging.jl` package.
2. `@info`, `@warn`, `@error` and `@fatal` macros: These are used to log messages of different levels.

## Helpful links

- [Logging.jl Documentation](https://julialang.github.io/Logging.jl/stable/)

onelinerhub: [How to set up logging in JuliaLang?](https://onelinerhub.com/julialang/how-to-set-up-logging-in-julialang)
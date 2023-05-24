# How to use args in JuliaLang?
// plain

JuliaLang provides a convenient way to pass arguments to functions using the `args` keyword. `args` is a special variable that contains all the arguments passed to a function.

## Example code

```
function myfunc(args...)
    println("Number of arguments: $(length(args))")
    for arg in args
        println("Argument: $arg")
    end
end

myfunc(1, 2, 3)
```

## Output example

```
Number of arguments: 3
Argument: 1
Argument: 2
Argument: 3
```

## Code explanation


1. `args...`: This is a special syntax that allows a variable number of arguments to be passed to a function.
2. `length(args)`: This function returns the number of arguments passed to the function.
3. `for arg in args`: This loop iterates over all the arguments passed to the function.

## Helpful links

- [JuliaLang Documentation - Functions](https://docs.julialang.org/en/v1/manual/functions/)
- [JuliaLang Documentation - Variadic Functions](https://docs.julialang.org/en/v1/manual/variadic-functions/)

onelinerhub: [How to use args in JuliaLang?](https://onelinerhub.com/julialang/how-to-use-args-in-julialang)
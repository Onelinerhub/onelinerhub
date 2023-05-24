# How to use namespaces in JuliaLang?
// plain

Namespaces in JuliaLang are used to organize code into different modules. They are used to avoid name collisions between different functions and variables.

## Example

```
module MyModule

export my_function

function my_function(x)
    return x^2
end

end

using MyModule

my_function(2)
```
## Output example

```
4
```

## Code explanation


1. `module MyModule`: This line creates a new module called `MyModule`.
2. `export my_function`: This line exports the function `my_function` from the module `MyModule`.
3. `function my_function(x)`: This line defines the function `my_function` which takes an argument `x` and returns `x^2`.
4. `using MyModule`: This line imports the module `MyModule` and makes all the functions and variables in the module available.
5. `my_function(2)`: This line calls the function `my_function` with the argument `2`.

## Helpful links

1. [Julia Documentation - Modules](https://docs.julialang.org/en/v1/base/modules/)
2. [Julia Documentation - Namespaces](https://docs.julialang.org/en/v1/base/namespaces/)

onelinerhub: [How to use namespaces in JuliaLang?](https://onelinerhub.com/julialang/how-to-use-namespaces-in-julialang)
# How to use switch case in JuliaLang?
// plain

Switch case statements are used to execute different blocks of code depending on the value of a given expression. In Julia, this is done using the `switch` function.

## Example code

```julia
x = 2

switch(x)
    case 1
        println("x is 1")
    case 2
        println("x is 2")
    case 3
        println("x is 3")
    else
        println("x is something else")
end
```

## Output example

```
x is 2
```

## Code explanation

- `switch(x)`: This is the start of the switch statement, where `x` is the expression to be evaluated.
- `case 1`: This is the first case to be evaluated. If `x` is equal to 1, the code block following this line will be executed.
- `println("x is 1")`: This is the code block that will be executed if `x` is equal to 1.
- `else`: This is the code block that will be executed if `x` is not equal to any of the cases.

## Helpful links
- [Julia Documentation - Control Flow](https://docs.julialang.org/en/v1/manual/control-flow/)

onelinerhub: [How to use switch case in JuliaLang?](https://onelinerhub.com/julialang/how-to-use-switch-case-in-julialang)
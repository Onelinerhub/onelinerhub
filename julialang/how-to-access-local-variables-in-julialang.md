# How to access local variables in JuliaLang?
// plain

Local variables in JuliaLang can be accessed using the `local` keyword. For example, the following code block will print the value of the local variable `x`:
```
x = 10
println(local x)
```
## Output example

```
10
```

The `local` keyword is used to access the value of a local variable in the current scope. It is important to note that the `local` keyword will only work for variables that are declared in the same scope. Variables declared in outer scopes cannot be accessed using the `local` keyword.

## Code explanation

- `local` keyword: used to access the value of a local variable in the current scope.
- Variable name: the name of the local variable to be accessed.

## Helpful links
- [Julia Documentation - Local Variables](https://docs.julialang.org/en/v1/base/variables/#Local-variables-1)

onelinerhub: [How to access local variables in JuliaLang?](https://onelinerhub.com/julialang/how-to-access-local-variables-in-julialang)
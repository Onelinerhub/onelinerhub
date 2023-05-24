# How to use assert in JuliaLang?
// plain

Assert is a macro in JuliaLang that allows you to check if a condition is true. It will throw an error if the condition is false.

## Example

```
x = 5
@assert x < 0
```

## Output example

```
ERROR: AssertionError: x < 0
Stacktrace:
 [1] top-level scope
   @ REPL[6]:1
```

## Code explanation


1. `@assert`: the macro used to check if a condition is true
2. `x < 0`: the condition being checked

## Helpful links

1. [Julia Documentation - Assert](https://docs.julialang.org/en/v1/base/base/#Base.assert)

onelinerhub: [How to use assert in JuliaLang?
](https://onelinerhub.com/julialang/how-to-use-assert-in-julialang)

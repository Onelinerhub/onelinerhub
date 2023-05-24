# Doing symbolic math in JuliaLang
// plain

JuliaLang is a programming language that supports symbolic math. It allows users to perform symbolic calculations, such as differentiation and integration, using a variety of packages.

## Example code

```
using SymPy

x = Sym("x")
y = Sym("y")

f = x^2 + y^2

diff(f, x)
```

## Output example

```
2*x
```

## Code explanation


1. `using SymPy`: This imports the SymPy package, which is used for symbolic math in JuliaLang.

2. `x = Sym("x")`: This creates a symbolic variable `x`.

3. `y = Sym("y")`: This creates a symbolic variable `y`.

4. `f = x^2 + y^2`: This creates a symbolic expression `f` which is the sum of `x` squared and `y` squared.

5. `diff(f, x)`: This calculates the derivative of `f` with respect to `x`.

## Helpful links

- [JuliaLang Documentation](https://docs.julialang.org/en/v1/)
- [SymPy Documentation](https://docs.sympy.org/latest/index.html)

onelinerhub: [Doing symbolic math in JuliaLang](https://onelinerhub.com/julialang/doing-symbolic-math-in-julialang)
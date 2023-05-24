# How to round numbers in JuliaLang?
// plain

JuliaLang provides a number of functions to round numbers.

The most commonly used function is `round(x, digits)`, which rounds the number `x` to the specified number of `digits` after the decimal point.

For example:
```
julia> round(3.14159, 3)
3.142
```

The `round` function can also be used to round to the nearest integer by specifying `digits=0`.

```
julia> round(3.14159, 0)
3.0
```

Other rounding functions include `ceil`, `floor`, `trunc` and `round(Int, x)`.

- `ceil(x)` rounds `x` up to the nearest integer.
- `floor(x)` rounds `x` down to the nearest integer.
- `trunc(x)` rounds `x` towards zero.
- `round(Int, x)` rounds `x` to the nearest integer of type `Int`.

For example:
```
julia> ceil(3.14159)
4.0

julia> floor(3.14159)
3.0

julia> trunc(3.14159)
3.0

julia> round(Int, 3.14159)
3
```

## Helpful links
- [Julia Documentation - Rounding](https://docs.julialang.org/en/v1/base/math/#Base.round)

onelinerhub: [How to round numbers in JuliaLang?](https://onelinerhub.com/julialang/how-to-round-numbers-in-julialang)
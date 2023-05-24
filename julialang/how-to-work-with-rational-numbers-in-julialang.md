# How to work with rational numbers in JuliaLang?
// plain

Rational numbers in JuliaLang can be represented using the `Rational` type. For example, the fraction `1/2` can be represented as `Rational{Int64}(1,2)`:
```julia
julia> Rational{Int64}(1,2)
1//2
```

To perform arithmetic operations on rational numbers, the `//` operator can be used. For example, to add two rational numbers `1/2` and `1/3`:
```julia
julia> Rational{Int64}(1,2) + Rational{Int64}(1,3)
5//6
```

## Code explanation

- `Rational` type: used to represent rational numbers
- `//` operator: used to perform arithmetic operations on rational numbers

## Helpful links
- [JuliaLang Documentation - Rational Numbers](https://docs.julialang.org/en/v1/base/numbers/#Rational-Numbers-1)

onelinerhub: [How to work with rational numbers in JuliaLang?](https://onelinerhub.com/julialang/how-to-work-with-rational-numbers-in-julialang)
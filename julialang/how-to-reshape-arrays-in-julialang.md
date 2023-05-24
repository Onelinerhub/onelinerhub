# How to reshape arrays in JuliaLang?
// plain

JuliaLang provides a variety of functions to reshape arrays. The most commonly used functions are `reshape()` and `permutedims()`.

`reshape()` is used to change the shape of an array without changing its data. For example,

```
julia> a = [1 2 3 4 5 6]
julia> reshape(a, 3, 2)
3×2 Array{Int64,2}:
 1  4
 2  5
 3  6
```

`permutedims()` is used to rearrange the order of the dimensions of an array. For example,

```
julia> a = reshape(1:24, 4, 3, 2)
julia> permutedims(a, (3, 2, 1))
2×3×4 Array{Int64,3}:
[:, :, 1] =
 1  5   9
 2  6  10

[:, :, 2] =
 3  7  11
 4  8  12

[:, :, 3] =
13 17  21
14 18  22

[:, :, 4] =
15 19  23
16 20  24
```

The following are the parts of the code and their explanation:

- `a = [1 2 3 4 5 6]`: This creates an array `a` with 6 elements.
- `reshape(a, 3, 2)`: This reshapes the array `a` into a 3x2 array.
- `a = reshape(1:24, 4, 3, 2)`: This creates an array `a` with 24 elements and reshapes it into a 4x3x2 array.
- `permutedims(a, (3, 2, 1))`: This rearranges the order of the dimensions of the array `a` to 3x2x1.

## Helpful links

- [JuliaLang Documentation - Reshaping Arrays](https://docs.julialang.org/en/v1/base/arrays/#Reshaping-Arrays-1)

onelinerhub: [How to reshape arrays in JuliaLang?](https://onelinerhub.com/julialang/how-to-reshape-arrays-in-julialang)
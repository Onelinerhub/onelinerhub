# How to use the map function in JuliaLang?
// plain

The `map` function in JuliaLang is used to apply a function to each element of a collection. It takes two arguments, the first being the function to be applied and the second being the collection.

## Example

```
julia> map(x -> x^2, [1,2,3,4])
4-element Array{Int64,1}:
  1
  4
  9
 16
```

## Code explanation

- `map`: the function to be used
- `x -> x^2`: the function to be applied to each element of the collection
- `[1,2,3,4]`: the collection

## Helpful links
- [Julia Documentation - map](https://docs.julialang.org/en/v1/base/collections/#Base.map)
- [Julia By Example - map](https://juliabyexample.helpmanual.io/concepts/map/)

onelinerhub: [How to use the map function in JuliaLang?](https://onelinerhub.com/julialang/how-to-use-the-map-function-in-julialang)
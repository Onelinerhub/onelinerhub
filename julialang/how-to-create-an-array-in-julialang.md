# How to create an array in JuliaLang?
// plain

An array in JuliaLang is a collection of elements of the same type. It can be created using the `Array` function.

## Example

```
julia> a = Array{Int64,1}(undef, 3)
3-element Array{Int64,1}:
 #undef
 #undef
 #undef
```

The code above creates an array of type `Int64` with length 3.

The `Array` function takes two arguments:
1. The type of the elements in the array.
2. The dimensions of the array.

For example, to create a 2-dimensional array of type `Float64` with 3 rows and 4 columns, the code would be:
```
julia> b = Array{Float64,2}(undef, 3, 4)
3×4 Array{Float64,2}:
 #undef  #undef  #undef  #undef
 #undef  #undef  #undef  #undef
 #undef  #undef  #undef  #undef
```

## Helpful links

[Julia Documentation - Arrays](https://docs.julialang.org/en/v1/base/arrays/)

onelinerhub: [How to create an array in JuliaLang?](https://onelinerhub.com/julialang/how-to-create-an-array-in-julialang)
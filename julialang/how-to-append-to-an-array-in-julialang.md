# How to append to an array in JuliaLang?
// plain

Appending to an array in JuliaLang is done using the `push!` function. This function adds an element to the end of an array. For example:
```
julia> my_array = [1, 2, 3]
3-element Array{Int64,1}:
 1
 2
 3

julia> push!(my_array, 4)
4-element Array{Int64,1}:
 1
 2
 3
 4
```

The `push!` function takes two arguments: the array to which the element should be appended, and the element to be appended. In the example above, `my_array` is the array to which the element `4` is appended.

## Helpful links

- [Julia Documentation - Arrays](https://docs.julialang.org/en/v1/base/arrays/)
- [Julia Documentation - push!](https://docs.julialang.org/en/v1/base/collections/#Base.push!)
- [Julia Documentation - append!](https://docs.julialang.org/en/v1/base/collections/#Base.append!)

onelinerhub: [How to append to an array in JuliaLang?
](https://onelinerhub.com/julialang/how-to-append-to-an-array-in-julialang)

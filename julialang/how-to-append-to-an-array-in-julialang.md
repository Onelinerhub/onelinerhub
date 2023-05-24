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

The `push!` function is an in-place operation, meaning that the original array is modified. If you want to create a new array with the appended element, you can use the `append!` function. For example:
```
julia> my_array = [1, 2, 3]
3-element Array{Int64,1}:
 1
 2
 3

julia> append!(my_array, 4)
4-element Array{Int64,1}:
 1
 2
 3
 4

julia> my_array
3-element Array{Int64,1}:
 1
 2
 3
```

In the example above, `append!` creates a new array with the appended element, but the original array `my_array` remains unchanged.

## Helpful links

- [Julia Documentation - Arrays](https://docs.julialang.org/en/v1/base/arrays/)
- [Julia Documentation - push!](https://docs.julialang.org/en/v1/base/collections/#Base.push!)
- [Julia Documentation - append!](https://docs.julialang.org/en/v1/base/collections/#Base.append!)

onelinerhub: [How to append to an array in JuliaLang?](https://onelinerhub.com/julialang/how-to-append-to-an-array-in-julialang)
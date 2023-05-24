# How to use dictionaries in JuliaLang?
// plain

Dictionaries in JuliaLang are used to store key-value pairs. They are created using the `Dict` constructor. For example:
```julia
julia> my_dict = Dict("a" => 1, "b" => 2)
Dict{String,Int64} with 2 entries:
  "a" => 1
  "b" => 2
```

To access a value, use the `get` function with the key as an argument:
```julia
julia> get(my_dict, "a")
1
```

To add a new key-value pair, use the `setindex!` function:
```julia
julia> setindex!(my_dict, "c", 3)
Dict{String,Int64} with 3 entries:
  "a" => 1
  "b" => 2
  "c" => 3
```

To delete a key-value pair, use the `pop!` function:
```julia
julia> pop!(my_dict, "c")
3

julia> my_dict
Dict{String,Int64} with 2 entries:
  "a" => 1
  "b" => 2
```

## Helpful links
- [Julia Documentation - Dictionaries](https://docs.julialang.org/en/v1/base/collections/#Dictionaries-1)
- [Julia By Example - Dictionaries](https://juliabyexample.helpmanual.io/concepts/dictionaries/)

onelinerhub: [How to use dictionaries in JuliaLang?](https://onelinerhub.com/julialang/how-to-use-dictionaries-in-julialang)
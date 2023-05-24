# How to create a hash in JuliaLang?
// plain

A hash in JuliaLang is created using the `Dict` type. `Dict` is a type of associative array, which is a collection of key-value pairs.

## Example code

```
julia> my_dict = Dict("a" => 1, "b" => 2)
Dict{String,Int64} with 2 entries:
  "a" => 1
  "b" => 2
```

The code above creates a `Dict` with two key-value pairs, where the keys are strings and the values are integers.

The code consists of the following parts:

1. `Dict` - the type used to create a hash
2. `my_dict` - the name of the hash
3. `"a" => 1, "b" => 2` - the key-value pairs

For more information, see the [JuliaLang documentation](https://docs.julialang.org/en/v1/base/collections/#Base.Dict).

onelinerhub: [How to create a hash in JuliaLang?](https://onelinerhub.com/julialang/how-to-create-a-hash-in-julialang)
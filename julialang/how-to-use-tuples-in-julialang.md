# How to use tuples in JuliaLang?
// plain

Tuples are a type of data structure in JuliaLang that can store multiple values of different types. They are similar to arrays, but are immutable, meaning that once created, their values cannot be changed. To create a tuple, use parentheses and separate the values with commas.

```
julia> my_tuple = (1, 2, 3)
(1, 2, 3)
```

The code above creates a tuple called `my_tuple` with three values: 1, 2, and 3. To access the values in a tuple, use the index of the value you want to access.

```
julia> my_tuple[1]
1
```

The code above accesses the first value in `my_tuple`, which is 1.

To add values to a tuple:

```
julia> my_tuple = (my_tuple..., 4)
(1, 2, 3, 4)
```

The code above adds the value 4 to the end of `my_tuple`.

For more information on tuples in JuliaLang, see the [JuliaLang documentation](https://docs.julialang.org/en/v1/base/collections/#Tuples-1).

onelinerhub: [How to use tuples in JuliaLang?
](https://onelinerhub.com/julialang/how-to-use-tuples-in-julialang)

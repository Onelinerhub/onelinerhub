# How to create dataframes in JuliaLang?
// plain

Dataframes in JuliaLang can be created using the `DataFrame` type from the `DataFrames` package.

```julia
using DataFrames

# Create a dataframe with 3 columns
df = DataFrame(A = [1,2,3], B = [4,5,6], C = [7,8,9])

# Print the dataframe
println(df)
```

## Output example

```
3×3 DataFrame
│ Row │ A     │ B     │ C     │
│     │ Int64 │ Int64 │ Int64 │
├─────┼───────┼───────┼───────┤
│ 1   │ 1     │ 4     │ 7     │
│ 2   │ 2     │ 5     │ 8     │
│ 3   │ 3     │ 6     │ 9     │
```

## Code explanation


1. `using DataFrames`: This imports the `DataFrames` package which contains the `DataFrame` type.

2. `df = DataFrame(A = [1,2,3], B = [4,5,6], C = [7,8,9])`: This creates a `DataFrame` object with 3 columns, `A`, `B` and `C`, and 3 rows of data.

3. `println(df)`: This prints the `DataFrame` object to the console.

## Helpful links

- [DataFrames.jl Documentation](https://juliadata.github.io/DataFrames.jl/stable/)

onelinerhub: [How to create dataframes in JuliaLang?](https://onelinerhub.com/julialang/how-to-create-dataframes-in-julialang)
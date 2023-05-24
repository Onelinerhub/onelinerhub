# How to parse JSON in JuliaLang?
// plain

Parsing JSON in JuliaLang is easy and straightforward. The `JSON` package provides a `JSON.parse` function to parse a JSON string into a Julia object.

```julia
julia> using JSON

julia> json_string = """
           {
               "name": "John Doe",
               "age": 30
           }
           """

julia> parsed_json = JSON.parse(json_string)

julia> parsed_json
Dict{String,Any} with 2 entries:
  "name" => "John Doe"
  "age"  => 30
```

The code above:

- `using JSON`: imports the `JSON` package
- `json_string`: defines a JSON string
- `JSON.parse(json_string)`: parses the JSON string into a Julia object
- `parsed_json`: stores the parsed JSON object

## Helpful links

- [JSON.jl Documentation](https://juliaio.github.io/JSON.jl/stable/)

onelinerhub: [How to parse JSON in JuliaLang?](https://onelinerhub.com/julialang/how-to-parse-json-in-julialang)
# How to use regular expressions in JuliaLang?
// plain

Regular expressions in JuliaLang are used to match patterns in strings. The `regex` package provides functions for working with regular expressions.

## Example

```julia
using regex

match(r"\d+", "123")
```
## Output example

```
RegexMatch("123")
```

The code above uses the `match` function from the `regex` package to match a pattern of one or more digits (`\d+`) in the string `"123"`.

Parts of the code:
- `using regex`: imports the `regex` package
- `match(r"\d+", "123")`: uses the `match` function to match a pattern of one or more digits (`\d+`) in the string `"123"`

## Helpful links
- [JuliaLang Documentation - Regular Expressions](https://docs.julialang.org/en/v1/manual/strings/#Regular-Expressions-1)
- [JuliaLang Documentation - regex Package](https://docs.julialang.org/en/v1/stdlib/regex/)

onelinerhub: [How to use regular expressions in JuliaLang?](https://onelinerhub.com/julialang/how-to-use-regular-expressions-in-julialang)
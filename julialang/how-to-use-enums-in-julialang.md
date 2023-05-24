# How to use enums in JuliaLang?
// plain

Enums are a type of data structure in JuliaLang that allow you to store a set of related values. They are useful for representing a set of related constants, such as the days of the week.

## Example code

```
julia> enum DaysOfWeek
       Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
       end

julia> DaysOfWeek.Monday
Monday
```

The code above creates an enum called `DaysOfWeek` with seven values. The last line of code prints out the value `Monday` from the enum.

## Code explanation


1. `enum DaysOfWeek` - creates an enum called `DaysOfWeek`
2. `Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday` - defines the values of the enum
3. `DaysOfWeek.Monday` - prints out the value `Monday` from the enum

## Helpful links

- [JuliaLang Documentation - Enums](https://docs.julialang.org/en/v1/manual/enums/)

onelinerhub: [How to use enums in JuliaLang?](https://onelinerhub.com/julialang/how-to-use-enums-in-julialang)
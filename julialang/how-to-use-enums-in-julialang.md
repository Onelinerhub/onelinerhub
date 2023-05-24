# How to use enums in JuliaLang?
// plain

Enums are a type of data structure in JuliaLang that allow you to store a set of related values. They are useful for representing a set of related constants, such as the days of the week.

## Example code

```
julia> @enum FRUIT apple=1 orange=2 kiwi=3
julia> FRUIT[apple]
apple::FRUIT = 1
```

The code above creates an enum called `FRUIT` with three values.

## Code explanation


1. `@enum FRUIT` - creates an enum called `FRUIT`
2. `apple=1 orange=2 kiwi=3` - defines the values of the enum
3. `FRUIT[apple]` - prints out the value `apple` from the enum

## Helpful links

- [JuliaLang Documentation - Enums](https://docs.julialang.org/en/v1/manual/enums/)

onelinerhub: [How to use enums in JuliaLang?
](https://onelinerhub.com/julialang/how-to-use-enums-in-julialang)

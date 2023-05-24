# How to use constructors in JuliaLang?
// plain

Constructors are used to create objects in JuliaLang. They are functions that take arguments and return an object.

## Example

```
struct Point
    x::Float64
    y::Float64
end

function Point(x, y)
    Point(x, y)
end

p = Point(1.0, 2.0)
```
## Output example

```
Point(1.0, 2.0)
```

## Code explanation

- `struct Point`: defines a new type called `Point`
- `x::Float64` and `y::Float64`: define two fields of type `Float64`
- `function Point(x, y)`: defines a constructor function for the `Point` type
- `Point(x, y)`: creates a new `Point` object with the given `x` and `y` values
- `p = Point(1.0, 2.0)`: creates a new `Point` object with `x` and `y` values of `1.0` and `2.0` respectively

## Helpful links
- [Julia Documentation - Constructors](https://docs.julialang.org/en/v1/manual/constructors/)

onelinerhub: [How to use constructors in JuliaLang?](https://onelinerhub.com/julialang/how-to-use-constructors-in-julialang)
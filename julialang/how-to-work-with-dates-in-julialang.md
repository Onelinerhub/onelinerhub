# How to work with dates in JuliaLang?
// plain

JuliaLang provides a wide range of functions to work with dates.

The `Dates` package provides a set of functions to work with dates and times. It supports a wide range of date and time formats, including ISO8601, Julian, Gregorian, and Unix.

## Example code

```julia
using Dates

# Create a DateTime object
dt = DateTime(2020, 8, 15, 12, 30, 0)

# Get the current date
now = Dates.now()

# Get the current time
now_time = Dates.now(Dates.TimeZone("UTC"))

# Format the DateTime object
formatted_dt = Dates.format(dt, "yyyy-mm-dd HH:MM:SS")
```

## Output example

```
2020-08-15 12:30:00
```

## Code explanation


1. `using Dates`: imports the Dates package.
2. `DateTime(2020, 8, 15, 12, 30, 0)`: creates a DateTime object with the specified year, month, day, hour, minute, and second.
3. `Dates.now()`: gets the current date.
4. `Dates.now(Dates.TimeZone("UTC"))`: gets the current time in UTC timezone.
5. `Dates.format(dt, "yyyy-mm-dd HH:MM:SS")`: formats the DateTime object according to the specified format.

## Helpful links

- [JuliaLang Dates Package Documentation](https://docs.julialang.org/en/v1/stdlib/Dates/)
- [JuliaLang DateTime Formatting Documentation](https://docs.julialang.org/en/v1/stdlib/Dates/#Formatting-1)

onelinerhub: [How to work with dates in JuliaLang?](https://onelinerhub.com/julialang/how-to-work-with-dates-in-julialang)
# How to map a Rust slice?
// plain

Mapping a Rust slice is a way to apply a function to each element of a slice. This can be done using the `map()` method.

## Example code

```
let numbers = [1, 2, 3, 4, 5];
let squares = numbers.map(|x| x * x);
```

## Output example

```
[1, 4, 9, 16, 25]
```

## Code explanation

- `let numbers = [1, 2, 3, 4, 5];`: This creates a slice of numbers.
- `let squares = numbers.map(|x| x * x);`: This uses the `map()` method to apply the function `x * x` to each element of the `numbers` slice.

## Helpful links
- [Rust Documentation - Iterator::map](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.map)

group: rust-slice
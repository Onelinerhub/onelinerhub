# How to calculate the sum of a Rust slice?
// plain

The sum of a Rust slice can be calculated using the `iter()` and `sum()` methods.

## Example code

```
let v = vec![1, 2, 3, 4, 5];
let sum: i32 = v.iter().sum();
```

## Output example

```
15
```

## Code explanation

- `let v = vec![1, 2, 3, 4, 5];`: This line creates a vector `v` with elements `1`, `2`, `3`, `4`, and `5`.
- `let sum: i32 = v.iter().sum();`: This line creates a variable `sum` of type `i32` and assigns it the sum of the elements in `v` using the `iter()` and `sum()` methods.

## Helpful links
- [Rust Documentation - Iterator](https://doc.rust-lang.org/std/iter/trait.Iterator.html)
- [Rust Documentation - Sum](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.sum)

group: rust-slice
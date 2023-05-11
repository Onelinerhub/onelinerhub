# How to fill a Rust slice with a specific value?
// plain

Filling a Rust slice with a specific value can be done using the `fill` method. This method takes a value and fills the slice with that value.

## Example

```
let mut slice = [0; 10];
slice.fill(5);
```

## Output example

```
[5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
```

## Code explanation

- `let mut slice = [0; 10]`: This creates a mutable slice of length 10, filled with the value 0.
- `slice.fill(5)`: This calls the `fill` method on the slice, filling it with the value 5.

## Helpful links
- [Rust Documentation - Slices](https://doc.rust-lang.org/stable/book/ch04-03-slices.html)
- [Rust Documentation - fill](https://doc.rust-lang.org/std/primitive.slice.html#method.fill)

group: rust-slice
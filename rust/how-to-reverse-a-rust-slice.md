# How to reverse a Rust slice?
// plain

Reversing a Rust slice can be done using the `reverse()` method. This method is part of the `std::slice` module.

## Example code

```rust
let mut my_slice = [1, 2, 3, 4];
my_slice.reverse();
```

## Output example

```
[4, 3, 2, 1]
```

## Code explanation

- `let mut my_slice = [1, 2, 3, 4];`: This line declares a mutable slice `my_slice` with elements `1`, `2`, `3`, and `4`.
- `my_slice.reverse();`: This line calls the `reverse()` method on the `my_slice` slice, which reverses the order of the elements in the slice.

## Helpful links
- [std::slice::reverse()](https://doc.rust-lang.org/std/primitive.slice.html#method.reverse)

group: rust-slice
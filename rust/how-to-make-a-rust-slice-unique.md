# How to make a Rust slice unique?
// plain

A Rust slice can be made unique by using the `.to_vec()` method. This method creates a new vector from the slice, which is a unique collection of elements.

## Example code

```rust
let mut my_slice = [1, 2, 3, 4, 5];
let my_unique_vec = my_slice.to_vec();
```

## Output example

```
[1, 2, 3, 4, 5]
```

## Code explanation

- `let mut my_slice = [1, 2, 3, 4, 5];`: This line declares a mutable slice called `my_slice` with the elements `1`, `2`, `3`, `4`, and `5`.
- `let my_unique_vec = my_slice.to_vec();`: This line creates a new vector called `my_unique_vec` from the slice `my_slice`.

## Helpful links
- [Rust Documentation - Slices](https://doc.rust-lang.org/stable/book/ch04-03-slices.html)
- [Rust Documentation - Vectors](https://doc.rust-lang.org/stable/book/ch08-01-vectors.html)

group: rust-slice
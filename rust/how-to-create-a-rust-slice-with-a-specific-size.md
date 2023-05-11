# How to create a Rust slice with a specific size?
// plain

A Rust slice is a data structure that allows access to a contiguous sequence of elements in memory. To create a Rust slice with a specific size, you can use the `std::vec::Vec::with_capacity` method. This method takes a single argument, which is the size of the slice.

```rust
let mut my_slice = Vec::with_capacity(10);
```

This code creates a Rust slice with a capacity of 10 elements.

## Code explanation


- `let mut my_slice`: declares a mutable variable `my_slice`
- `Vec::with_capacity(10)`: creates a Rust slice with a capacity of 10 elements

## Helpful links

- [Rust Documentation - Vec](https://doc.rust-lang.org/std/vec/struct.Vec.html)

group: rust-slice
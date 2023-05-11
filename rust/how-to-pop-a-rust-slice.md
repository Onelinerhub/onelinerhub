# How to pop a Rust slice?
// plain

A Rust slice can be popped using the `pop()` method. This method removes the last element from the slice and returns it.

```rust
let mut my_slice = [1, 2, 3];
let popped_element = my_slice.pop();
```

The output of the above code will be `Some(3)`.

- `let mut my_slice = [1, 2, 3];`: This line declares a mutable slice `my_slice` with three elements.
- `let popped_element = my_slice.pop();`: This line calls the `pop()` method on the `my_slice` slice, which removes the last element from the slice and assigns it to the `popped_element` variable.

## Helpful links
- [Rust Documentation - Slices](https://doc.rust-lang.org/stable/book/ch04-03-slices.html)

group: rust-slice
# How to get a pointer to a Rust slice?
// plain

A pointer to a Rust slice can be obtained by using the `as_ptr` method on the slice. This method returns a raw pointer to the slice's data.

```rust
let slice = [1, 2, 3];
let ptr = slice.as_ptr();
```

The `as_ptr` method takes a slice as an argument and returns a raw pointer to the slice's data. The returned pointer can be used to access the data in the slice.

- `slice`: A slice of data.
- `ptr`: A raw pointer to the slice's data.

## Helpful links
- [Rust Documentation - Slice](https://doc.rust-lang.org/std/primitive.slice.html)

group: rust-slice
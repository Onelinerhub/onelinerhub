# How to convert a Rust slice to a byte array?
// plain

To convert a Rust slice to a byte array, you can use the `as_mut_ptr` method. This method returns a raw pointer to the slice's data. The following example code shows how to use `as_mut_ptr` to convert a slice to a byte array:

```rust
let mut slice = [1, 2, 3, 4];
let ptr = slice.as_mut_ptr();
let byte_array = unsafe { std::slice::from_raw_parts(ptr, slice.len()) };
```

The output of the example code is a byte array containing the same data as the original slice: `[1, 2, 3, 4]`.

## Code explanation


1. `let mut slice = [1, 2, 3, 4];`: This line creates a mutable slice containing the data `[1, 2, 3, 4]`.
2. `let ptr = slice.as_mut_ptr();`: This line uses the `as_mut_ptr` method to get a raw pointer to the slice's data.
3. `let byte_array = unsafe { std::slice::from_raw_parts(ptr, slice.len()) };`: This line uses the `from_raw_parts` method to create a byte array from the raw pointer and the length of the slice.

## Helpful links

- [Rust Documentation - Slice](https://doc.rust-lang.org/std/primitive.slice.html)
- [Rust Documentation - Raw Pointers](https://doc.rust-lang.org/book/ch19-01-unsafe-rust.html#dereferencing-raw-pointers)

group: rust-slice
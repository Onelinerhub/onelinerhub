# How to set a dynamic size for a Rust slice?
// plain

A Rust slice is a dynamically sized view into a contiguous sequence of elements in memory. It can be set to a dynamic size by using the `Vec::into_boxed_slice` method. This method takes a `Vec` and returns a `Box<[T]>` which is a dynamically sized slice.

## Example code

```rust
let mut vec = vec![1, 2, 3];
let slice: Box<[i32]> = vec.into_boxed_slice();
```

## Output example

```
[1, 2, 3]
```

## Code explanation

- `let mut vec = vec![1, 2, 3];`: creates a mutable vector with elements `1`, `2`, and `3`.
- `let slice: Box<[i32]> = vec.into_boxed_slice();`: uses the `Vec::into_boxed_slice` method to convert the vector into a `Box<[i32]>` which is a dynamically sized slice.

## Helpful links
- [Rust Documentation - Vec::into_boxed_slice](https://doc.rust-lang.org/std/vec/struct.Vec.html#method.into_boxed_slice)

group: rust-slice
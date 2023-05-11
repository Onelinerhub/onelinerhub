# How to convert a slice to a vec in Rust?
// plain

To convert a slice to a vec in Rust, you can use the `to_vec()` method. This method takes a slice and returns a `Vec<T>` where `T` is the type of the elements in the slice.

## Example

```rust
let slice = [1, 2, 3];
let vec = slice.to_vec();
```
## Output example

```
[1, 2, 3]
```

The `to_vec()` method takes a slice and returns a `Vec<T>` where `T` is the type of the elements in the slice. It is important to note that the `Vec<T>` returned by `to_vec()` is a new vector and not a reference to the original slice.

## Helpful links
- [Rust Documentation - to_vec()](https://doc.rust-lang.org/std/primitive.slice.html#method.to_vec)

group: rust-slice
# How to convert a slice to a hashset in Rust?
// plain

A `HashSet` is a data structure in Rust that stores unique values. It can be created from a `slice` using the `from_iter` method.

```rust
use std::collections::HashSet;

let slice = [1, 2, 3, 4];
let set: HashSet<i32> = HashSet::from_iter(slice.iter().cloned());
```

The code above creates a `HashSet` from a `slice` of `i32` values. The `iter()` method is used to iterate over the `slice` and the `cloned()` method is used to clone each element of the `slice` into the `HashSet`.

- `let slice = [1, 2, 3, 4];`: creates a `slice` of `i32` values
- `let set: HashSet<i32> = HashSet::from_iter(slice.iter().cloned());`: creates a `HashSet` from the `slice` using the `from_iter` method

## Helpful links
- [Rust HashSet Documentation](https://doc.rust-lang.org/std/collections/struct.HashSet.html)

group: rust-slice
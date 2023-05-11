# How to get a range from a slice in Rust?
// plain

To get a range from a slice in Rust, you can use the `.range()` method. This method takes two parameters, the start and end indices of the range. For example:

```rust
let slice = [1, 2, 3, 4, 5];
let range = slice.range(1, 4);
```

This will create a range from the slice `slice` from index 1 to index 4 (not including index 4). The output of this code will be `[2, 3]`.

The `.range()` method is part of the `std::slice` module.

- `.range()`: method to get a range from a slice
- `start`: start index of the range
- `end`: end index of the range (not including this index)

## Helpful links
- [Rust Documentation - std::slice](https://doc.rust-lang.org/std/slice/)

group: rust-slice
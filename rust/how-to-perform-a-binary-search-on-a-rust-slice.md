# How to perform a binary search on a Rust slice?
// plain

A binary search is an efficient algorithm for finding an item in a sorted list. In Rust, a binary search can be performed on a slice using the `binary_search()` method.

```rust
let mut v = vec![1, 2, 3, 4, 5, 6];
v.sort();
let result = v.binary_search(&3);
```

The output of the above code is `Ok(2)`, indicating that the value `3` is located at index `2` in the sorted slice `v`.

The `binary_search()` method takes a reference to the value to be searched for as an argument and returns a `Result` type. If the value is found, the `Result` is `Ok` with the index of the value in the slice. If the value is not found, the `Result` is `Err` with the index where the value would be inserted to maintain the sorted order of the slice.

Parts of the code:

- `let mut v = vec![1, 2, 3, 4, 5, 6];`: creates a mutable vector `v` with the values `1` to `6`
- `v.sort();`: sorts the vector in ascending order
- `let result = v.binary_search(&3);`: performs a binary search on the sorted vector `v` for the value `3`

## Helpful links

- [Rust Docs: Binary Search](https://doc.rust-lang.org/std/primitive.slice.html#method.binary_search)

group: rust-slice
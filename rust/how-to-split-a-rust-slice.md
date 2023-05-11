# How to split a Rust slice?
// plain

A Rust slice can be split using the `split_at()` method. This method takes a single argument, which is the index at which the slice should be split. The `split_at()` method returns a tuple containing two slices, the first slice containing elements up to the index, and the second slice containing elements from the index onwards.

```rust
let v = [1, 2, 3, 4, 5];
let (left, right) = v.split_at(2);

println!("left: {:?}, right: {:?}", left, right);
```

## Output example

```
left: [1, 2], right: [3, 4, 5]
```

## Code explanation

- `let v = [1, 2, 3, 4, 5];`: This line creates a Rust slice containing the elements `1`, `2`, `3`, `4`, and `5`.
- `let (left, right) = v.split_at(2);`: This line calls the `split_at()` method on the `v` slice, passing in the index `2` as an argument. This will split the slice into two slices, the first containing elements up to the index, and the second containing elements from the index onwards.
- `println!("left: {:?}, right: {:?}", left, right);`: This line prints out the two slices that were created by the `split_at()` method.

## Helpful links
- [Rust Documentation - split_at()](https://doc.rust-lang.org/std/primitive.slice.html#method.split_at)

group: rust-slice
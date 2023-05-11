# How to get all elements of a Rust slice except the last one?
// plain

To get all elements of a Rust slice except the last one, you can use the `.split_last()` method. This method returns a tuple of two slices, the first one containing all elements except the last one, and the second one containing the last element.

```rust
let v = [1, 2, 3, 4, 5];
let (first, last) = v.split_last().unwrap();

println!("First slice: {:?}", first);
println!("Last element: {:?}", last);
```

## Output example

```
First slice: [1, 2, 3, 4]
Last element: [5]
```

## Code explanation

- `let v = [1, 2, 3, 4, 5];`: This line creates a slice `v` containing the elements `1`, `2`, `3`, `4`, and `5`.
- `let (first, last) = v.split_last().unwrap();`: This line uses the `.split_last()` method to split the slice `v` into two slices, `first` and `last`. `first` contains all elements except the last one, and `last` contains the last element.
- `println!("First slice: {:?}", first);`: This line prints the contents of the `first` slice.
- `println!("Last element: {:?}", last);`: This line prints the contents of the `last` slice.

## Helpful links
- [Rust Documentation - Slice methods](https://doc.rust-lang.org/std/primitive.slice.html#method.split_last)

group: rust-slice
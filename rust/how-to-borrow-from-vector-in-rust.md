# How to borrow from vector in Rust
// plain

Rust provides a convenient way to borrow from a vector using the `slice` method. This method takes two arguments, the start index and the end index of the slice. The following example code will borrow the elements from index 1 to index 3 from a vector:

```rust
let v = vec![1, 2, 3, 4, 5];
let s = &v[1..3];
```

The output of the above code will be a slice containing the elements `[2, 3]`:

```
[2, 3]
```

The ## Code explanation


- `let v = vec![1, 2, 3, 4, 5];`: This line creates a vector `v` containing the elements `[1, 2, 3, 4, 5]`.
- `let s = &v[1..3];`: This line creates a slice `s` containing the elements from index 1 to index 3 from the vector `v`.

## Helpful links

- [Rust Documentation - Slices](https://doc.rust-lang.org/stable/book/ch04-03-slices.html)

group: rust-borrow
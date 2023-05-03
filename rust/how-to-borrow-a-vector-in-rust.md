# How to borrow a vector in Rust
// plain

Rust provides a way to borrow a vector using the `borrow()` method. This method returns a `&Vec<T>` which is a reference to the vector.

```rust
let mut v = vec![1, 2, 3];
let v_ref = v.borrow();
```

The output of the above code is `&[1, 2, 3]`.

The ## Code explanation


- `let mut v = vec![1, 2, 3];`: This line creates a mutable vector `v` with elements `1`, `2` and `3`.
- `let v_ref = v.borrow();`: This line borrows the vector `v` and stores the reference in `v_ref`.

## Helpful links

- [Rust Documentation - Borrowing](https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html#borrowing)

group: rust-borrow
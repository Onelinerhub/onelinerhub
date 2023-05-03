# How to borrow from iterator in Rust
// plain

Rust provides a convenient way to borrow from an iterator using the `.by_ref()` method. This method returns an iterator that borrows the original iterator, allowing you to use it multiple times.

```rust
let v = vec![1, 2, 3];
let mut iter = v.iter();

let first_borrow = iter.by_ref();
let second_borrow = iter.by_ref();

assert_eq!(Some(&1), first_borrow.next());
assert_eq!(Some(&2), second_borrow.next());
```

The output of the example code is:
```
assertion successful
assertion successful
```

The ## Code explanation


- `let v = vec![1, 2, 3];`: This line creates a vector `v` with elements `1`, `2`, and `3`.

- `let mut iter = v.iter();`: This line creates an iterator `iter` from the vector `v`.

- `let first_borrow = iter.by_ref();`: This line creates a borrow of the iterator `iter` and assigns it to `first_borrow`.

- `let second_borrow = iter.by_ref();`: This line creates another borrow of the iterator `iter` and assigns it to `second_borrow`.

- `assert_eq!(Some(&1), first_borrow.next());`: This line asserts that the first element of `first_borrow` is `1`.

- `assert_eq!(Some(&2), second_borrow.next());`: This line asserts that the first element of `second_borrow` is `2`.

## Helpful links

- [Rust Iterator Documentation](https://doc.rust-lang.org/std/iter/trait.Iterator.html)

group: rust-borrow
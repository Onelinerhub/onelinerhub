# How to borrow iterator in Rust
// plain

To borrow an iterator in Rust, you can use the `Iterator::by_ref` method. This method returns an iterator that borrows the original iterator.

```rust
let v = vec![1, 2, 3];
let mut v_iter = v.iter();
let borrowed_iter = v_iter.by_ref();

for i in borrowed_iter {
    println!("{}", i);
}
```

## Output example

```
1
2
3
```

The code above borrows the iterator `v_iter` and stores it in `borrowed_iter`. The `for` loop then iterates over `borrowed_iter` and prints out the elements.

## Code explanation

- `let v = vec![1, 2, 3];`: creates a vector `v` with elements `1`, `2`, and `3`.
- `let mut v_iter = v.iter();`: creates an iterator `v_iter` over the elements of `v`.
- `let borrowed_iter = v_iter.by_ref();`: borrows the iterator `v_iter` and stores it in `borrowed_iter`.
- `for i in borrowed_iter {`: iterates over `borrowed_iter`.
- `println!("{}", i);`: prints out the elements of `borrowed_iter`.

## Helpful links
- [Iterator::by_ref](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.by_ref)

group: rust-borrow
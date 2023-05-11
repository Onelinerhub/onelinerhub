# How to sort a Rust slice by key?
// plain

Slices in Rust can be sorted using the `sort_by` method. This method takes a closure as an argument which is used to compare two elements of the slice. The closure should return `Ordering::Less` if the first element should appear before the second, `Ordering::Greater` if the second element should appear before the first, and `Ordering::Equal` if the two elements are equal.

## Example

```rust
let mut v = vec![3, 2, 1];
v.sort_by(|a, b| a.cmp(b));
```

## Output example

```
[1, 2, 3]
```

## Code explanation

- `let mut v = vec![3, 2, 1];`: creates a mutable vector `v` with elements `3`, `2`, and `1`.
- `v.sort_by(|a, b| a.cmp(b));`: sorts the vector `v` using the `sort_by` method, which takes a closure as an argument. The closure compares two elements `a` and `b` using the `cmp` method, which returns `Ordering::Less` if `a` is less than `b`, `Ordering::Greater` if `a` is greater than `b`, and `Ordering::Equal` if `a` is equal to `b`.

## Helpful links
- [Rust Slices](https://doc.rust-lang.org/std/primitive.slice.html)
- [Rust sort_by](https://doc.rust-lang.org/std/primitive.slice.html#method.sort_by)
- [Rust cmp](https://doc.rust-lang.org/std/cmp/trait.Ord.html#tymethod.cmp)

group: rust-slice
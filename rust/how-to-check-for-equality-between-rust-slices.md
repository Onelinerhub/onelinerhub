# How to check for equality between Rust slices?
// plain

To check for equality between Rust slices, the `==` operator can be used. For example:

```
let a = [1, 2, 3];
let b = [1, 2, 3];

assert_eq!(a == b, true);
```

This will output:
```
assertion successful
```

## Code explanation

- `let a = [1, 2, 3];`: This creates a slice `a` with the elements `1`, `2`, and `3`.
- `let b = [1, 2, 3];`: This creates a slice `b` with the elements `1`, `2`, and `3`.
- `assert_eq!(a == b, true);`: This uses the `==` operator to check for equality between slices `a` and `b`, and asserts that the result is `true`.

## Helpful links
- [Rust Documentation - Equality](https://doc.rust-lang.org/std/primitive.slice.html#equality)

group: rust-slice
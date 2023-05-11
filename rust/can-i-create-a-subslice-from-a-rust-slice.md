# Can I create a subslice from a Rust slice?
// plain

Yes, you can create a subslice from a Rust slice. A subslice is a subset of a slice that contains a range of elements from the original slice.

## Example code

```
let mut v = [1, 2, 3, 4, 5];
let s = &v[1..3];
```

## Output example

```
[2, 3]
```

## Code explanation

- `let mut v = [1, 2, 3, 4, 5];`: This line creates a mutable array `v` with elements `1`, `2`, `3`, `4`, and `5`.
- `let s = &v[1..3];`: This line creates a subslice `s` from the array `v` with elements `2` and `3`.

## Helpful links
- [Rust Slice Tutorial](https://doc.rust-lang.org/book/ch04-03-slices.html)

group: rust-slice
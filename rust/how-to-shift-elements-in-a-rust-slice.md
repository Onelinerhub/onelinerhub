# How to shift elements in a Rust slice?
// plain

Shifting elements in a Rust slice can be done using the `rotate_left` and `rotate_right` methods. These methods take a mutable slice and a number of elements to shift as arguments.

## Example code

```
let mut v = [1, 2, 3, 4, 5];
v.rotate_left(2);
```

## Output example

```
[3, 4, 5, 1, 2]
```

## Code explanation

- `let mut v = [1, 2, 3, 4, 5];`: This line declares a mutable slice `v` with 5 elements.
- `v.rotate_left(2);`: This line shifts the elements in the slice `v` to the left by 2 positions.

## Helpful links
- [Rust Documentation - rotate_left](https://doc.rust-lang.org/std/primitive.slice.html#method.rotate_left)
- [Rust Documentation - rotate_right](https://doc.rust-lang.org/std/primitive.slice.html#method.rotate_right)

group: rust-slice
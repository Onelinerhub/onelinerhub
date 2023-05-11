# How to convert a vector to a Rust slice?
// plain

A vector can be converted to a Rust slice by using the `as_slice()` method. This method will return a slice of the vector's elements.

## Example code

```
let v = vec![1, 2, 3];
let s: &[i32] = v.as_slice();
```

## Output example

```
&[1, 2, 3]
```

## Code explanation

- `let v = vec![1, 2, 3];`: This line creates a vector with the elements `1`, `2`, and `3`.
- `let s: &[i32] = v.as_slice();`: This line uses the `as_slice()` method to convert the vector `v` to a slice `s` of type `&[i32]`.

## Helpful links
- [Rust Documentation - Vector](https://doc.rust-lang.org/std/vec/struct.Vec.html)
- [Rust Documentation - Slice](https://doc.rust-lang.org/std/primitive.slice.html)

group: rust-slice
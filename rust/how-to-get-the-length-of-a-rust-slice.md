# How to get the length of a Rust slice?
// plain

The length of a Rust slice can be obtained using the `len()` method.

## Example code

```
let my_slice = [1, 2, 3, 4];
let length = my_slice.len();
```

## Output example

```
4
```

## Code explanation

- `let my_slice = [1, 2, 3, 4];`: This line declares a slice with four elements.
- `let length = my_slice.len();`: This line calls the `len()` method on the slice, which returns the length of the slice.

## Helpful links
- [Rust Documentation - Slices](https://doc.rust-lang.org/stable/book/ch04-03-slices.html)

group: rust-slice
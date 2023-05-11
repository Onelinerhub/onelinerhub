# How to create a slice from a vec in Rust?
// plain

Creating a slice from a vec in Rust is a simple process. The syntax for creating a slice from a vec is `&vec[start..end]`, where `start` is the index of the first element in the slice and `end` is the index of the element after the last element in the slice.

For example, the following code creates a slice of the first three elements of a vec:
```
let vec = vec![1, 2, 3, 4, 5];
let slice = &vec[0..3];
```
The output of this code is `[1, 2, 3]`.

## Code explanation


- `let vec = vec![1, 2, 3, 4, 5];`: This line creates a vec with the elements `1`, `2`, `3`, `4`, and `5`.

- `let slice = &vec[0..3];`: This line creates a slice of the vec `vec` from the first element (index `0`) to the element after the third element (index `3`).

## Helpful links

- [The Rust Programming Language - Slices](https://doc.rust-lang.org/book/ch04-03-slices.html)
- [The Rust Programming Language - Vectors](https://doc.rust-lang.org/book/ch08-01-vectors.html)

group: rust-slice
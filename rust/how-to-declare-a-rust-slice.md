# How to declare a Rust slice?
// plain

A Rust slice is a data structure that allows access to a contiguous sequence of elements in a collection. It is declared using the `&[T]` syntax, where `T` is the type of the elements in the slice.

## Example

```
let numbers = [1, 2, 3, 4, 5];
let slice = &numbers[1..3];
```

This example creates a slice of the `numbers` array, containing elements at indices 1 and 2 (inclusive). The output of this code is `[2, 3]`.

The parts of the code are:
- `let numbers = [1, 2, 3, 4, 5];`: This declares an array of 5 elements.
- `let slice = &numbers[1..3];`: This creates a slice of the `numbers` array, containing elements at indices 1 and 2 (inclusive).

## Helpful links
- [Rust Documentation - Slices](https://doc.rust-lang.org/book/ch04-03-slices.html)
- [Rust by Example - Slices](https://doc.rust-lang.org/rust-by-example/slice.html)

group: rust-slice
# Can you provide an example of a Rust slice?
// plain

A Rust slice is a data structure that allows you to reference a contiguous sequence of elements in a collection. It is similar to an array, but does not own the data it references.

## Example code

```
let numbers = [1, 2, 3, 4, 5];
let slice = &numbers[1..3];
```

## Output example

```
[2, 3]
```

The code above creates a slice of the array `numbers` from index 1 to index 3 (not including index 3). The slice contains the elements `2` and `3`.

## Helpful links
- [Rust Documentation - Slices](https://doc.rust-lang.org/stable/book/ch04-03-slices.html)
- [Rust by Example - Slices](https://doc.rust-lang.org/stable/rust-by-example/slice.html)

group: rust-slice
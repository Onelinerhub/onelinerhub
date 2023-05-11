# How to convert a slice into an iter in Rust?
// plain

To convert a slice into an iter in Rust, you can use the `iter()` method. This method takes a slice and returns an iterator over its elements.

## Example

```
let slice = [1, 2, 3];
let iter = slice.iter();
```

## Output example

```
iter
```

The `iter()` method takes a slice and returns an iterator over its elements. The iterator can then be used to iterate over the elements of the slice.

## Code explanation

- `iter()`: method that takes a slice and returns an iterator over its elements

## Helpful links
- [Rust Documentation - Iterator](https://doc.rust-lang.org/std/iter/trait.Iterator.html)

group: rust-slice
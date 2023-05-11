# How to convert a Rust slice to an array?
// plain

To convert a Rust slice to an array, you can use the `into_iter()` method. This method will return an iterator over the slice, which can then be collected into an array.

## Example code

```
let slice = [1, 2, 3];
let array: [i32; 3] = slice.into_iter().collect();
```

## Output example

```
[1, 2, 3]
```

## Code explanation

- `let slice = [1, 2, 3];`: This creates a slice containing the values 1, 2, and 3.
- `let array: [i32; 3] =`: This declares a new array with the type `i32` and a length of 3.
- `slice.into_iter()`: This creates an iterator over the slice.
- `.collect()`: This collects the iterator into an array.

## Helpful links
- [Rust Documentation - Iterator](https://doc.rust-lang.org/std/iter/trait.Iterator.html)
- [Rust Documentation - IntoIterator](https://doc.rust-lang.org/std/iter/trait.IntoIterator.html)

group: rust-slice
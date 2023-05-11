# How to get the minimum value of a Rust slice?
// plain

The minimum value of a Rust slice can be obtained using the `min()` method. This method takes a closure as an argument which is used to compare two elements of the slice and return the minimum value.

## Example code

```rust
let slice = [1, 2, 3, 4, 5];
let min = slice.min().unwrap();
```

## Output example

```
1
```

## Code explanation

- `let slice = [1, 2, 3, 4, 5];`: This line creates a slice containing the values 1, 2, 3, 4, and 5.
- `let min = slice.min().unwrap();`: This line calls the `min()` method on the slice, which returns an `Option` containing the minimum value. The `unwrap()` method is used to extract the value from the `Option`.

## Helpful links
- [Rust Documentation - min()](https://doc.rust-lang.org/std/primitive.slice.html#method.min)

group: rust-slice